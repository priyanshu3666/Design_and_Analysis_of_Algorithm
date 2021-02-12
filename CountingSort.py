#This code is written by Priyanshu Shukla
#language used:- Python
#This code is written to implement the concept of countinng sort
def counting_sort(array1, max_value):
    m = max_value + 1
    count = [0] * m

    for a in array1:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1
    return array1


print(counting_sort([17,85,65,15,71,62],85))