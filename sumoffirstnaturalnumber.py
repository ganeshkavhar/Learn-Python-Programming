Method 1:

num = int(input("Enter the Number:"))
value = 0
for i in range(1, num+1):
    value = value + i

print("Sum of N natural numbers:", value)


Method 2:

num = int(input("Enter the Number:"))
sum = (num * (num+1))/2
print("The Sum of N natural Number is {}".format(sum))
