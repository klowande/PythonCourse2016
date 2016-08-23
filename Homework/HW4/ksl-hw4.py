# ksl hw4 'algorithms'
import random
import itertools
import time

# Sorting Algorithm 1: Bogosort - worst of all, according to wikipedia. O((n+1)!)

def bogoSort(numbers):
	while not order(numbers):
		random.shuffle(numbers)
    
# Sorting Algorithm 2: Insertion Sort - O(n^2)

def insertionSort(numbers):
	n = len(numbers)
	for position in range(1,n):
		current = numbers[position]
		while position >= 1 and numbers[position-1]>current:
			numbers[position]=numbers[position-1]
			position+=-1
		numbers[position] = current
	
# Supporting Function for Checking Order
def order(x):
    for i in range(len(x) - 1):
        if x[i]>x[i+1]: return False
    return True
    
bogo = []
insert = []
n = range(1,201)
 
for i in range(1,201):
	A = random.sample(range(1,1000),i)
	B = random.sample(range(1,1000),i)
	t1 = time.time()
	bogoSort(A)
	t2 = time.time()
	insertionSort(B)
	t3 = time.time()
	bogo.append(t2-t1)
	insert.append(t3-t2)
	

