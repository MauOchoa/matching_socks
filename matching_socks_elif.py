""" 
This code will create a list with random pairs of socks and after a shuffle the system will 
sort them automatically V0.6
"""
import random #IMPORT random to generate the random list of socks
import pygame #IMPORT PYGAME for the grapchical version of the code.
import os     #IMPORT os so we can get the images from other folders
import time   #IMPORT time so the buttons can run only once and not several times
#Initialize pygame
pygame.init()
clock = pygame.time.Clock()
#size of the screen
size = 1200, 650
#colors RGB
color_bred = (255,0,0)
color_bgreen = (0,255,0)
color_green=(0,100,0)
color_red=(100,0,0) 
color_white=(255,255,255)
color_grey=(211,211,211)
#available list of socks 
socks = [
    'blue','orange','yellow',
    'red', 'green', 'striped_orange',
    'white','black','striped_blue',
]
#random picked socks and their pairs the drawer
picked = []
pairs = []
GUI_drawer = []
#list for pairs
GUI_blue_list =[]
GUI_orange_list =[]
GUI_yellow_list = []
GUI_red_list = []
GUI_green_list = []
GUI_striped_orange_list = []
GUI_white_list = []
GUI_black_list = []
GUI_striped_blue_list = []
#for GUI purposes define socks     SOON TO CHANGE FOR PNG FILES WITHOUT BG
icon = pygame.image.load(os.path.join('images/socks.png'))
blue_sock = pygame.image.load(os.path.join('images/blue.png'))
orange_sock = pygame.image.load(os.path.join('images/orange.png'))
yellow_sock = pygame.image.load(os.path.join('images/yellow.png'))
red_sock = pygame.image.load(os.path.join('images/red.png'))
green_sock = pygame.image.load(os.path.join('images/green.png'))
white_sock = pygame.image.load(os.path.join('images/white.png'))
black_sock = pygame.image.load(os.path.join('images/black.png'))
striped_blue_sock = pygame.image.load(os.path.join('images/striped_blue.png'))
striped_orange_sock = pygame.image.load(os.path.join('images/striped_orange.png'))
#Start the screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SOCK SORTING")
pygame.display.set_icon(icon)
amount_of_socks = random.randint(2,len(socks)) #random amount of socks (minimum 2 pairs and a max length of socks)
#Text sizes and fonts
small_text = pygame.font.Font('freesansbold.ttf',20)
large_text = pygame.font.Font('freesansbold.ttf',115)

#switching the switchcase to a one function
def color_sorting(sock,list_ofsock):
    screen.blit(sock, (random.randint(0,800),random.randint(0,462)))
    list_ofsock.append(sock)
    if list_ofsock not in GUI_drawer:
        GUI_drawer.append(list_ofsock)

#generates text for buttons
def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Dictionary to pull socks randomly
def pull(sock_list):
        if sock_list == 'blue':
            color_sorting(blue_sock,GUI_blue_list)
        elif sock_list == 'black':
            color_sorting(black_sock,GUI_black_list)
        elif sock_list == 'white':
            color_sorting(white_sock,GUI_white_list)
        elif sock_list == 'orange':
            color_sorting(orange_sock,GUI_orange_list)
        elif sock_list == 'green':
            color_sorting(green_sock,GUI_green_list)
        elif sock_list == 'red':
            color_sorting(red_sock,GUI_red_list)
        elif sock_list == 'yellow':
            color_sorting(yellow_sock,GUI_yellow_list)
        elif sock_list == 'striped_blue':
            color_sorting(striped_blue_sock,GUI_striped_blue_list)
        elif sock_list == 'striped_orange':
            color_sorting(striped_orange_sock,GUI_striped_orange_list)
        else:
            print("NO SOCK FOUND 404")

#function that sorts the socks and displays them with their pair
#this will change as they only are randomly placed on screen need to come up with a way to get it in order
def sort(x,y):
    for element in range(len(GUI_drawer)):
        x_c=random.randint(0,800)
        y_c=random.randint(0,462)
        screen.blit(GUI_drawer[element][0],(x_c,y_c))
        screen.blit(GUI_drawer[element][1],(x_c+x,y_c+y))

#button function so you can add more buttons
def button(x,y,w,h,ic,ac,msg,status = None):
    mouse = pygame.mouse.get_pos()                      #gets mouse position
    click = pygame.mouse.get_pressed()                  #gets if mouse is clicking
    if ((w+x > mouse[0] >x) and (y+h >mouse[1]>y)):     #if mouse pointer is inside the "button"
        pygame.draw.rect(screen,ac,(x,y,w,h))           #highlight the button to see selection
        if(click[0] == 1 and status != None):           #if left click and is from a button
            if status == "pull":                        #if is the right button
                t0 = time.time()
                for x in range(amount_of_socks):
                    number = random.randint(0,8)
                    if socks[number] not in picked:
                        picked.append(socks[number])
                time.sleep(1)                           #timer to get one click only
                screen.fill(color_grey)
                pygame.display.update()
                pairs = picked
                for element in range(len(picked)):
                    pull(picked[element])
                    pull(pairs[element])
                print(time.time()-t0)
            elif(status == "sort"):
                t0 = time.time()
                time.sleep(1)
                screen.fill(color_grey)
                sort(0,70)
                print(time.time()-t0)
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    textsurf, textrect = text_objects(msg, small_text, color_grey)
    textrect.center= ((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)
    pygame.display.update()
    clock.tick(60)

#Run the introduction of the GUI
def intro():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        #for loop to select from random amount of socks random socks
        screen.fill(color_grey)
        textsurf, textrect = text_objects("Sorting socks", large_text,color_green)
        textrect.center= (460,300)
        screen.blit(textsurf,textrect)
        pygame.display.update()
        clock.tick(60)
        loop()
def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        button(1000,100,100,50,color_green,color_bgreen,"random","pull")
        button(1000,400,100,50,color_red,color_bred,"pair","sort")
        pygame.display.update()
        clock.tick(60)
intro()
loop()    
pygame.quit()
quit()