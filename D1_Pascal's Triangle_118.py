class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=[]
        for i in range(numRows):
            if i ==0:
                n.append([1])
            elif i==1:
                n.append([1,1])
            else:
                x=[1]
                for j in range(len(n[i-1])-1):
                    x.append(n[i-1][j]+n[i-1][j+1])
                x.append(1)
                n.append(x)
        return n
