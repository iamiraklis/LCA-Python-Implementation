class Node:

    def __init__(self, key):
        self.data = key
        self.pred = self.succ = []

def dagLCA(root,n1,n2):

    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root
    if n1 == n2:
        return n1.data
    lca = []

    for i in range(len(n1.pred)):
        for j in range(len(n2.pred)):
            if(n1.pred[i].data == n2.pred[j].data):
                lca.append(n1.pred[i].data)


    if(lca == []):
        if(n1.data > n2.data):
            lca.append(dagLCA(root,n1.pred[0],n2))
        else:
            lca.append(dagLCA(root,n1,n2.pred[0]))

    return max(lca)


root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)
root.succ = [r2,r3,r4,r5]
r2.succ = [r4]
r2.pred = [root]
r3.succ = [r4, r5]
r3.pred = [root]
r4.succ = [r5]
r4.pred = [r2,r3,root]
r5.pred = [r3,r4,root]
r6.pred = [r4]


#
# def findPath( root, n, path):
#
# 	if root is None:
# 		return False
#
#
# 	path.append(root.data)
#
# 	if root.data == n :
# 		return True
#
# 	if ((root.left != None and findPath(root.left, n, path)) or
# 			(root.right!= None and findPath(root.right, n, path))):
# 		return True
#
# 	path.pop()
# 	return False
#
# def findLCA(root, n1, n2):
#
# 	path1 = []
# 	path2 = []
#
# 	if (not findPath(root, n1, path1) or not findPath(root, n2, path2)):
# 		return -1
#
# 	i = 0
# 	while(i < len(path1) and i < len(path2)):
# 		if path1[i] != path2[i]:
# 			break
# 		i += 1
# 	return path1[i-1]
#
#
# root = Node(10)
# root.left = Node(5)
# root.right = Node(19)
# root.left.left = Node(1)
# root.left.right = Node(6)
# root.right.left = Node(17)
# root.right.right = Node(21)
#
# print ("LCA(1, 6): %d" %findLCA(root, 1, 6))
# print ("LCA(17, 21): %d" %findLCA(root, 17, 21))
# print ("LCA(1, 21): %d" %findLCA(root, 1, 21))
# print ("LCA(4, 19), where 4 is not a node in the tree: %d" %findLCA(root, 4, 19))
#
#
#
# # def findPath( root, n, path):
# #
# # 	if root is None:
# # 		return False
# #
# #
# # 	path.append(root.data)
# #
# # 	if root.data == n :
# # 		return True
# #
# # 	if ((root.left != None and findPath(root.left, n, path)) or
# # 			(root.right!= None and findPath(root.right, n, path))):
# # 		return True
# #
# # 	path.pop()
# # 	return False
# #
# # def findLCA(root, n1, n2):
# #
# # 	path1 = []
# # 	path2 = []
# #
# # 	if (not findPath(root, n1, path1) or not findPath(root, n2, path2)):
# # 		return -1
# #
# # 	i = 0
# # 	while(i < len(path1) and i < len(path2)):
# # 		if path1[i] != path2[i]:
# # 			break
# # 		i += 1
# # 	return path1[i-1]
# #
# #
# # root = Node(10)
# # root.left = Node(5)
# # root.right = Node(19)
# # root.left.left = Node(1)
# # root.left.right = Node(6)
# # root.right.left = Node(17)
# # root.right.right = Node(21)
# #
# # print ("LCA(1, 6): %d" %findLCA(root, 1, 6))
# # print ("LCA(17, 21): %d" %findLCA(root, 17, 21))
# # print ("LCA(1, 21): %d" %findLCA(root, 1, 21))
# # print ("LCA(4, 19), where 4 is not a node in the tree: %d" %findLCA(root, 4, 19))
