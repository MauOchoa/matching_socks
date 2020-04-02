""" 
This code will create a list with random pairs of socks and after a shuffle the system will 
sort them automatically
"""
import random #IMPORT random to generate the random list of socks
import pygame #IMPORT PYGAME for the grapchical version of the code.
import os
#Initialize pygame
pygame.init()
#size of the screen
size = 1200, 900
#pygame clock
clock = pygame.time.Clock()
#available list of socks 
socks = [
    'blue','orange','yellow',
    'red', 'green', 'striped_orange',
    'white','black','striped_blue',
]
#random picked socks and their pairs the drawer
picked = []
pairs = []
drawer = []
#list for pairs
blue_list =[]
orange_list =[]
yellow_list = []
red_list = []
green_list = []
striped_orange_list = []
white_list = []
black_list = []
striped_blue_list = []
#Start the screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SOCK SORTING")
amount_of_socks =   random.randint(2,len(socks)) #random amount of socks (minimum 2 pairs and a max length of socks)
run = True
#for GUI purposes define socks
blue_sock = pygame.image.load(os.path.join('images/blue.png'))
orange_sock = pygame.image.load(os.path.join('images/orange.png'))
yellow_sock = pygame.image.load(os.path.join('images/yellow.png'))
red_sock = pygame.image.load(os.path.join('images/red.png'))
green_sock = pygame.image.load(os.path.join('images/green.png'))
white_sock = pygame.image.load(os.path.join('images/white.png'))
black_sock = pygame.image.load(os.path.join('images/black.png'))
striped_blue_sock = pygame.image.load(os.path.join('images/striped_blue.png'))
striped_orange_sock = pygame.image.load(os.path.join('images/striped_orange.png'))
#switch case to python
def blue():
    blue_list.append("blue")
    screen.blit(blue_sock, (random.randint(0,800),random.randint(0,600)))
    if blue_list not in drawer:
        drawer.append(blue_list)

def orange():
    orange_list.append("orange")
    screen.blit(orange_sock, (random.randint(0,800),random.randint(0,600)))
    if orange_list not in drawer:
        drawer.append(orange_list)
    
def yellow():
    yellow_list.append("yellow")
    screen.blit(yellow_sock, (random.randint(0,800),random.randint(0,600)))
    if yellow_list not in drawer:
        drawer.append(yellow_list)
    
def red():
    red_list.append("red")
    screen.blit(red_sock, (random.randint(0,800),random.randint(0,600)))
    if red_list not in drawer:
        drawer.append(red_list)
    
def black():
    black_list.append("black")
    screen.blit(black_sock, (random.randint(0,800),random.randint(0,600)))
    if black_list not in drawer:
        drawer.append(black_list)
    
def white_fu():
    white_list.append("white")
    screen.blit(white_sock, (random.randint(0,800),random.randint(0,600)))
    if white_list not in drawer:
        drawer.append(white_list)
    
def striped_blue():
    striped_blue_list.append("striped blue")
    screen.blit(striped_blue_sock, (random.randint(0,800),random.randint(0,600)))
    if striped_blue_list not in drawer:
        drawer.append(striped_blue_list)
    
def striped_orange():
    striped_orange_list.append("striped orange")
    screen.blit(striped_orange_sock, (random.randint(0,800),random.randint(0,600)))
    if striped_orange_list not in drawer:
        drawer.append(striped_orange_list)
    
def green():
    green_list.append("green")
    screen.blit(green_sock, (random.randint(0,800),random.randint(0,600)))
    if green_list not in drawer:
        drawer.append(green_list)

def sort(sock_list):
    sock_dict = {
        'blue':blue,
        'orange':orange,
        'yellow':yellow,
        'red':red,
        'black':black,
        'white':white_fu,
        'striped_orange':striped_orange,
        'striped_blue':striped_blue,
        'green':green
    }
    function = sock_dict.get(sock_list, lambda:"invalid")
    function()

while run:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
    #for loop to select from random amount of socks random socks
    for x in range(amount_of_socks):
        number = random.randint(0,8)
        if socks[number] not in picked:
            picked.append(socks[number])

    #run every item in the sort function to match them with their pairs
    question = input("sort socks?")
    if (question == "yes"):
        
        print(picked)
        pairs = picked
        random.shuffle(picked)
        print(pairs)
        for x in range(len(picked)):
            sort(picked[x])
            sort(pairs[x])
            pygame.display.update()
            clock.tick(60)
        
        print(drawer)
    else:
        run = False

    
pygame.quit()
quit()