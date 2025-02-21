print("Tenshinhan is trying to find Gohan to save him from Majin Buu, but Tenshinhan is not able to find him.")
print("Fortunally, you know where Gohan is, can you tell him the right place to go?.")
mapa: [[str]] = [[0 for x in range(3)] for x in range(3)]
mapa[0][0] = "Only Sand..."
mapa[0][1] = "Someone has beeing here..."
mapa[0][2] = "Only Sand..."
mapa[1][0] = "We are very close..."
mapa[1][1] = "Gohan is here!"
mapa[1][2] = "We are very close..."
mapa[2][0] = "Only Sand..."
mapa[2][1] = "Someone has beeing here..."
mapa[2][2] = "Only Sand..."

print("You have 3 attempts to save Gohan, where do you think he is?")
print("The map is a 3x3 matrix, where each position has a clue to where Gohan is.")
for i in range(3):
    print("Attempt", i + 1)
    x = int(input("Enter the row: "))
    y = int(input("Enter the column: "))
    if mapa[x][y] == "Gohan is here!":
        print("Congratulations! You helped Tenshinhan to find Gohan!")
        break
    elif i == 2:
        print("You failed to save Gohan, looks like that we will need the dragon balls to revive him.")
    else:
        print(f"{mapa[x][y]}")
        print("Sorry, Gohan is not here.")
