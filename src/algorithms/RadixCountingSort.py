def countingsort(l, d, r):
   #l - list
   #d - digit to sort of a number
   #r - radix for decical it is 10
   out = [0]*len(l)
   rl = [0]*r

   for i in range(len(l)):
      rl[(l[i]//r**d)%r] = rl[(l[i]//r**d)%r] + 1
   
   for j in range(1, r):
      rl[j] = rl[j] + rl[j-1]

   for m in range(len(l)-1, -1, -1):
      rl[(l[m]//r**d)%r] = rl[(l[m]//r**d)%r] - 1
      out[rl[(l[m]//r**d)%r]] = l[m]
   
   return out

def radixsort(l, m, r):
   #l - list to sort
   #m - maximum digits for numbers in list
   #r - radix
   out = l
   for i in range(m):
      out = countingsort(out, i, r)
   
   return out

if __name__ == "__main__":
   import random
   rn = 500
   l = []
   for i in range(rn):
      l.append(random.randrange(rn))
   print(radixsort(l, 3, 10))