a = [10, 8, 1, 3, 0, 9, 4, 7, 6, 2, 5]

def new_heap(n):
  return [0]*(n+1)

def insert(e, a):
  # inserting element e into min-heap a
  a[0] = a[0] + 1
  a[a[0]] = e
  heap_fix_up(a, a[0])

def heap_fix_up(a, i):
  # fix up from position i to restore
  # min-heap property of heap a
  while i > 1:
    p = i//2
    if a[p] > a[i]:
      a[p], a[i] = a[i], a[p]
      i = p
    else: 
      return
    
def abstract_sort(a):
  n, na = len(a), []
  for _ in range(n):
    smallest = delete_smallest(a)
    na.append(smallest)
  return na

def delete_smallest(a):
  e, a[1], a[0] = a[1], a[a[0]], a[0]-1
  heap_fix_down(a, 1)
  return e

def heap_fix_down(a, i):
  while 2*i <= a[0]:
    c = 2*i
    if c+1 <= a[0]:
      if a[c+1] < a[c]:
        c += 1
    if a[i] > a[c]:
      a[i], a[c] = a[c], a[i]
      i = c
    else:
      return

def heap_sort(x):
  n, a = len(x), new_heap(len(x))
  
  for i in range(n):
    insert(x[i], a)
  
  for i in range (n):
    x[i] = delete_smallest(a)
  return x