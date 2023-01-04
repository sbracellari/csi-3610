a = [10, 8, 1, 3, 0, 9, 4, 7, 6, 2, 5]

def merge(a, b):
    ia, ib, ic = 0, 0, 0
    total = len(a) + len(b)
    c = [0]*total

    while ia < len(a) and ib < len(b):
      if a[ia] <= b[ib]:
        c[ic]=a[ia]
        ia += 1
      else:
        c[ic]=b[ib]
        ib += 1
      ic += 1

    while ia < len(a):
      c[ic]=a[ia]
      ia += 1
      ic += 1

    while ib < len(b):
      c[ic]=b[ib]
      ib += 1
      ic += 1

    return c

def merge_sort(a):
  if len(a) <= 1:
    return a
  else:
    m = len(a)//2
    return merge(merge_sort(a[0:m]), merge_sort(a[m:]))