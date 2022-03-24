class Solution(object):
    def generateParenthesis(self, n):
        
        def paren(left, right, curr, res):
            # 'evaluate current string
            # if we are out of brackets to add, we must be at a valid string
            if left == 0 and right == 0:
                #print("appending ",end="")
                #print(curr)
                res.append(curr)
                return
            
            # recursive call: add either open or close
            # if adding open bracket is valid
            if left > 0:
                # add open bracket, decr count
                #print(left-1,end="")
                #print(" | ",end="")
                #print(right,end="")
                #print(" | ",end="")
                #print(curr+"(",end="")
                #print((10-len(curr))*" "+" | ",end="")
                #print(res)
                paren(left-1, right, curr + "(", res)
                
            # if adding close bracket is valid
            if right > left:
                # add close bracket, decr count
                #print(left,end="")
                #print(" | ",end="")
                #print(right-1,end="")
                #print(" | ",end="")
                #print(curr+")",end="")
                #print((10-len(curr))*" "+" | ",end="")
                #print(res)
                paren(left, right-1, curr + ")", res)
            
            ##print(res)
            #print("returning...")
            return res
        # end paren()
        #print(n,end="")
        #print(" | ",end="")
        #print(n,end="")
        #print(" | ",end="")
        #print("''",end="")
        #print(" | ",end="")
        #print([])
        res = paren(n, n, '', [])
        #print("\n\n")
        return res

'''
Output

roy@ubuntu:~$ python3 test.py 



3 | 3 | '' | []
2 | 3 | (           | []
1 | 3 | ((          | []
0 | 3 | (((         | []
0 | 2 | ((()        | []
0 | 1 | ((())       | []
0 | 0 | ((()))      | []
appending ((()))
returning...
returning...
returning...
1 | 2 | (()         | ['((()))']
0 | 2 | (()(        | ['((()))']
0 | 1 | (()()       | ['((()))']
0 | 0 | (()())      | ['((()))']
appending (()())
returning...
returning...
1 | 1 | (())        | ['((()))', '(()())']
0 | 1 | (())(       | ['((()))', '(()())']
0 | 0 | (())()      | ['((()))', '(()())']
appending (())()
returning...
returning...
returning...
returning...
2 | 2 | ()          | ['((()))', '(()())', '(())()']
1 | 2 | ()(         | ['((()))', '(()())', '(())()']
0 | 2 | ()((        | ['((()))', '(()())', '(())()']
0 | 1 | ()(()       | ['((()))', '(()())', '(())()']
0 | 0 | ()(())      | ['((()))', '(()())', '(())()']
appending ()(())
returning...
returning...
1 | 1 | ()()        | ['((()))', '(()())', '(())()', '()(())']
0 | 1 | ()()(       | ['((()))', '(()())', '(())()', '()(())']
0 | 0 | ()()()      | ['((()))', '(()())', '(())()', '()(())']
appending ()()()
returning...
returning...
returning...
returning...
returning...
returning...



['((()))', '(()())', '(())()', '()(())', '()()()']

If we just need the count

class Solution(object):
    def generateParenthesis(self, n):
        count=0
        def paren(left, right):
            nonlocal count
            
            if left == 0 and right == 0:
                count+=1
                return
            
            if left > 0:
                paren(left-1, right)
                
            if right > left:
                paren(left, right-1)
            
            return count
        
        res = paren(n, n)
        return res
'''
