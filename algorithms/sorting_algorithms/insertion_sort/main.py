collection = [8,3,5,1,4,2]

def insertion_sort(collection):
     for i in range(1, len(collection)):
          key = collection[i]
          j = i-1
          while j>=0 and collection[j]>key:
               collection[j+1]=collection[j]
               j-=1
          collection[j+1]=key
     return collection

result = insertion_sort(collection)

print(result)
