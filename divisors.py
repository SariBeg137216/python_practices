user_input = int(input("Enter your number: "))

maghsumelayha = []
for i in range(1, user_input+1):
    if user_input % i == 0:
        maghsumelayha.append(i)

print(maghsumelayha)