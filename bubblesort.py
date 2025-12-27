# Given a list of numbers in range 1 to 100, sort in ascending order according
# to the bubble sort algorithm, measuring time taken.

# Elizabeth Goulborn
# 26/12/2025

import random
import time

# Initialisation
swap = True
passes = 0
num_swaps = 0
n = 5
og_list = random.sample(range(1,100),n)
list = og_list.copy()

start = time.time()
# Code multiple passes
while swap == True:
	# Code pass
	swap = False
	for L in range(len(list)-1):
		if list[L] > list[L+1]:
			list[L], list[L+1] = list[L+1], list[L]
			num_swaps += 1
			swap = True
	passes += 1
	# Exit loop once list is sorted
	if swap == False:
		break
end = time.time()
time_taken = end - start

# Print results
print("Unsorted list: " + str(og_list))
print("Bubblesorted list: " + str(list))
print(str(passes) + " passes (including verification pass)")
print(str(num_swaps) + " swaps")
print(str(time_taken) + "s to complete algorithm")
