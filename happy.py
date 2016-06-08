import sys
 
def sum_digits_squared(n):
    s = 0
    while n > 0:
        n, m = n // 10, n % 10
        s = s + m * m
    return s
 
def is_happy(n):
    n0, n1 = n, n
    while True:
        n0 = sum_digits_squared(n0)
        if n0 == 1:
            return True
        n1 = sum_digits_squared(n1)
        n1 = sum_digits_squared(n1)
        if n0 == n1:
            return False
 
happy =  filter(lambda x : is_happy(x), range(int(sys.argv[1])))
 
for h in happy:
        print h
