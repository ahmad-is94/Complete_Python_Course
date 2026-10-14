try:
    dev = 4//0
    print(dev)
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("finally statement")