import math
from gmpy2 import mpfr,sqrt
import sys

def F(x,a):
	return pow(x,a)

def G(x,r):
	return r*x

def H(x,a):
	return pow(x,1/a) 

def iter(p,z,r,k):
	x=int(p)
	b=G(z%x,r)
	a=H(p,k)
	return F(a+b,k)

def factor(n,s):
	r=0.5
	while r < 4.5:
		a=0.8
		while a < 1.1:
			old_p=0
			p=s
			i=0
			while abs(p-old_p)>0.00001 and i < 20 and p < sqrt(n):
				old_p=p
				p=iter(old_p,n,r,a)
				i+=1
			if abs(p-old_p)<=0.00001:
				#print('{}'.format(int(p)))
				return True
			a+=0.005
		r+=0.1
	return False
