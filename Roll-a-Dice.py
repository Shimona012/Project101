import random
while True:
    print("Welcome to Dice Simulator")
    no=random.randint(1,6)
    if no == 1:
        print(" [-----]")
        print(" [     ]")
        print(" [  0  ]")
        print(" [     ]")
        print(" [-----]")
    elif no == 2:
        print(" [-----]")
        print(" [     ]")
        print(" [ 0 0 ]")
        print(" [     ]")
        print(" [-----]")
    elif no == 3:
        print(" [-----]")
        print(" [     ]")
        print(" [0 0 0]")
        print(" [     ]")
        print(" [-----]")
    elif no == 4:
        print(" [-----]")
        print(" [0   0]")
        print(" [     ]")
        print(" [0   0]")
        print(" [-----]")
    elif no == 5:
        print(" [-----]")
        print(" [0   0]")
        print(" [  0  ]")
        print(" [0   0]")
        print(" [-----]")
    else:
        print(" [-----]")
        print(" [0   0]")
        print(" [0   0]")
        print(" [0   0]")
        print(" [-----]")
        
    response = input("\n","Do you want to quit or Roll-the-Dice again? enter Y to restart or N to end: ")
    if response.upper() == "Y": #go back to the top
        continue    
    print("Bye... Thank you for using our app!")
    break #exit