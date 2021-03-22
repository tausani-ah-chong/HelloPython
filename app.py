def say_hi(name):
    if name == '':
        print("You haven't entered a name, please try again")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)


name = input()

say_hi(name.upper())
