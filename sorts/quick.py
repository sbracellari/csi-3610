from insertion import insertion_sort

a = [10, 8, 1, 3, 0, 9, 4, 7, 6, 2, 5]

def partition(a, l, u):
  t = a[l]
  m = l

  for i in range(l+1, u+1):
    if a[i] < t:
      m += 1
      a[i], a[m] = a[m], a[i]
  a[m], a[l] = a[l], a[m]
  return m

def quicksort(a, l=0, u=None):
  if u is None:
    u = len(a)-1
  if l < u:
    m = partition(a, l, u)
    quicksort(a, l, m-1)
    quicksort(a, m+1, u)
  return a

print(quicksort([6, 2, 8, 12, 5, 1, 8, 10]))

# a better implementation of quicksort, using insertion sort for small arrays
# since it's faster
def quicksort1(a, l=0, u=None):
  if u is None:
    u = len(a)-1
  if l < u-128:
    m = partition(a, l, u)
    quicksort1(a, l, m-1)
    quicksort1(a, m+1, u)
  elif l < u:
    insertion_sort(a, l, u)
  return a