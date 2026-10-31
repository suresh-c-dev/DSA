#DSA practice
def biggest_in_list(num):
    big =num[0]
    for i in num:
        if i > big:
           big=i
           
    return big
print(biggest_in_list([10,20,30,40]))
print(biggest_in_list([-20,-2,-1,-19]))
print(biggest_in_list([-10,-20,0,-11]))
print(biggest_in_list([0,2,3,1,]))
