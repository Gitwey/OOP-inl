class UserInterface(): 

    def __init__(self):
        pass
    
    def page_info(self):
        print("*"*20)
        print("Welcome to my application")
        print("*"*20)
        print("Here you can gather your own collection of animals as well as hunt as your favourite animal")


    def first_menu(self):
        print("*"*20)
        print("Welcome to the Wilderness")
        print("*"*20)
        print("What would you like to do?")
        print("-"*20)
        print("1. Add an animal")
        print("2. Remove an animal")
        print("3. Hunt an animal")
        print("4. Recieve info on an animal")
        print("5. Look at all the animals in the wilderness")
        print("6. Escape the wilderness")

    def error(self):
        print("Encountered error, please retry")
