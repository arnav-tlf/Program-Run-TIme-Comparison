import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('linear_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='x is Time, Y is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Time Growth')
plt.legend()
plt.show()


x = []
y = []

with open('poly_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='x is Time, Y is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Time Growth')
plt.legend()
plt.show()

x = []
y = []

with open('exp_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='x is Time, Y is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Time Growth')
plt.legend()
plt.show()

x = []
y = []

with open('log_output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[3])

plt.plot(x,y, label='x is Time, Y is fn run length')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Logarithmic Time Growth')
plt.legend()
plt.show()