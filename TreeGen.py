import math
from tkinter import *
from random import *


def circle(centerx, centery, radius, color):
    shift = max(abs(radius),3)/2
    startx = centerx - shift
    starty = centery - shift
    endx = centerx + shift
    endy = centery + shift
    canvas.create_oval(startx, starty, endx, endy, fill=color, width=0)


def radian(angle):
    return (angle - 90) * math.pi / 180


def rgb(r,g,b):
    r = math.floor(min(max(r,0),255))
    g = math.floor(min(max(g,0),255))
    b = math.floor(min(max(b,0),255))
    return f'#{r:02x}{g:02x}{b:02x}'


def calc_from_parent(genome_size,parent_size,percent_size):
    return (parent_size-genome_size)*percent_size + genome_size


def branch(genome_line, parent_info):
    nextx = parent_info['endx']
    nexty = parent_info['endy']

    genome_size = genome_line['size']
    parent_size = parent_info['last size']
    percent_size = genome_line['size from parent']
    radius = calc_from_parent(genome_size,parent_size,percent_size)

    percent_color = genome_line['color from parent']
    red = calc_from_parent(genome_line['red'],parent_info['last red'],percent_color)
    green = calc_from_parent(genome_line['green'],parent_info['last green'],percent_color)
    blue = calc_from_parent(genome_line['blue'],parent_info['last blue'],percent_color)

    red += uniform(-genome_line['color deviation'], genome_line['color deviation'])
    green += uniform(-genome_line['color deviation'], genome_line['color deviation'])
    blue += uniform(-genome_line['color deviation'], genome_line['color deviation'])

    angle = parent_info['angle']+uniform(-genome_line['random angle'],genome_line['random angle'])
    length = genome_line['length'] + randint(-genome_line['random length'],genome_line['random length'])

    for step in range(length):
        nextx += math.cos(radian(angle))
        nexty += math.sin(radian(angle))
        angle += uniform(-genome_line['random turn'],genome_line['random turn'])

        radius += genome_line['size shift']

        red += genome_line['red shift']
        green += genome_line['green shift']
        blue += genome_line['blue shift']
        color = rgb(red, green, blue)
        circle(nextx, nexty, radius, color)

    save = {
        'endx': nextx,
        'endy': nexty,
        'angle': angle,
        'last size': radius,
        'last red': red,
        'last green': green,
        'last blue': blue,
    }
    return save


def tree(genome, parent_genome, depth = 0):
    if depth == len(genome): return
    save = branch(genome[depth], parent_genome)

    branch_amount = genome[depth]['branch amount']
    max_angle = genome[depth]['max branch angle']
    saved_angle = save['angle']
    for index in range(branch_amount):
        norm_angle = 0
        if branch_amount != 1:
            norm_angle = -1+(2/(branch_amount-1))*index
        save['angle'] = saved_angle+(norm_angle*max_angle)
        save['angle diff'] = norm_angle*max_angle
        tree(genome, save, depth+1)


genome = [
    # 1 глубина
    {
        'length': 100,
        'size': randint(15,25),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0,255),
        'green': randint(0,255),
        'blue': randint(0,255),
        'red shift': uniform(-3,3),
        'green shift': uniform(-3,3),
        'blue shift': uniform(-3,3),
        'branch amount': randint(1,4),
        'max branch angle': randint(10,60),
        'size from parent': random(),
        'color from parent': random(),
        'color deviation': randint(5,40),
        'turn': uniform(-1,1),
        'random turn': uniform(0,5),
        'random length': randint(0,30),
        'random angle': uniform(0,20),
    },
    {
        'length': 100,
        'size': randint(15,25),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0,255),
        'green': randint(0,255),
        'blue': randint(0,255),
        'red shift': uniform(-3,3),
        'green shift': uniform(-3,3),
        'blue shift': uniform(-3,3),
        'branch amount': randint(1,4),
        'max branch angle': randint(10,60),
        'size from parent': random(),
        'color from parent': random(),
        'color deviation': randint(5,40),
        'turn': uniform(-1,1),
        'random turn': uniform(0,5),
        'random length': randint(0,30),
        'random angle': uniform(0,20),
    },
    {
        'length': 100,
        'size': randint(15,25),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0,255),
        'green': randint(0,255),
        'blue': randint(0,255),
        'red shift': uniform(-3,3),
        'green shift': uniform(-3,3),
        'blue shift': uniform(-3,3),
        'branch amount': randint(1,4),
        'max branch angle': randint(10,60),
        'size from parent': random(),
        'color from parent': random(),
        'color deviation': randint(5,40),
        'turn': uniform(-1,1),
        'random turn': uniform(0,5),
        'random length': randint(0,30),
        'random angle': uniform(0,20),
    },
    {
        'length': 100,
        'size': randint(15,25),
        'size shift': uniform(-0.3, 0.3),
        'red': randint(0,255),
        'green': randint(0,255),
        'blue': randint(0,255),
        'red shift': uniform(-3,3),
        'green shift': uniform(-3,3),
        'blue shift': uniform(-3,3),
        'branch amount': randint(1,4),
        'max branch angle': randint(10,60),
        'size from parent': random(),
        'color from parent': random(),
        'color deviation': randint(5,40),
        'turn': uniform(-1,1),
        'random turn': uniform(0,5),
        'random length': randint(0,30),
        'random angle': uniform(0,20),
    }

]


window = Tk()
window.geometry("500x500")
window.title("genome tree generation")

canvas = Canvas(window, width=500, height=500, bg='#012')
canvas.pack()

# tree(250, 490, 0, genome)

start_parent = {
    'endx': 250,
    'endy': 450,
    'angle': 0,
    'last size': 0,
    'last red': 0,
    'last green': 0,
    'last blue': 0,
    'angle diff': 0,
}

tree(genome, start_parent)

window.mainloop()




# def branch(startx, starty, angle, length):
#     nextx = startx
#     nexty = starty
#     for step in range(length):
#         nextx += math.cos(radian(angle))
#         nexty += math.sin(radian(angle))
#         circle(nextx, nexty, 10)
#
#     save = {
#         'endx': nextx,
#         'endy': nexty,
#         'angle': angle,
#     }
#     return save


# def branch(startx, starty, angle, genome_line):
#     nextx = startx
#     nexty = starty
#
#     radius = genome_line['size']
#
#     red = genome_line['red']
#     green = genome_line['green']
#     blue = genome_line['blue']
#
#     for step in range(genome_line['length']):
#         nextx += math.cos(radian(angle))
#         nexty += math.sin(radian(angle))
#         radius += genome_line['size shift']
#         red += genome_line['red shift']
#         green += genome_line['green shift']
#         blue += genome_line['blue shift']
#         color = rgb(red, green, blue)
#         circle(nextx, nexty, radius, color)
#
#     save = {
#         'endx': nextx,
#         'endy': nexty,
#         'angle': angle,
#     }
#     return save


# def tree(startx, starty, angle, length, depth):
#     if depth == 0: return
#     save = branch(startx, starty, angle, length)
#     endx = save['endx']
#     endy = save['endy']
#     angle = save['angle']
#     tree(endx, endy, angle-30, length-14, depth-1)
#     tree(endx, endy, angle+30, length-14, depth-1)

# genome = [
#     { 'length': 100 }, # 1 уровень
#     { 'length': 70 },  # 2 уровень
#     { 'length': 50 },  # 3 уровень
#     { 'length': 40 },  # 4 уровень
#     { 'length': 35 },  # 5 уровень
#     { 'length': 30 },  # 6 уровень
# ]
#

# genome = [
#     { 'length': 100, 'size': randint(15,25) },  # 1 уровень
#     { 'length': 70,  'size': randint(12,22) },  # 2 уровень
#     { 'length': 50,  'size': randint(10,20) },  # 3 уровень
#     { 'length': 40,  'size': randint(8,18) },   # 4 уровень
#     { 'length': 35,  'size': randint(7,16) },   # 5 уровень
#     { 'length': 30,  'size': randint(6,14) },   # 6 уровень
# ]



# def tree(startx, starty, angle, genome, depth = 0):
#     if depth == len(genome): return
#     save = branch(startx, starty, angle, genome[depth])
#     endx = save['endx']
#     endy = save['endy']
#     angle = save['angle']
#
#     branch_amount = genome[depth]['branch amount']
#     # print("branch amount", branch_amount)
#     for index in range(branch_amount):
#         norm_angle = 0
#         if branch_amount != 1:
#             norm_angle = -1+(2/(branch_amount-1))*index
#             # print("index", index)
#             # print("branch amount loop", branch_amount)
#             # print("normal angle", norm_angle)
#         tree(endx, endy, angle+(norm_angle*30), genome, depth+1)


