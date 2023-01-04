# given an array that contains only 0s and 1s,
# where zeros may only ever appear before ones or not at all,
# return the index of the first 1, or -1 if there are none, or if there are no zeros
# the unique thing about this search is that it's done in a binary fashion, 
# i.e., splitting the array in half each time

def search_ones(arr):
  left, index, right = 0, 1, len(arr)-1

  # if the array is empty, return -1
  if right == -1 or arr[left] == arr[right]:
    return -1
  
  # if the value at `index` is 1 and the value to its immediate left is 0,
  # then `index` is the first value where a 1 appears. return that
  if arr[left] < arr[index]:
    return index 

  # now we move through the array, doubling the index at each pass, and stop only
  # when we see a 1
  while arr[index] != 1:
    index *= 2
    # just making sure we don't pass the end of the array
    if index > right:
      index = right
      break

  while left < right:
    m = (left+right)//2 # middle point of the array
    # if there is a 1 to the left of the midpoint, set the end of the array to that index
    if arr[m-1] == 1: 
      right = m - 1
    
    # if the above condition does not pass, that means the value was a 0. if the value of the 
    # midpoint is a 1, that's the first 1 in the array, so return that index
    elif arr[m] == 1:
      return m
    
    # if the above condition does not pass, that means the middle was a 0. if the value to the 
    # immediate right of the middle is a 1, that's the first one, return
    elif arr[m+1] == 1:
      return m + 1

    # if all else fails, set the beginning of the array to the `middle + 1` position, and repeat
    else:
      left = m + 1

# TESTS
# to cover the three cases that should return -1
a1 = []
a2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
a3 = [1, 1, 1, 1]

# to cover the case where the second element is a 1
# test with big and small n-m
a4 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
a5 = [0, 1]

# large m
a6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
a7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# other general cases
a8 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
a9 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] 