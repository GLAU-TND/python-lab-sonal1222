try:
    n=int(input("enter no:"))+ input()
    n.count()
except(AttributeError):
    print(" attribute Error occured")
except (TypeError):
    print("type error occured")
except(ValueError):
    print("Value error occured")
