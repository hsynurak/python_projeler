#Selection Sort Algorithm

collection = [12, 9, 45,324,7,5,1,0,67823498, 9023849023]


#Selection Sort Function
def find_sorted_array(collection):
     
     for i in range(len(collection)):
          min_index = i
          for j in range(i+1, len(collection)):
               if collection[i] > collection[j]:
                    min_index = j
          collection[i], collection[min_index] = collection[min_index], collection[i]
     return collection
"""
1-) Find the minimum value for the each index with comparing all values in the collection
2-) Swap the minimum value if it is not in the right index
3-) Repeat the process for all indexes
"""


find_sorted_array(collection)
print("Your sorted array is: ", collection)