user_input = input("Insert the temperature: ")
divided_number = float(user_input[0:-1])
divided_scale = user_input.lower()[-1]

if divided_scale == "f":
    print((5 * float(divided_number) -160) / 9 , "C")
elif divided_scale == "c":
    print(((9* float(divided_number) + 32 * 5) /5) , "F")
else:
    print("Error")
