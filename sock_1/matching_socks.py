""" 
This code will create a list with random pairs of socks and after a shuffle the system will 
sort them automatically
"""
import random #IMPORT random to generate the random list of socks

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

amount_of_socks =   random.randint(2,len(socks)) #random amount of socks (minimum 2 pairs and a max length of socks)

#for loop to select from random amount of socks random socks
for x in range(amount_of_socks):
    number = random.randint(0,8)
    if socks[number] not in picked:
        picked.append(socks[number])
"""
Randomly shuffle the pairs to have them in disorder
"""
print(picked)
pairs = picked
random.shuffle(picked)
print(pairs)

#switch case to python
def blue():
    blue_list.append("blue")
    if blue_list not in drawer:
        drawer.append(blue_list)
    
def orange():
    orange_list.append("orange")
    if orange_list not in drawer:
        drawer.append(orange_list)
    
def yellow():
    yellow_list.append("yellow")
    if yellow_list not in drawer:
        drawer.append(yellow_list)
    
def red():
    red_list.append("red")
    if red_list not in drawer:
        drawer.append(red_list)
    
def black():
    black_list.append("black")
    if black_list not in drawer:
        drawer.append(black_list)
    
def white():
    white_list.append("white")
    if white_list not in drawer:
        drawer.append(white_list)
    
def striped_blue():
    striped_blue_list.append("striped blue")
    if striped_blue_list not in drawer:
        drawer.append(striped_blue_list)
    
def striped_orange():
    striped_orange_list.append("striped orange")
    if striped_orange_list not in drawer:
        drawer.append(striped_orange_list)
    
def green():
    green_list.append("green")
    if green_list not in drawer:
        drawer.append(green_list)

def sort(sock_list):
    sock_dict = {
        'blue':blue,
        'orange':orange,
        'yellow':yellow,
        'red':red,
        'black':black,
        'white':white,
        'striped_orange':striped_orange,
        'striped_blue':striped_blue,
        'green':green
    }
    function = sock_dict.get(sock_list, lambda:"invalid")
    function()
#run every item in the sort function to match them with their pairs
for x in range(len(picked)):
    sort(picked[x])
    sort(pairs[x])

print(drawer)