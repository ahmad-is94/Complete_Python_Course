import sys
print(sys.version)
#Input and Output using sys Module
for line in sys.stdin:
    if line.strip() == "exit":
        break
    print("Input:", line.strip())
print("Exit")