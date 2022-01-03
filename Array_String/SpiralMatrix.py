class coordinates :
    def __init__(self,cor_x,cor_y):
        self.cor_x=cor_x
        self.cor_y=cor_y
class Solution:
    def SpiralMatrix(self,mat):
        row= len(mat)
        col=len(mat[0])
        row_top=0
        col_right=col-1
        row_bottom=row-1
        col_left=0
        start_row=row_top
        start_col=col_right
        result=[]
        contain=[]
        coordinate=[]
        index=0
        number_of_element=col*row
        while(True):
            contain.clear()
            if index%2==0:
                y=0
                while y<col:
                    if len(coordinate)==0:
                        couple=coordinates(start_row,y)
                        coordinate.append(couple)
                        contain.append(mat[start_row][y])
                    else:
                        check=False              
                        for couple_cor in coordinate:
                            if couple_cor.cor_x==start_row and couple_cor.cor_y==y:
                                check=True
                                break
                        if check==False:
                            couple=coordinates(start_row,y)
                            coordinate.append(couple)
                            contain.append(mat[start_row][y])
                                
                    y+=1
                if index%4==0:
                    start_row=row_bottom
                    row_top+=1
                    for con in contain:
                        result.append(con)
                elif index%4==2:
                    start_row=row_top
                    row_bottom-=1
                    contain.reverse()
                    for con in contain:
                        result.append(con)
            else:
                x=0
                while x<row:
                    check=False
                    for couple_cor in coordinate:
                            if couple_cor.cor_x==x and couple_cor.cor_y==start_col:
                                check=True
                                break 
                    if check==False:
                        couple=coordinates(x,start_col)
                        coordinate.append(couple)
                        contain.append(mat[x][start_col])
                    x+=1
                if index%4==1:
                    start_col=col_left
                    col_right-=1
                    for con in contain:
                        result.append(con)
                elif index%4==3:
                    start_col=col_right
                    col_left+=1
                    contain.reverse()
                    for con in contain:
                        result.append(con)   
            index+=1
            if len(result)==number_of_element:
                break
        return result
                 

St=Solution()
a=[[1,2,3],[4,5,6],[7,8,9]]
print(St.SpiralMatrix(a))

                


                

