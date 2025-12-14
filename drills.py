
# def prime(n):
#     check = ""
#     for i in range(2,n):
#         if n % i == 0:
#             check = "Not Prime"
#             break
#     else:
#         check = "Prime"
#     return check

# n = int(input("Enter a number: ")) 
# print(prime(n))


game_on = True
while game_on:
    exit = input("Do you want to exit? (yes/no): ")
    if exit == "yes":
        game_on = False
        print("Goodbye!")
    elif exit == "no":
        print("Looping...")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")