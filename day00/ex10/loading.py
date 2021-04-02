from time import sleep, time

def ft_progress(lst):
    for elem in lst:
        now = time()
        print(time)
        yield elem


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.005)
print()
print(ret)