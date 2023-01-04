
from insertion import insertion_sort

a = [10, 8, 1, 3, 0, 9, 4, 7, 6, 2, 5]
  
def bin_sort(arr):
  n, size = len(arr), max(arr)/len(arr)

  bins = [[] for _ in range(n)]
  for i in range(n):
    num = int(arr[i]/size) # to get bin numbers
    if num != n:
      bins[num].append(arr[i])
    else:
      bins[n-1].append(arr[i])

  for i in range(n):
    insertion_sort(bins[i])

  arr = []
  for i in range(n):
    arr += bins[i]
 
  return arr