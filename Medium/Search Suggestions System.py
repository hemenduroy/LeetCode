class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        for i in range(len(searchWord)):
            curr=[]
            for j in products:
                if j.startswith(searchWord[:i+1]):
                    curr.append(j)
                if len(curr)==3:
                    break
            res.append(curr)
        return res
