class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

		def findPath( root, n, path):

			if (root is None):
				return False


				path.append(root.data)


				if (root.data == n):
					return True


					if ((root.left != None and findPath(root.left, n, path)) or
					(root.right!= None and findPath(root.right, n, path))):
					return True


					path.pop()
					return False


					def findLCA(root, n1, n2):

						path1 = []
						path2 = []

						if (not findPath(root, n1, path1) or not findPath(root, n2, path2)):
							return -1

							i = 0
							while(i < len(path1) and i < len(path2)):
								if path1[i] != path2[i]:
									break
									i += 1
									return path1[i-1]

									root = Node(10)
									root.left = Node(5)
									root.right = Node(19)
									root.left.left = Node(1)
									root.left.right = Node(6)
									root.right.left = Node(17)
									root.right.right = Node(21)

									print ("LCA(1, 6): %d" %findLCA(root, 1, 6,))
									print ("LCA(17, 21): %d" %findLCA(root, 17, 21))
									print ("LCA(1, 21): %d" %findLCA(root, 1, 21))
									print ("LCA(4, 19), where 4 is not a node in the tree: %d" %findLCA(root, 4, 19))
