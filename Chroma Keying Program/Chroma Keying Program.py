
import pygame,sys#imports pygame and sys libraries
#pygame.init()#initiates pygame
pygame.font.init()
def print_instructions():#Defines the print instructions function
    print("1) Make sure the two files (Ghost and background) are in the same folder as this python file")#Prints the instructions
    print("2) Enter the name of the background file (Be sure to include the file extension!!!! (.bmp))")
    print("3) Enter the name of the ghost file (Be sure to include the file extension!!!! (.bmp))")
    print("4) Enter the X and Y value you wish the ghost's center to be(This must be within boundries of the background image!)")
    print("5) Watch spooky ghost appear :)")
def instruction():#Instruction check function
    Instructions = int(input("Do you need instructions?\n1) Yes \n2) No \n(1 or 2): "))#Asks user if they need instructions
    if Instructions == 1:#if yes, call the print instructions function
        print_instructions()
    else:#if no, exit function
        return


Font = pygame.font.SysFont("Times New Roman", 16)#Sets the font for the on screen X,Y coordinates
instruction()#Calls the "Do you need instructions" Function

User_Input_Background = input("Enter the background file name (Include the file extension): ") #Asks the user to input background image file name
User_Input_Ghost = input("Enter the ghost file name (Include the file extension): ")#Ask s the user to input ghost image file name
try:#Tries to load the files that use inputs
    Background = pygame.image.load(User_Input_Background)#Sets the variable Background to the background image
    Ghost = pygame.image.load(User_Input_Ghost)#Sets the variable Ghost to the ghost image

except:#If fails, print instructions and wait then terminate
    print("Cannot find files.\n")
    print_instructions()#Calls the function that prints instructions
    pygame.time.delay(5000)#Delays the Termination so the User can read the instructions
    pygame.quit()  # Ends Pygame
    sys.exit()#Ends Terminal


#Gets the width and height of the background and ghost image
(Background_X, Background_Y) = Background.get_rect().size
(Ghost_X, Ghost_Y) = Ghost.get_rect().size
print("Background Dimensions: ",Background_X,Background_Y,"\nGhost Dimensions: ",Ghost_X,Ghost_Y)#prints the background and ghost image dimensions
Window = pygame.display.set_mode((Background_X,Background_Y))#Sets the pygame window dimensions to the dimensions of the background image
Window.blit(Background,(0,0))#Blits the background image onto the window
pygame.display.update()#Displays the background image

Mouse = int(input("Would you like to use the mouse or the terminal for selecting the center?\n1) Mouse \n2) Terminal \n(1 or 2): "))#Asks the user if they want to use mouse or terminal to enter the coordinates

if Mouse == 1:#If Mouse:
    Mouse_Loop = True#Define mouse loop
    while Mouse_Loop:#Begin mouse loop(so if the user enters invalid coordinates, it will ask them to enter valid ones)
        (User_X, User_Y) = pygame.mouse.get_pos()#Constantly gets the position of the mouse
        Mouse_Location = Font.render("X: {} , Y: {}".format(User_X,User_Y), True, (0, 0, 0),(255,255,255))#Renders the mouse coordinates
        Window.blit(Background,(0,0))#Blits the background onto the window
        Window.blit(Mouse_Location, (User_X, User_Y))#Blits the mouse location onto the window
        pygame.display.update()#Refreshes screen so we can see updates
        for event in pygame.event.get():#Check for an event
            if event.type == pygame.MOUSEBUTTONDOWN:#If mouse click
                (User_X,User_Y) = (pygame.mouse.get_pos())#Gets position again (this line is redundant)
                Top_Left_X = User_X - int(Ghost_X / 2)  # Gets coordinates of top left of ghost x
                Top_Left_Y = User_Y - int(Ghost_Y / 2)  # Gets coordinates of top left of ghost Y
                Bottom_Right_X = User_X + int(Ghost_X / 2)  # Gets coordinates of bottom right of ghost X
                Bottom_Right_Y = User_Y + int(Ghost_Y / 2)  # Gets coordinates of bottom right of ghost Y
                if (User_X >= 0) and (User_Y >= 0) and (User_X <= Background_X) and (
                        User_Y <= Background_Y):  # Checks if the ghost image fits within the background image dimensions
                    Window.blit(Background,(0,0))#Redraws The background
                    Mouse_Loop = False  # if yes, exit the loop
                else:
                    print(
                        "Please enter a X and Y value that fit within the background image")  # if no, loop back to getting x and y coordinates

else:
    while True:#Beginning of loop for the user input X and Y
        #Asks User for X and Y (The center of the ghost)
        print(Background_X,Background_Y)
        User_X = int(input("Enter a X Value: "))#Gets user input for X
        User_Y = int(input("Enter a Y Value: "))#Gets user input for Y
        Top_Left_X = User_X - int(Ghost_X / 2)  # Gets coordinates of top left of ghost x
        Top_Left_Y = User_Y - int(Ghost_Y / 2)  # Gets coordinates of top left of ghost Y
        Bottom_Right_X = User_X + int(Ghost_X / 2)  # Gets coordinates of bottom right of ghost X
        Bottom_Right_Y = User_Y + int(Ghost_Y / 2)  # Gets coordinates of bottom right of ghost Y
        if (User_X >= 0) and (User_Y >= 0) and (User_X <= Background_X) and (
                        User_Y <= Background_Y):  # Checks if the ghost image fits within the background image dimensions
            break  # if yes, exit the loop
        else:
            print(
                "Please enter a X and Y value that fit within the background image")  # if no, loop back to getting x and y coordinates

#Code for chroma-keying(green screen(removing the green and averaging the pixels)
for x in range(0,Ghost_X):# for loop for all x
    for y in range(0,Ghost_Y):#for loop for all y

        if (Top_Left_X+x >= 0) and (Top_Left_Y+y >= 0) and (Top_Left_X+x <= Background_X-1) and (Top_Left_Y+y <= Background_Y-1):
            GhostPixelRGB = Ghost.get_at((x,y))#Gets the RGB value of a pixel on the ghost image at (x,y)
            BackgroundPixelRGB = Background.get_at((Top_Left_X+x,Top_Left_Y+y))#gets the RGB value of a pixel on the background image at (x,y)
            if (GhostPixelRGB[0],GhostPixelRGB[1],GhostPixelRGB[2]) == (0,255,0):#Checks if the pixel is green (0,255,0)
                Ghost.set_at((x,y),(BackgroundPixelRGB[0],BackgroundPixelRGB[1],BackgroundPixelRGB[2]))#If yes, set pixel colour to the corresponding background pixel colour
            else:#If no, set the pixels to the RGB of the ghost pixel plus the RGB of the background pixel and half it for a spooky effect
                R = int((GhostPixelRGB[0]+BackgroundPixelRGB[0])/2)
                G = int((GhostPixelRGB[1]+BackgroundPixelRGB[1])/2)
                B = int((GhostPixelRGB[2]+BackgroundPixelRGB[2])/2)
                Ghost.set_at((x,y),(R,G,B))#Sets ghost pixel to equal combined pixels colour

Window.blit(Ghost,(Top_Left_X,Top_Left_Y))#Blits the new ghost image onto the background image
pygame.display.update()#Updates the pygame window

end = False#Check if user presses quit(X) loop
while not end:#start of loop
    for event in pygame.event.get():#Gets a certain user input
        if event.type == pygame.QUIT:#If user input is quit
            end = True#Exit the loop

pygame.display.quit()#Ends the pygame display
pygame.quit()#Ends pygame
sys.exit()#Ends the terminal
