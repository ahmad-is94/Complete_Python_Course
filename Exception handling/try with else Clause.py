def reciprocal(num):
    try:
        reci = 1/num
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print(reci)



reciprocal(4)
reciprocal(0)
