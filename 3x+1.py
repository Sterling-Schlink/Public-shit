a = int(input("Enter a number: "))
while 1 == 1:
    if a == 1:
        break
    elif (a % 2) == 1:
        a = (a * 3) + 1
    elif (a % 2) == 0:
        a = a / 2
    print(str(a))
print("Fail")
