import matplotlib.pyplot as plt

def readData(file):
	x=[]
	y=[]
	with open(file,'r') as f:
		for i in f.readlines():
			n=float(i.split(' ')[0])
			s=float(i.split(' ')[1])
			x.append(n)
			y.append(s)
	return x,y


x,y=readData('pairs')


plt.scatter(x,y,label='Original data')
plt.title("Converging Seeds")
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel("Sample Integers")
plt.ylabel("Seeds")
plt.savefig('seed-data.png')
plt.show()