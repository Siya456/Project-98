print("Please enter a lower range limit")
lowerRange = int(input())
print("Please enter an upper range limit")
upperRange = int(input())
print("Please enter a number to be divided by")
number = int(input())

for i in range(lowerRange, upperRange+1):
    if i%number == 0:
        print(i)
