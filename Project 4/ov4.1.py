# Jennifer Ly, grudat20 upppg 4.1

# Task: Calculate the time complexity for pow, sum1 och sum2

import time
import random 

# O(logn) 
def pow(n):
	"""Return 2^n, where n is a nonnegative integer."""		
	if n == 0:												
		return 1											
	x = pow(n//2)											
	if n%2 == 0:											
		return x*x											
	return 2*x*x											
	# T(1) = 1
	# T(n) = 1 + T(n/2) for n>1 (*)
	# The equation (*) captures the fact that the function performs constant work (that’s the one) 
	# and a single recursive call to a slice of size n/2.

# O(nlogn)
def sum1(a):					
	"""Return the sum of the elements in the list a."""
	n = len(a)											 	
	if n == 0:												
		return 0											
	if n == 1:												
		return a[0]								
	return sum1(a[:n//2]) + sum1(a[n//2:])					
				
# O(n)
def sum2(a):
	"""Return the sum of the elements in the list a."""
	return _sum(a, 0, len(a)-1)

def _sum(a, i, j):
	"""Return the sum of the elements from a[i] to a[j]."""
	if i > j:
		return 0
	if i == j:
		return a[i]
	mid = (i+j)//2
	return _sum(a, i, mid) + _sum(a, mid+1, j)
	
	# T(n) = T(n/2) + T(n/2) (*)
	# (*) Each half is sorted, which takes n/2 operations each, 
	# and then merged together. 
	
# Creates a vector with randomized elements 
def vec(length):
    vec = []
    for i in range(0, length):
        i = random.randint(0, 100)
        vec.append(i) 
    return vec

def main():
	n = [10, 100, 1000, 10000, 100000, 1000000]
	vector = []
	
	# Execution time
	print("Elapsed time for pow() function")
	for i in n:
		start = time.time()
		pow(i)
		print(time.time() - start)
		vect = vec(i)							# creates vectors with length n[i] 
		vector.append(vect)						# puts the vector in the vector-list

	print("\nElapsed time for sum1() function")
	for i in vector:
		start = time.time()
		sum1(i)
		print(time.time() - start)

	print("\nElapsed time for sum2() function")
	for i in vector:
		start = time.time()
		sum2(i)
		start = time.time()

	start = time.time()
	vecto = vec(10000000)
	sum1(vecto)
	print(time.time() - start)

	start = time.time()
	vecto1 = vec(10000000)
	sum2(vecto1)
	print(time.time() - start)




	
main()

