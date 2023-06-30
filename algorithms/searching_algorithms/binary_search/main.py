# Binary Search Algorithm


# Sorted Array
collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Binary search function
def find(collection, target):
     lower_bound = 0
     upper_bound  = len(collection) - 1
     
     while lower_bound <= upper_bound:
          mid = (lower_bound + upper_bound) // 2
          
          if collection[mid] == target:
               return mid
          elif collection[mid] < target:
               lower_bound = mid+1
          elif collection[mid] > target:
               upper_bound = mid-1
     return -1
"""
1-) Find the mid index of the collection
2-)If mid index is equal to target, return mid index
3-)If mid index is not equal to target, check if mid index is less or greater than target
4-)If target is not found, return -1
"""

#taking input from user for target
target = int(input("Please enter the target:"))
result = find(collection, target)


#giving output to user about target
if result == -1:
     print("Collections doesn't contain the target")
else:
     print("Collections contains the target at index %s" %result)
