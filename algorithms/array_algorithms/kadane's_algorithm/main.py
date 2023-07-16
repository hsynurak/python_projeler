A = [-2,1,-3,4,-1,2,1,-5,4]

def find_max_sum_array(A):
     current_sum = A[0]
     max_sum = A[0]

     for i in range(1,len(A)):
          current_sum = max(A[i],current_sum + A[i])
          max_sum = max(current_sum,max_sum)
     return max_sum

print(find_max_sum_array(A))