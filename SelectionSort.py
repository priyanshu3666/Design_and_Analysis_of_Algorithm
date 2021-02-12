import sys
A = [98,29,11,32,27,46]
for i in range(len(A)):
    min_index = i
    for j in range(i+1,len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]

print("Sorted Array is")
for i in range(len(A)):
    print("%d" %A[i])