#first approach tried
n=len(matrix)
setr=set()
setc=set()
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:

            setr.add(i)
            setc.add(j)

for i in range(n):
    for j in range(len(matrix[0])):
        if i in setr or j in setc:
            matrix[i][j]=0
  






#space efficient sol


n=len(matrix[0])
        m=len(matrix)
        col_flg=False
        
        for i in range(m):
            if matrix[i][0]==0:
                col_flg=True
            for j in range(1,n):
                if matrix[i][j]==0:
                    
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]== 0 or matrix[0][j]== 0 :
                    matrix[i][j] = 0
        
        if matrix[0][0]==0:
            for i in range(n):
                matrix[0][i]=0
        if col_flg:
            for j in range(m):
                matrix[j][0]=0
