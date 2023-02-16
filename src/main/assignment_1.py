import math # used for the ceiling function

#function for number 6
def function(x: float):
        y = x**3 + 4*x**2 - 10
        return y        


# (1)

# calculation of sign, exponent, and mantissa 
s = 0
c = 2**10 + 2**2 + 2**1 + 2**0
f = .5**1 + .5**2 + .5**3 + .5**5 + .5**7 + .5**8 + .5**9 + .5**12

# calculation of number based on formula from chapter 1.2
num1 = (-1**s) * 2**(c - 1023) * (1 + f)

print(num1)
print("\n")


# (2) using three digit chopping

# chopping variables to perform operations
c = 1030
f = .920
num2 = (-1**s) * 2**(c - 1023) * (1 + f)

print(math.ceil(num2))
print("\n")


# (3) using three digit rounding

# rounding variables to perform operations (only final value changes)
num3 = math.floor(num2) 
print(num3)
print("\n")


# (4)

#calculating absolute error
absError = abs(num1 + 246)
print(absError)

# calculating relative error
relError = absError / abs(num1)
print(relError)
print("\n")


#(5)

# we are solving for n: 1 / (n + 1)^3 < 10^-4
# (n + 1)^3 > 10^4
n = 10**(4/3) - 1

#rounding up because we cannot perform partial iterations
print(math.ceil(n))
print("\n")


# (6) bisection method

# variable declaration
a = -4
b = 7
tol = .0001
i = 0

# based on psuedocode from ch 2.1
while abs(b - a) > tol:
    i += 1
    p = (a + b) / 2
    if ((function(a) < 0 and function(p) > 0) or function(a) > 0 and function(p) < 0):
        b = p
    else:
        a = p

print (math.ceil(p))


