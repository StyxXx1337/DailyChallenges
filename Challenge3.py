# Given the root to a binary tree, implement 
# serialize(root):
# which serializes the tree into a string, and 
# deserialize(s), 
# which deserializes the string back into the tree.
#
# 2021-07-17

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
    	return "Node Val:{}-Left:{}-Right:{}.".format(self.val, self.left, self.right)


def serialize(root: Node, tree_string="") -> str:
	tree_string = tree_string + f"{root.val}-"

	if root.left == None:
		tree_string = tree_string + 'None-'
	else:
		tree_string = serialize(root.left, tree_string)
	
	if root.right == None:
		tree_string = tree_string + 'None-'
	else:
		tree_string = serialize(root.right, tree_string)

	return tree_string


def deserialize(tree_string: str) -> Node:
	item_list = tree_string.split('-')
	def rec(item_list) -> Node:
		for item in item_list:
			if item == "None":
				return Node(item)

	pass



def traverse(root: Node, result="") -> str:
	
	if root == None:
		return
	result = result + ' ' + str(traverse(root.left))
	result = result + ' ' + str(traverse(root.right))
	
	return result + ' ' + str(root.val)

example1 = Node(4,left=Node(2,left=Node(1, left=Node(0))))
example2 = Node(4,Node(2,Node(1),Node(3)),Node(5,right=Node(6)))
example3 = Node(4,right=Node(5,right=Node(6,right=Node(7))))


print(example1)
print(' ')
print(serialize(example3))
deserialize(serialize(example1))
print(traverse(example1))