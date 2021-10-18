#Documentation at the end of this code.

print("Creating two text files one with 10 million random integers. Another with 10 thousand random integers.")
print("wait...")
import random
f=open('input.txt', 'w+')
n=10000000
num=0
for i in range(n):
    num=random.randint(1,n)
    f.write(str(num)+'\n')
f.close()

import random
f=open('small.txt', 'w+')
n=1000
num=0
for i in range(n):
    num=random.randint(1,n)
    f.write(str(num)+'\n')
f.close()

#Using program for finding maximum element as program with linear run time.
def linear_fn(L):
    max_element=0
    for i in range(len(L)):
        if L[i]>max_element:
            max_element=L[i]
    return max_element

with open('input.txt') as f:
    L = f.readlines()
    L = [int(i) for i in L]

import time
import csv

#Creating a csv and storing all output in the new csv.                  
with open('linear_output.csv','w+', newline='') as file:
    print("Starting Linear Time Program")
    go=time.time()                               #go time to start clocking.
    for i in range(100000,len(L),100000):
        k=linear_fn(L)
        stop=time.time()                #stop clocks return time of each output.
        run_time=(stop-go)              #run time is the difference between stop and go.   
        lin=i,go,stop,run_time
        writer=csv.writer(file)         # i gives the run length. We jump to spped up the clocking.
        writer.writerow(lin)            #each clocked time is merged with the csv file right away.
        print(i,go,stop,run_time)
print("----------------xxx-------------xxxxxx--------------xxx----------------")

print("Now plotting this data...")

print("----------------xxx-------------xxxxxx--------------xxx----------------")

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('linear_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='y is Time, x is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Time Growth')
plt.legend()
plt.show()

#Using program for Bubble sort as program with exponential(quadratic) run time.
def poly_fn(L):
    for i in range(0,len(L)):
        min=i
        for j in range(i+1,len(L)):
            if L[j]<L[min]:
                min=j
        L[i],L[min]=L[min],L[i]
    return L

with open('small.txt') as f:            #Used a smaller imput sample with 10000 elements as the bigger one choked on PC.
    L = f.readlines()
    L = [int(i) for i in L]

import time
import csv

with open('poly_output.csv','w+', newline='') as file:
    print("Starting Polynomial Time Program")
    go=time.time()
    for i in range(100,len(L),10):
        k=poly_fn(L)
        stop=time.time()
        run_time=stop-go
        lin=i,go,stop,run_time
        writer=csv.writer(file)
        writer.writerow(lin)
        print(i,go,stop,run_time)
print("----------------xxx-------------xxxxxx--------------xxx----------------")

print("Now plotting this data...")

print("----------------xxx-------------xxxxxx--------------xxx----------------")

x = []
y = []

with open('poly_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='y is Time, x is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Time Growth')
plt.legend()
plt.show()

#Using program for Sublist in a List for Exponential run time.        
def exp_fn(L):
    f = [[]]
    for i in range(len(L) + 1):
        for j in range(i):
            f.append(L[j:i])
    return f

with open('small.txt') as f:
    L = f.readlines()
    L = [int(i) for i in L]

import time
import csv

with open('exp_output.csv','w+', newline='') as file:
    print("Starting Exponential Time Program")
    go=time.time()
    for i in range(100,len(L),10):        
        k=exp_fn(L)
        stop=time.time()
        run_time=stop-go
        lin=i,go,stop,run_time
        writer=csv.writer(file)
        writer.writerow(lin)
        print(i,go,stop,run_time)
print("----------------xxx-------------xxxxxx--------------xxx----------------")

print("Now plotting this data...")

print("----------------xxx-------------xxxxxx--------------xxx----------------")

x = []
y = []

with open('exp_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='y is Time, x is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Time Growth')
plt.legend()
plt.show()

#Using program for BBinary Search for Logarithmic run time.         
def log_fn(L,I):
    first = 0
    last = len(L)-1
    found = False

    while first<=last and not found:
        midpoint = round((first + last)/2)
        if L[midpoint] == I:
            found = True
        else:
            if I < L[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

with open('input.txt') as f:
    L = f.readlines()
    L = [int(i) for i in L]

import random

I=random.choice(L)

import time
import csv

with open('log_output.csv','w+', newline='') as file:
    print("Starting Logarithmic Time Program")
    go=time.time()
    for i in range(100000,len(L),100000):
        k=log_fn(L,I)
        stop=time.time()
        run_time=stop-go
        lin=i,go,stop,run_time
        writer=csv.writer(file)
        writer.writerow(lin)
        print(i,go,stop,run_time)
print("----------------xxx-------------xxxxxx--------------xxx----------------")

print("Now plotting this data...")

print("----------------xxx-------------xxxxxx--------------xxx----------------")

x = []
y = []

with open('log_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='y is Time, x is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithmic Time Growth')
plt.legend()
plt.show()

'''Documentation.
The program is giving certain erroneous results.
Linear Results are coming for Exponential and Polynonmial run time while 
Logarithmic is returning a step function graph.
I have double and triple checked the test case programs which seem to be correct. 

The problem seems to be arising while clocking the program start time, which Ii have 
started before the loop. Since the loop will close only after running through the 
program, the value of start is not being stored thus the error.

I have tried but failed to correct this.

Parameters for memory fail-
1. Running 10 million elements for exponential and quadratic time complexities.
2. Spyder crashed while I tried to verify program results by printing fns. for these two cases. 
Rationale - Exponential growth in temporary storage (RAM) requirement for such calculations.
3. Jump argument required while covering large input samples.'''
