class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # arr = []
    # cb = lambda x: arr.append(x)
    # callback appends x into array
    # start at root node
    cb(self.value)
    # print(self.value)
    #traverse as far as possible along each branch
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    if self.right is not None:
      self.right.depth_first_for_each(cb)
    return

  def breadth_first_for_each(self, cb):
    #initialize queue
    queue = [self]
    # create for loop and check if nodes exist left and/or right, if it does then append to queue
    for node in queue:
      cb(node.value)
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
