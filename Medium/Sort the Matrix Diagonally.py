class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        height=len(mat)
        width=len(mat[0])
        #print(height,width)
        res=[]
        #res2=[[0]*width]*height
        res2 = [ [0]*width for i in range(height)]
        #print(res2)
        #print(height,width)
        i=height-1
        j=0
        
        count=height*width
        mode=True
        traversed=0
        tmp=[]
        while count>0:
            tmp.append(mat[i][j])
            traversed+=1
            #print(i,j)
            i+=1
            j+=1
            if i==height or j==width:
                for x in sorted(tmp):
                    res.append(x)
                tmp=[]
                if i==j:
                    mode=False
                if mode:
                    #reset
                    i-=traversed
                    j=0
                    #next
                    i-=1
                else:
                    #reset
                    j-=traversed
                    i=0
                    #next
                    j+=1
                traversed=0
            #print(count)
            count-=1
        #print(res)
        #filling elements from res to res2
        mode=True
        i=height-1
        j=0
        count=height*width
        k=0
        #print(len(res))
        #print(res)
        while count>0:
            #print(res2)
            #print("res2["+str(i)+"]["+str(j)+"]="+str(res[k]))
            res2[i][j]=res[k]
            traversed+=1
            i+=1
            j+=1
            if i==height or j==width:
                if i==j:
                    mode=False
                if mode:
                    #reset
                    i-=traversed
                    j=0
                    #next
                    i-=1
                else:
                    #reset
                    j-=traversed
                    i=0
                    #next
                    j+=1
                traversed=0
            #print(count)
            count-=1
            k+=1
        #print("end of while")
        return res2
