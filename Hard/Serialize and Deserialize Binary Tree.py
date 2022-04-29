# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# DFS
class Codec:
    def serialize(self, root):
        def dfs(root, res):
            if root == None:
                res.append(None)
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
        
        res = []
        dfs(root, res)
        #print(str(res))
        return str(res)

    def deserialize(self, data):
        
        #convert from str to list
        data=data[1:len(data)-1].replace(' ','').split(',')
        data=[item if item!='None' else None for item in data]
        
        #start
        i=0
        def dfs():
            nonlocal i
            if data[i] == None:
                i += 1
                return None
            root = TreeNode(data[i])
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# BFS
class Codec:
    def serialize(self, root):
        if not root:
            return []
        lst, curr_level = [], [root]
        while curr_level:
            next_level, has_value = [], False
            for node in curr_level:
                if node:
                    lst.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                    if node.left or node.right:
                        has_value = True
                else:
                    lst.append(None)
            curr_level = next_level if has_value else []
        return lst

    def deserialize(self, data):
        n = len(data)
        if n == 0:
            return None
        root = TreeNode(data[0])
        curr_level, i = [root], 1
        while curr_level and i < n:
            next_level = []
            for node in curr_level:
                if data[i] != None:
                    node.left = TreeNode(data[i])
                    next_level.append(node.left)
                i += 1
                if data[i] != None:
                    node.right = TreeNode(data[i])
                    next_level.append(node.right)
                i += 1
            curr_level = next_level
        return root
