from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg, stats


OUT = Path("plots")
OUT.mkdir(exist_ok=True)

A = np.array([[1, -2, 3], [4, 5, 6], [7, 1, 9]], dtype=float)
b = np.array([1, 2, 3], dtype=float)
x = linalg.solve(A, b)
print("A x = b")
print(x)
print(np.allclose(A @ x, b))

rng = np.random.default_rng(0)
B = rng.random((3, 3))
X = linalg.solve(A, B)
print("A X = B")
print(X)
print(np.allclose(A @ X, B))

eigenvalues, eigenvectors = linalg.eig(A)
print("eigenvalues")
print(eigenvalues)
print("eigenvectors")
print(eigenvectors)

print("inverse")
print(linalg.inv(A))
print("determinant")
print(linalg.det(A))
for order in [None, "fro", 1, 2, np.inf]:
    print(f"norm {order}: {linalg.norm(A, ord=order)}")

poisson = stats.poisson(mu=4)
k = np.arange(0, 15)
poisson_samples = poisson.rvs(size=1000, random_state=rng)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].stem(k, poisson.pmf(k))
axes[1].step(k, poisson.cdf(k), where="post")
axes[2].hist(poisson_samples, bins=np.arange(-0.5, 15.5, 1), density=True)
fig.tight_layout()
fig.savefig(OUT / "poisson.png")
plt.close(fig)

normal = stats.norm(loc=0, scale=1)
z = np.linspace(-4, 4, 400)
normal_samples = normal.rvs(size=1000, random_state=rng)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(z, normal.pdf(z))
axes[1].plot(z, normal.cdf(z))
axes[2].hist(normal_samples, bins=30, density=True)
fig.tight_layout()
fig.savefig(OUT / "normal.png")
plt.close(fig)

sample1 = stats.norm(loc=0, scale=1).rvs(size=200, random_state=rng)
sample2 = stats.norm(loc=0.2, scale=1).rvs(size=200, random_state=rng)
print("ttest_ind")
print(stats.ttest_ind(sample1, sample2))
