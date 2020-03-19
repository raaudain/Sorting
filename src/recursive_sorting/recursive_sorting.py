# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    elements = len( arrA ) + len( arrB )
    merged_arr = [] * elements
    
    # TO-DO
    
    # Variables i and j equaling to 0
    # Created to change index numbers
    i = 0
    j = 0
    
    # While i is less than the length of array A
    # and while j is less than array B, the conditional will continue
    while i < len(arrA) and j < len(arrB):
        # If the index of array A is less than the index of array B...
        if arrA[i] < arrB[j]:
            # Append the index of array A to the list
            merged_arr.append(arrA[i])
            # Add 1 to i changing the index number for the next pass
            i+=1
            
        # If the index of array A is greater than the index of array B...
        else:
            # Append the index of array A to the list
            merged_arr.append(arrB[j])
            # Add 1 to j changing the index number for the next pass
            j+=1

    # This will append any left over numbers 
    # if array A is longer than array B
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i+=1
    
    # This will append any left over numbers 
    # if array B is longer than array A
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j+=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # If the array is less than or equal to one,
    # return it to the function
    if len(arr) <= 1:
        return arr
    
    # Splits the array in half
    middle = len(arr)//2
    
    # Left side of the array is returned to the merge_sort function
    # and divided again and again until it is no longer divisible
    left = merge_sort(arr[0:middle])
    
    # Right side of the array is returned to the merge_sort function
    # and divided again and again until it is no longer divisible
    right = merge_sort(arr[middle:])
    
    # Sends left and right arrays to merge function above
    arr = merge(left, right)

    return arr



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr



#print(merge([1, 5, 6, 7, 20], [0, 12, 16, 89]))

# arr = [1, 5, 44, 7, 20, 100, 30000, 2, 78, 19, 20, 0]
# print(merge_sort(arr))