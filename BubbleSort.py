#this code is written by Priyanshu Shukla
#language used => Pyhton
def bubblesort(arr):
    n = len(arr)
    for i in  range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr =  [12,54,24,64,59,13]
bubblesort(arr)
print("Sorted Array is")
for i in range(len(arr)):
    print("%d " %arr[i])