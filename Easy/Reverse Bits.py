class Solution:
    def reverseBits(self, n: int) -> int:
        m=bin(n)
        m=m[2::][::-1]+('0'*(34-len(m)))
        return int(m,2)
