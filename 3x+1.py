a = int(input("Enter a number: "))
b = 0
c = 0
while 1 == 1:
    if a == 1:
        break
    elif (a % 2) == 1:
        a = (a * 3) + 1
    elif (a % 2) == 0:
        a = a / 2
    b = b + 1
    if a >= c:
        c = a
    print(str(a))
print("Fail")
print(str(b) + " iterations")
print("Highest Number: " + str(c))
