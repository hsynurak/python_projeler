collection = [12,14,34,56,75,89,3,7,5]

def find(collection, target):
     for i in collection:
          if i == target:
               return i
     return target
          
target = int(input("Please enter the target:"))
result = find(collection, target)
index = collection.index(result)

if result == target:
     print("Collections doesn't contain the target")
else:
     print("Collections contains the target at index %s" %index)      


