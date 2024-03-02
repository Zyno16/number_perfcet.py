a = int(input("enter the first number: "))
sum_of_divisors = 0
for i in range (1,a) :
    if a % i == 0:
        sum_of_divisors += i
    
if sum_of_divisors == a:
    print("the number is perfect")
else:
    print("the number is not")
