import threading
import pickle
import queue
import math
import time
import sys

def saveData(x):
	#f=open('pairs','ab')
	#pickle.dump(x,f)
	#f.close()
	with open('pairs','a') as f:
		f.write(' '.join(x)+'\n')



def rf(x, y, rst=False,z=0):
	l1=[]
	l2=[]

	if rst:
		with open(x,'r') as f:
			for i in f.readlines():
				l1.append(int(i.strip('\n')))	
		with open(y,'r') as f:
			for i in f.readlines():
				l2.append(int(i.strip('\n')))
		b=sorted([x*y for x in l1 for y in l2])
		
		i=0
		while i<len(b):
			if b[i]==z:
				return b[i+1:]
			i+=1


	with open(x,'r') as f:
		for i in f.readlines():
			l1.append(int(i.strip('\n')))	
	with open(y,'r') as f:
		for i in f.readlines():
			l2.append(int(i.strip('\n')))
	
	b= sorted([x*y for x in l1 for y in l2])
	return b

	#return list(map(lambda x, y: x*y,l1,l2))

def frange(x, y, z):
	while x<=y:
		yield x
		x+=z

def F(x,a):
	return math.pow(x,a)

def G(x,r):
	return r*x

def H(x,a):
	return math.pow(x,1/a) 

def iter(p,z,r,k):
	x=int(p)
	b=G(z%x,r)
	a=H(p,k)
	return F(a+b,k)

def lowestSeed(n):
	sq = math.sqrt(n)
	m=(sq/10)*0.6
	for s in frange(m,sq,0.01):
		r=0.5
		while r < 4.5:
			a=0.8
			while a < 1.1:
				old_p=0
				p=s
				i=0
				while abs(old_p-p) > 0.000001 and i < 20 and p<sq:			
					old_p=p
					p=iter(p,n,r,a)
					i+=1
				if abs(old_p-p) <= 0.000001:
					print('{} {} {} {}'.format(a,r,s,p))
					return s
				a+=0.005
			r+=0.1






def worker(q):
	pairs=[]
	
	while True:
		n=q.get()
		saveData((str(n),str(lowestSeed(n))))
		q.task_done()

"""
def main():
	nums=rf('1.txt','2.txt')
	pairs=[]

	try:
		for n in nums:
			a=lowestSeed(n)
			pairs.append((n,a))
	except KeyboardInterrupt:
		saveData(pairs)
		sys.exit()
	saveData(pairs)
"""

def main():
	nums=rf('1','2',rst=False)

	#print(len(nums))
	#remember rst
	q=queue.Queue()
	for i in range(16):
		t=threading.Thread(target=worker, args=(q,))
		t.daemon = True
		t.start()

	for i in nums:
		q.put(i)

	q.join()

if __name__ == '__main__':
	main()