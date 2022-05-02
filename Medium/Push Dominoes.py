class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        while True:
            old=dominoes
            
            dominoes=dominoes.replace('R.L','RXL').replace('.L','LL').replace('R.','RR')
            
            if dominoes==old:
                break
            
        return dominoes.replace('X','.')
