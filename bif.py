import matplotlib.pyplot as plt

def lgs(k,x):
	return k*x*(1 - x)

def ntherm(k):
	if k < 3:
		return 100
	else:
		return 1000

dk = 0.0025
MAXBIF = 20

k = 3.25

while k < 4:
	k+=dk
	x = 0.5

	for i in xrange(ntherm(k)):
		x = lgs(k,x)
	for i in xrange(MAXBIF):
		x = lgs(k,x)
		plt.plot(x,k, ',b')

#plt.show()
plt.savefig('bif.png')
