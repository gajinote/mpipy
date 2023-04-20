from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()  # サイズ（指定されたプロセス数）
rank = comm.Get_rank()  # ランク（プロセスID）
name = MPI.Get_processor_name()

my_self = MPI.COMM_SELF
my_size = my_self.group.Get_size()
my_rank = my_self.group.Get_rank()

if rank == 0:
  print("From the New World: rank %d of %d running on %s (SELF rank %d of %d)"
    % (rank, size, name, my_rank, my_size), end = ' ')
  for i in range(1, size):
    wrold_rank, your_name, your_rank, your_size = comm.recv(source=i, tag=1)
    print(workd_rank, world_size, your_name, your_size)
else:
  comm.send((rank, size, name, my_rank, my_size), dest=0, tag=1)

MPI.Finalize()
