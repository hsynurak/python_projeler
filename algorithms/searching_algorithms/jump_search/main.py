#Jump Search Algorithm

import math

collection = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#Jump Search Function
def find(collection, target):
     blocksize = int(math.sqrt(len(collection)))
     
     end = blocksize
     start = 0
     
     while (collection[end] <= target and end < len(collection)):
          start = end
          end += blocksize
          break
          
     for i in collection[start:end]:
          if i == target:
               return i
          
     return -1
"""
1-) Find the block size of the collection
     Best block size is sqrt of the collection
2-) Create start and end variables for target block
3-) Check if target is in the block
4-) If target is not in the block, increase end and start variables as block size
5-) If target is in the block, check the block with linear search
"""

#taking input from user for target
target = int(input("Please enter the target:"))
result = find(collection, target)


#giving output to user about target
if result == -1:
     print("Collections doesn't contain the target")
else:
     print("Collections contains the target at index %s" %(result-1))
     
     