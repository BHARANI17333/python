num=int(input("enter the number:"))
count_even=0
count_odd=0
x=0
while(x<=num):
    if x%2==0:
        count_even+=1
        x+=1
    else :
        count_odd+=1
        x+=1
print("number of odd numbers:",count_odd)
print("number of even numbers:",count_even)

    
