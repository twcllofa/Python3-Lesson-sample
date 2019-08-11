def add(*args):
    if args != ():
        sum = 0 
        for i in args:
            sum += i

        return sum
    else:
        return None
print(add(1,2,3,4))