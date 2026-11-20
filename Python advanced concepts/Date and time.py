# import time;
# #prints the number of ticks spent since 12 AM, 1st January 1970
# print(time.time())

import time

# returns a time tuple

print(time.localtime(time.time()))
for i in range(0,5):
    print(i)
    #Each element will be printed after 1 second
    time.sleep(1)

# returns the formatted time

print(time.asctime(time.localtime(time.time())))