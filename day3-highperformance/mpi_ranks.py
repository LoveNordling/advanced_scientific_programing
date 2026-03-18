from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
local_value = rank

total_sum = comm.allreduce(local_value, op=MPI.SUM)


if rank == 0:
    print("rank is: ", rank)
    print("sum of ranks is:", total_sum)
