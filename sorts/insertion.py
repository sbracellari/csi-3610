a = [10, 8, 1, 3, 0, 9, 4, 7, 6, 2, 5]

def insertion_sort(arr):
  for i in range(1, len(arr)):
    cv = arr[i]
    pos = i

    while pos > 0 and arr[pos-1] > cv:
      arr[pos] = arr[pos-1]
      pos = pos-1

    arr[pos] = cv
  return arr