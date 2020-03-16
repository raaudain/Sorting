# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    
    # Loop through the array starting at 0
    for i in range(0, len(arr) - 1):
        # Store the first element as the smallest value
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc
        
        # Compare this item to the next item in the array until you find a smaller number
        # i+1 to move to the next index
        for j in range(cur_index+1, len(arr)):
            # If arr[j] is greater than arr[smallest_index], smallest_index = j   
            if arr[j] < arr[smallest_index]:  
                smallest_index = j

        #TO-DO: swap
        
        # If the "mininum" is not the index you initially began with, swap the two values
        if cur_index != smallest_index:
            temp = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = temp


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Start looping through the array with a variable called i
    for i in range(len(arr)):
        # Start an inner loop through the array with 
        # a variable called j until i-1 (stop)
        for j in range(0, len(arr)-i-1):
            # If arr[j] is greater than arr[j+1], swap those two values
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(selection_sort(arr))

# print(bubble_sort(arr))