from multiprocessing import Queue

fruits = ['Apple', 'Orange', 'Guava', 'Papaya', 'Banana']
count = 1
# creating a queue object
queue = Queue()
print('pushing items to the queue:')
for fr in fruits:
    print('item no: ', count, ' ', fr)
    queue.put(fr)
    count += 1

print('\npopping items from the queue:')
count = 0
while not queue.empty():
    print('item no: ', count, ' ', queue.get())
    count += 1  