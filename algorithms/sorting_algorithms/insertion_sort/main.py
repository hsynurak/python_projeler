#Insertion Sort Algorithm

collection = [8,3,5,1,4,2]


#Insertion Sort Function
def insertion_sort(collection):
     for i in range(1, len(collection)):
          key = collection[i]
          j = i-1
          while j>=0 and collection[j]>key:
               collection[j+1]=collection[j]
               j-=1
          collection[j+1]=key
     return collection
"""
1-) Start the comparison loop from the number one index to last index.
2-) Save the index value as key. 
          Because possible the value at the targer index will be changed. 
          We will be need the value at the end of the loop for swap operation.
3-) Start the second loop from the index one before the key index to the first index.
4-) If the value at the target index is greater than the key value, start the swap operation.
"""


result = insertion_sort(collection)

print(result)
