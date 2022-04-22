# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
