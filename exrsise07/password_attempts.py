password = 23456                                     #password with limited attempts
attempts = 5

while attempts > 0:
    user_input = int(input("Enter password: "))

    if user_input == password:
        print("Access granted")
        break
    else:
      attempts -= 1
      print("Wrong password. Attempts left:",attempts)
    if attempts == 0:

        print("Authorities have been alearted")
