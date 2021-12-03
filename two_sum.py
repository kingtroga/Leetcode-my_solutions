def two_sum(nums, target):
	hash_table = {}
	for i in range(len(nums)):
		complement = target - nums[i]
		if hash_table.get(complement):
			continue
		else:
			hash_table[complement] = i

	for i in range(len(nums)):
		# does the element at this index exist as a key
		if hash_table.get(nums[i]):
			# and if it does what is the value of this key 
			j = hash_table.get(nums[i])
			if not (j == i):
				return [i, j]

	return -1

		
print(two_sum([3,3], 6))
