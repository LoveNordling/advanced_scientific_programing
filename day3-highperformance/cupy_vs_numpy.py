import numpy as np
import pandas as pd
from IPython import get_ipython

import cupy as cp

sizes = [128, 256, 512, 1024, 2048]
dtypes = [np.float64, np.float32]

def numpy_fft2(a):
    return np.fft.fft2(a)

def cupy_fft2(a):
    y = cp.fft.fft2(a)
    cp.cuda.Stream.null.synchronize()   # important: FFT launch is async on GPU
    return y

# Warm up CUDA context + cuFFT
x0 = cp.random.random((16, 16), dtype=cp.float32)
_ = cupy_fft2(x0)

ip = get_ipython()
rows = []

for dtype in dtypes:
    print(f"\n=== dtype = {dtype.__name__} ===")
    for n in sizes:
        x_np = np.random.random((n, n)).astype(dtype, copy=False)
        x_cp = cp.asarray(x_np)

        # Warm up per size/dtype so plan creation doesn't dominate timing
        _ = cupy_fft2(x_cp)

        t_np = ip.run_line_magic("timeit", f"-o -q numpy_fft2(x_np)")
        t_cp = ip.run_line_magic("timeit", f"-o -q cupy_fft2(x_cp)")

        rows.append({
            "dtype": dtype.__name__,
            "size": f"{n}x{n}",
            "numpy_best_s": t_np.best,
            "cupy_best_s": t_cp.best,
            "speedup_numpy_over_cupy": t_np.best / t_cp.best,
            "cupy_faster": t_cp.best < t_np.best,
        })

df = pd.DataFrame(rows)

# Pretty print
df["numpy_best_ms"] = 1e3 * df["numpy_best_s"]
df["cupy_best_ms"] = 1e3 * df["cupy_best_s"]

display(
    df[
        ["dtype", "size", "numpy_best_ms", "cupy_best_ms",
         "speedup_numpy_over_cupy", "cupy_faster"]
    ].round({
        "numpy_best_ms": 3,
        "cupy_best_ms": 3,
        "speedup_numpy_over_cupy": 2
    })
)

for dtype in df["dtype"].unique():
    sub = df[df["dtype"] == dtype]
    winners = sub.loc[sub["cupy_faster"], "size"].tolist()
    if winners:
        print(f"For {dtype}, CuPy is faster at: {', '.join(winners)}")
    else:
        print(f"For {dtype}, CuPy is not faster for any tested size.")
