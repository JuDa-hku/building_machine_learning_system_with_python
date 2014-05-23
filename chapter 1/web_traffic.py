import scipy as sp
data=sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10])
print(data.shape)
x=data[:,0] #choose the columns individually
y=data[:,1]
print sp.sum(sp.isnan(y))
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("time")
plt.ylabel("Hite/hour")
plt.xticks([w*7*24 for w in range(10)],
['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()

def error(f, x, y):
    return sp.sum((f(x)-y)**2)
## use polynomial of degree 1
fp1, res, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
print("Model parameters: %s" %fp1)
print(res)
f1=sp.poly1d(fp1)
print("error is %s" %error(f1, x, y,))
fx=sp.linspace(0, x[-1], 1000)
#plt.plot(fx, f1(fx), linewidth=4)

### use polynomial of degree 2
f2p=sp.polyfit(x, y, 2)
print(f2p)
f2=sp.poly1d(f2p)
#plt.plot(fx, f2(fx), linewidth=4)
print("2 degree error %s" %error(f2, x, y))
for i in range(11):
    fp=sp.polyfit(x, y, i)
    fip=sp.poly1d(fp)
    print("%s degree error %s" %(i, error(fip, x, y)))
inflection= 3.5*7*24 ## from the plt, find the inflection point
xpart1=x[:inflection]
xpart2=x[inflection:]

ypart1=y[:inflection]
ypart2=y[inflection:]

fpar1=sp.polyfit(xpart1, ypart1, 1)
fpar2=sp.polyfit(xpart2, ypart2, 1)

f1=sp.poly1d(fpar1)
f2=sp.poly1d(fpar2)

print("Two part error %f" %(error(f1, xpart1, ypart1)+error(f2, xpart2, ypart2)))
fx1=sp.linspace(0, inflection, 1000)
fx2=sp.linspace(inflection, x[-1], 1000)


plt.plot(fx1, f1(fx1), 'r--', linewidth=3)
plt.plot(fx2, f2(fx2), '--', linewidth=3 )
plt.legend(["d=%i" % f1.order, "d=%i" % f2.order], loc="upper left")
plt.show()

fb=sp.polyfit(xpart2, ypart2, 2)
fbt2=sp.poly1d(fb)
print(fbt2)
print(fbt2-100000)
from scipy.optimize import fsolve
reached_max = fsolve(fbt2-100000, 800)/(7*24)
print ("10,000 hits/hour expected at week %f" % reached_max[0])
