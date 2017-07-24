arr =[]
class Node:
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None

def printorder(root):
    m = dict()
    #since root's hd is 0
    makehashmap(root, 0, m)

    #'sorted' sorts a dictionary wrt its key values
    #'enumerate' is an iterator
    for i, array in enumerate(sorted(m)):
        for j in array:
            print(j)
        print('\n')

def makehashmap(root, hd, m):
    #base case
    if root is None:
        return 0

    try:
        m[hd].append(root)
    except:
        m[hd] = [root]

    makehashmap(root.left, hd - 1, m)
    makehashmap(root.right, hd + 1, m)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print ("Vertical order traversal is")
printorder(root)
