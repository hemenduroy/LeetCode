class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        while True:
            old=dominoes
            
            dominoes=dominoes.replace('R.L','RXL')
            dominoes=dominoes.replace('.L','LL')
            dominoes=dominoes.replace('R.','RR')
            
            if dominoes==old:
                break
            
        return dominoes.replace('X','.')
