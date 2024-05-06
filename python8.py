# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time
print(time.ctime())
#Start code below this line:
for i in range(1, 6):
    print("Mississippi", i)
    #1 second pause
    time.sleep(1)

print("Ready or not, here I come!")

print(time.strftime("%Y-%m-%d %H:%M:%S"))