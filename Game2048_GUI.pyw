from tkinter import *
from Game2048_logic import *


def draw(game):
    for i in range(game.n):
        for k in range(game.n):
            table[i][k]['text'] = game.field[i][k]
            try:
                table[i][k]['bg'] = colors[game[i][k]]
            except KeyError:
                table[i][k]['bg'] = 'black'
            if game[i][k] == 2 or game[i][k] == 4:
                table[i][k]['fg'] = 'black'
            else:
                table[i][k]['fg'] = 'white'
    scorebar['text'] = game.get_scorebar()


def left(event):
    game.left()
    draw(game)


def right(event):
    game.right()
    draw(game)


def up(event):
    game.up()
    draw(game)


def down(event):
    game.down()
    draw(game)


colors = {'': '#CDC1B4',
          2: '#EEE4DA',
          4: '#EDE0C8',
          8: '#F2B179',
          16: '#F59563',
          32: '#F67C5F',
          64: '#F65E3B',
          128: '#EDCF72',
          256: '#EDCC61',
          512: '#EDCC61',
          1024: '#EDCC61',
          2048: '#EDCC61'}

n = 4
root = Tk()
root['bg'] = '#BBADA0'
game = Game2048(n)
scorebar = Label(root, font='Arial 20')
scorebar.grid(row=0, columnspan=4)
scorebar['text'] = game.get_scorebar()
table = ([[Label(root, height=2, width=4, font='Arial 24') for i in range(game.n)]
          for j in range(game.n)])

for i in range(game.n):
    for k in range(game.n):
        table[i][k].grid(row=i+1, column=k)

for i in range(game.n+1):
        root.grid_rowconfigure(i, pad=10)
        root.grid_columnconfigure(i, pad=10)

draw(game)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)

root.mainloop()
