import timeit

cmd = '"-".join(str(n) for n in range(100))'
print(timeit.timeit(cmd, number=10))