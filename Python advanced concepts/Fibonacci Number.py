def Fibonacci_series(x):
  # creating an array in the function
   fib_Array = [0] * (x + 1)
   fib_Array[1] = 1
   # adding elements of the series to the array using addition of previous two elements.
   for n in range (2, x + 1):
      fib_Array[n] = fib_Array[n - 1] + fib_Array[n - 2]
   return fib_Array[x]
if __name__ == "__main__":
   print("12th element of the Fibonacci series:", Fibonacci_series(12))