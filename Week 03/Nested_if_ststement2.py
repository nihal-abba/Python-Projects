MENU = "l) login, q) Quit"
# MENU is in caps and it means it's a CONSTANT
# The CONSTANT is a variable that never changes it's value

print(MENU)
valid_username = "Nihal"
valid_password = "password"

user_choice = input("choose [l/q]: ")

if user_choice == "l":
    print("Logging you in...")
    entered_username = input("Enter your username:")
    entered_password = input("Enter your password:")
    if entered_username == valid_username and entered_password == valid_password:
        print("you have successfully logged in.")

    else:
        print("Invalid credentials")

elif user_choice == "q":
    Print("Quitting the program...")
else:
    print("Invalid choice!")


