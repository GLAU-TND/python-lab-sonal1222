class MyException(Exception):
    def __init__(self,v):
        self.v=v
        def __str__(self):
            return self.v
def xyz(a,b):
    c=a+b
    if c<150:
        raise TypeError("custom exception occured")
    else:
        return c
a=int(input())
b=int(input())
print(xyz(a,b))
