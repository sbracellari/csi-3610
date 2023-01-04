class Node: 
  def __init__(self, key): 
    self.value = key 
    self.left = None
    self.right = None

def grandchildren_sum(parent, mp):
  sum = 0
  if parent.left is not None:
    sum += calc_max_sum(parent.left.left, mp) + calc_max_sum(parent.left.right, mp)
  if parent.right is not None:
    sum += calc_max_sum(parent.right.left, mp) + calc_max_sum(parent.right.right, mp)
  return sum

def calc_max_sum(parent, mp):
  if parent is None:
    return 0
  if parent in mp:
    return mp.get(parent)

  grandchildren = parent.value + grandchildren_sum(parent, mp)
  children = calc_max_sum(parent.left, mp) + calc_max_sum(parent.right, mp)
  mp.update({parent: max(grandchildren, children)})

  return mp.get(parent)

def get_max_sum(parent):
  if parent is None:
    return 0
  return calc_max_sum(parent, {})

if __name__ == '__main__':
  # construct a tree
  root = Node(1)
  root.left = Node(3)  
  root.right = Node(10)
  root.left.left = Node(1)
  root.left.right = Node (6)
  root.right.right = Node(14)
  root.left.right.left = Node(4)
  root.left.right.right = Node(7)
  root.right.right.left = Node(13)
  print(get_max_sum(root)) 
  