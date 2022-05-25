class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        S = set(words)
        ans = []
        for word in words:
            if not word:
                continue
            stack = [0]
            seen = set()
            seen.add(0)
            M = len(word)
            while stack:
                left = stack.pop()
                if left == M:
                    ans.append(word)
                    break
                for right in range(1, M + 1): # rightust start from 1
                    if word[left:right] in S and right not in seen and not (left==0 and right==M): 
                # that is, the word must be broken but not a complete one
                        stack.append(right)
                        seen.add(right)
        return ans
