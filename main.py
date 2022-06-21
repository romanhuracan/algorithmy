# -*- coding: utf-8 -*-


def binary_search(n: int, sorted_array: list):
	low = 0
	high = len(sorted_array) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = sorted_array[mid]

		if guess > n:
			high = mid - 1
		elif guess < n:
			low = mid + 1
		else:
			return mid

	return None


if __name__ == '__main__':
	print(binary_search(2, [1,2,3]))
