my_list = [1,23,3,4,5,6]

ele = int(input())

flag = False

for i in my_list:
    if(i  == ele):
        flag = True
        break

if(flag == True):
    print("Element found")
    else: 
        print("Element not found")
