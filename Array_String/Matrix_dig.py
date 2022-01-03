class Solution:
    def digMatrix(self,mat):
        list=[]
        col,row=0,0
        result=[]
        N=len(mat)
        M=len(mat[0])
        for i in range(M+N-1):
            x=row
            y=col
            list.clear()
            while(x>=0 and y<M):
                list.append(mat[x][y])
                x-=1
                y+=1
            if row==N-1:
                col+=1
            if row<N-1:
                row+=1
            if i%2==1:
                list.reverse()     
            for j in list:
                result.append(j)        
        return result

St=Solution()
list=[]
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,4,3],[6,5,4],[43,8,9]]
c=[[1,2,3],[4,5,6],[5,8,9]]
d=[[1,42,3],[4,54,65],[73,8,9]]
e=[[1,2,33],[34,45,46],[74,8,9]]
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)
f=open('result.txt','w')
for i in list:

    # print(St.digMatrix(a))
    f.write(str(St.digMatrix(i))+"\n")
f.close()