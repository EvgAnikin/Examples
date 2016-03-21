XMIN = -4.
XMAX = 4.
N = 1000
DX = (XMAX - XMIN)/N
XVALUES = [XMIN + DX*i for i in range(N)]
a = 0.5


def initial():
	u = []
	for i in range(N):
		x = XMIN + i*DX
		u.append(2/(1 + 4*x**2))
	return u

def update(u):
	u_new = []
	for i in range(len(u)):
		new_value = u[i] - 0.5*a*(u[i]**2 - u[i-1]**2)
		u_new.append(new_value)
	return u_new
