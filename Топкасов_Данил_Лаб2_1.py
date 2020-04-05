
# 35-ое число Фибоначчи 



print("Формула Бине")
import timeit
test1 = """
n = int(35)
def FB(n):
    answer=(pow((1+sqrt(5))/2, n)-pow((1-sqrt(5))/2, n))/sqrt(5)
    return answer
"""
time1 = timeit.timeit(test1, number=100)/100
print(time1)



print("Итерационая формула")
test2 = """
n = int(35)
def ItF(n):
        a, b = 1, 1
        for i in range(3,n+1):
            if (i%2 == 0):
                a+=b
            else:
                b+=a
        if (a>b):
            return a
        else:
            return b
"""
time2 = timeit.timeit(test2, number=100)/100
print(time2)



print("Разделяй и властвуй")
test3 = """
n = int(35)
RV = lambda n: RV(n - 1) + RV(n - 2) if n > 2 else 1
"""
time3 = timeit.timeit(test3, number=100)/100
print(time3)



print("Нисходящие ДП")
test4 = """
n = int(35)
ndp = {0: 0, 1: 1}
def NDP(n):
    if n in ndp:
        return ndp[n]
    ndp[n] = NDP(n - 1) + NDP(n - 2)
    return ndp[n]
"""

time4 = timeit.timeit(test4, number=100)/100
print(time4)



print("Восходящие ДП")
test5 = """
n = int(35)
def VDP(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
"""
time5 = timeit.timeit(test5, number=100)/100
print(time5)