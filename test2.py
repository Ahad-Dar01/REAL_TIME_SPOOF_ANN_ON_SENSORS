import time
def stat():
 for i in range(10):
    print(i)
    i=i+1
    time.sleep(1)
 return i,i+1
a,b=stat()
print(a)
##only returning to a will make an 'a' a tuple
# returning in for will terminate the for loop
# using a for loop incrementor wont be effective in python but in c