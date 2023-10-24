import random

def openGame(userName): #function để load game
    with open("savegame.txt", "a") as f:
        pass
    with open("savegame.txt", "r") as f:
        createdNames = f.read()
    if f'{userName}:' in createdNames:
        i = createdNames.index(f'{userName}:')
        j = createdNames[i:].find(":")
        currentAmount = float(createdNames[i + j + 2 : i + j + 7])
        print(f"Hello {userName}; Your current amount is: {currentAmount}$")
        clear_junks()
        return currentAmount
    else:
        with open("savegame.txt", "a") as f:
            f.write(f"\n{userName}: 10         ")
            print("Your username has been created successfully. You will start with 10$")
            clear_junks()
            return 10

def clear_junks():
#do save game hay cash out là write toàn bộ lại, chỉ xóa tên mà không xóa số nên dọn rác cho gọn file save
    with open("savegame.txt", "r") as f:
        lines = f.readlines()
    with open("savegame.txt", "w") as f:
        pass    
    with open("savegame.txt", "a") as f:    
        for line in lines:
            if line[0].isdigit() or line[0].isspace():
                pass
            else:
                f.write(line)

def saveGame(): 
    print(f"You will save the game at {currentAmount}$")
    with open("savegame.txt", "r") as f:
        text = f.read()
        text = text.replace(f"{userName}: ", "")
    with open("savegame.txt", "w") as f:
        f.write(text) 
    with open("savegame.txt", "a") as f:
        f.write(f"\n{userName}: {currentAmount}         ")
    print("Successfully saved. Good bye!!")
    clear_junks()
    exit()

def cashOut():
    with open("savegame.txt", "r") as f:
        text = f.read()
        text = text.replace(f"{userName}: ", "")
    with open("savegame.txt", "w") as f:
        f.write(text)
    with open("savegame.txt", "a") as f:
        f.write(f"\n{userName}: 0         ")
    print(f"Successful withdrawal. You will receive {currentAmount}$.\nThank you for playing my game.")
    clear_junks()
    exit()

def first_menu():
    print(f"""     _______________________________ 
    |                               |
    |Press 0: Play the slot machine |
    |Press any key to Exit          |
    |_______________________________|""")

    userChoice = input("Enter your choice: ")
    if userChoice == '0':
        return
    else:
        exit()

def menu():
    print(f"""     _______________________________
    |                              |    
    |Press 1: Play the slot machine|
    |Press 2: Save game            |
    |Press 3: Cash out             |
    |______________________________|""")
    
    userChoice = input("Enter your choice: ")
    i = userChoice
    if i == '1':
        return
    elif i == '2':
        saveGame()
    elif i == '3':
        cashOut()
    else:
        print("Error!! Try again")
        menu()

print("""################################## SLOT MACHINE GAME ##################################\n""")

while True:
    userName = input("Enter your username (alphabets first): ")
    userName = userName.lower()
    if userName[0].isalpha():
        break
    else:
        print("Invalid username. Please try again!\n")

first_menu()

currentAmount = openGame(userName)
list = list(range(10))
while True:
    if currentAmount == 0:
        print("You've ran out of money. Good bye!!!")
        break
    menu()
    currentAmount -= 0.25
    a = random.choice(list)
    b = random.choice(list)
    c = random.choice(list)
    print(f"\nYour number is: {a}{b}{c}")
    if a == b == c:
        currentAmount += 10
        print("You've received 10$!!!")
    elif a == b or a == c or b == c:
        currentAmount += 0.5
        print("You've received 0.5$!!")
    else:
        print("Nothing happen!")
    print(f"\nYour current amount is: {currentAmount}$")

