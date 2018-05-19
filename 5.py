from math import gcd
a = [i for i in range(1,21)]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  num = (lcm*i)
  den = gcd(lcm, i)
  lcm = num // den

print(lcm)
