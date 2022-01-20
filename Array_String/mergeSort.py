import random as rand
class merge_sort:
    def __init__(self):
        pass
    def input_size(self):
        while True :
            try:
                size_list = int(input("input size of list: "))
                return size_list
            except :
                print("size_list must be integer!!")
    def create_list(self,size_list):
        result = []
        for i in range (0,size_list-1):
            result.append(rand.randint(1,size_list))
        return result
    def do_merge(self,a1,a2):
        i1 , i2 =0 ,0
        result = []
        while i1 < len(a1) or i2 <len(a2):
            if i1 < len(a1) and i2 <len(a2):
                if a1[i1] < a2[i2]:
                    result.append(a1[i1])
                    i1+=1
                else : 
                    result.append(a2[i2])
                    i2+=1
            else:
                if i1 == len(a1) :
                    result.append(a2[i2])
                    i2+=1
                elif i2 == len(a2):
                    result.append(a1[i1])
                    i1+=1
        return result
    def merge_sort(self,a,l,r):
        if l > r:
            return []
        if l == r :
            single = []
            single.append(a[l])
            return single
        # mid point
        mid = (l+r)//2
            # divide half array 
        left = self.merge_sort(a,l,mid)
        right = self.merge_sort(a,mid+1,r)
            # merge two list
        result = self.do_merge(left,right)
        return result

def main():
    mr = merge_sort()
    f = open("test.txt","r")
    for i in f.readlines():
            size_list = int(i.strip()) 
            result = mr.create_list(size_list)
            print("before sort : ")
            print(result)
            print("after sort : ")
            print(mr.merge_sort(result,0,len(result)-1))
        
    f.close()
main()

