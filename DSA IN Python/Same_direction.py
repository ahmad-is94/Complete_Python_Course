def clean(names):
    left=0
    for right in range(1,len(names)):
        if names[right]!=names[left]:
            left=left+1
            names[left]=names[right]
            return left +1
names = ['ali','ali','ahmad','s','ali','ahmad']
count = clean(names)
print(names[:count])