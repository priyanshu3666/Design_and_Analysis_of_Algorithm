def insertionSort(arr):
   for index in range(1,len(arr)):

     currentvalue = arr[index]
     position = index

     while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1

     arr[position]=currentvalue

arr = [45,89,62,31,15,25,10]
insertionSort(arr)
print(arr)
