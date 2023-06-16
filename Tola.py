import random
grams = [1,5,12,58,82,117,223]
boxes = ["Box 1","Box 2","Box 3","Box 4","Box 5","Box 6","Box 7"]
random.shuffle(grams)
counter=0

while True:
    boxes[counter] = grams[counter]
    counter+=1
    if counter==7:
        counter=0
        break

print("JEETOOOOOOOOOO PAKISTANNNNNNNNNN")
print("THE GOLD GAME")
name= (input("Enter your name to proceed :"))
print("Welcome {0}! Let's begin the game...".format(name))

print('''Hi {0} let's tell you how this game works. Firstly you have to select any 1 box from the 7 boxes u will ne offered once selected
       the game will get started then there will be 6 other boxes exculding ur box u have to choose one box at a time and open it 
      you can only exchnage the box once after the game is started and the last box which will be left in the end will be your's
      GOODLUCK!'''.format(name))

def gameLoop():
    print('''Select any one box from the following
        1. Box 1
        2. Box 2
        3. Box 3
        4. Box 4
        5. Box 5
        6. Box 6
        7. Box 7''')
    box = int(input("Enter the box number you choose : "))
    userint = box - 1
    if boxes[userint] == 0:
        print("box already opened select another one")
        gameLoop()
    else:
        print("you just loss: ")
        print(boxes[userint])
        boxes[userint] = 0;


while True:
    gameLoop()
    counter += 1
    if counter==6:
        numbs = 0
        while True:
            if boxes[numbs] != 0:
                print("congratulations you have won : ")
                print(boxes[numbs])
                break
            else:
                numbs +=1
        break


