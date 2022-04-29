import sympy as sp
from sympy.abc import x,y,z

y = sp.exp(sp.asin(x))
z = sp.exp(-1*sp.acos(x))
print("dy/dx = ",sp.diff(y,x))
print("dz/dx = ",sp.diff(z,x))
print("dy/dz = ",sp.diff(y,x)/sp.diff(z,x))