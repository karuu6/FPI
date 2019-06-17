from new import popt, func
from factor import *
import numpy as np
import math
import time

def brute_force(n):
	i=2
	while i<n:
		if n % i ==0:
			return i
		i+=1

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

nums=rf('3', '4', rst=False)
s=0
v=0
for n in nums:
	seed=func(n,*popt)
	t1=time.time()
	k=factor(n,seed)
	t2=time.time()
	if k:
		s+=t2-t1
		v+=1

print('FPI %f seconds' % (s/v))

s=0
v=0
for n in nums:
	t1=time.time()
	k=brute_force(n)
	t2=time.time()
	s+=t2-t1
	v+=1
print('Brute Force %f seconds' % (s/v))
