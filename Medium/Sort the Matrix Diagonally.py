class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        height=len(mat)
        width=len(mat[0])
        res=[]
        res2=[[0]*width*height]
        #print(res)
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
                res.append(sorted(tmp))
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
        print(res)
        #filling elements from res to res2
        i=height-1
        j=0
        count=height*width
        while count>0:
            
            res2[i][j]=
            traversed+=1
            #print(i,j)
            i+=1
            j+=1
            if i==height or j==width:
                res.append(sorted(tmp))
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
        
    
