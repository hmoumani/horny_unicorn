from time import sleep, time
import math

def ft_progress(lst):
    l_lst = len(lst)
    start = time()
    lst = list(lst)[1:]
    add = 1
    if l_lst % 2 == 0: 
        add=0
        lst = lst + [lst[-1] + 1]
    for i in range(1, l_lst + 1):
        now = time()
        time_done = now - start
        estimated = 0
        estimated = time_done * l_lst / i
        hrs = math.floor(estimated / 3600)
        minn = math.floor((estimated - (3600  * hrs)) / 60)
        scnd = estimated - (3600  * hrs) - (60 * minn)
        print('ETA: ', end="")
        if i and hrs:
            print('{:.0f}'.format(hrs) + 'h ', end="")
        if i and minn:
            print('{:.0f}'.format(minn) + 'm ', end="")
        if i:
            print('{:.2f}'.format(scnd) + 's ', end="")
        print("[{:>3.0f}%]".format(i * 100 / l_lst), end="")
        print("[{:=>{}}>{:<{}}]".format("", int((i / l_lst) * 24),"", 24 - int((i / l_lst) * 24)), end="")
        print("{:{}}/{}".format(i + add, len(str(l_lst)), l_lst), end="")
        print(" | elapsed time ", end="")
        hrs = math.floor(time_done / 3600)
        minn = math.floor((time_done - (3600 * hrs)) / 60)
        scnd = time_done - (3600 * hrs) - (60 * minn)
        if hrs:
            print('{:.0f}'.format(hrs) + 'h ', end='')
        if minn:
            print('{:.0f}'.format(minn) + 'm ', end='')
        print('{:.2f}'.format(scnd) + 's', end='\r')
        yield i

if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)

    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
    
    
# current / total * size

# x -> size
# current / total