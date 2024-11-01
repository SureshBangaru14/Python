# here we are creating our first Thread.
# before going to thred using time.sleep()

import time

def do_work():
    print("Start Work")
    time.sleep(1) # this means wait for 1 secounds.
    print("Finshed Work")

for _ in range(5):
    do_work()

# we are getting like this output.
# here code excuted line by line.
# here process complete line by line.
'''
Start Work
Finshed Work
Start Work
Finshed Work
Start Work
Finshed Work
Start Work
Finshed Work
Start Work
Finshed Work

'''


######################################################
print("\n\n")
print("With using Thread Concept")
# With using Thread Concept.

from threading import Thread

def do_work():

    print("Start Work")
    time.sleep(1) # this means wait for 1 secounds.
    i=0
    for _ in range(20000000):
        i+=1
    print("Finshed Work")


for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()

# we are getting like this output with using Thread.
# here complete 1 line and 1 process and all iterations.

'''
Start Work
Start Work
Start Work
Start Work
Start Work
Finshed Work
Finshed Work
Finshed Work
Finshed Work
Finshed Work

'''

