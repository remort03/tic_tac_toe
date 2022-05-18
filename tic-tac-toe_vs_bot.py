#Imports
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#Variabels
global grid_pos
grid_pos = ['top_left', 'top_cent', 'top_right', 'mid_left', 'mid_cent', 'mid_right', 'bot_left', 'bot_cent', 'bot_right']
global player
player = 1
global player_1
player_1 = []
global player_2
player_2 = []
global game_x
game_x = 450
global game_y
game_y = 450
global winner
winner = ''
global win_conditions
win_conditions = [['top_left', 'top_cent', 'top_right'], ['mid_left', 'mid_cent', 'mid_right'], ['bot_left' ,'bot_cent', 'bot_right'], ['top_left', 'mid_left', 'bot_left'], ['top_cent', 'mid_cent', 'bot_cent'], ['top_right', 'mid_right', 'bot_right'], ['top_left', 'mid_cent', 'bot_right'], ['top_right', 'mid_cent', 'bot_left']]
global used_buttons
used_buttons = []

#Functions
def place(position, button):
    global player
    global grid_pos
    global player_1
    global player_2
    global winner
    global win_conditions
    global used_buttons
    global turn
    used_buttons += [button]
    if(button['bg'] == 'snow'):
        button.configure(bg = 'DodgerBlue2')
        player_1 += [position]
        grid_pos.remove(position)
        for condition in win_conditions:
            if(condition[0] in player_1 and condition[1] in player_1 and condition[2] in player_1):
                winner = 'Player 1'
            else:
                if(len(grid_pos) == 0):
                    winner = 'Tie'
        if(winner == ''):
            turn_changeover()

            #Implementing the bot
            target_spot = ''
            #Takes winning move
            for condition in win_conditions:
                if((condition[0] in player_2 and condition[1] in player_2) or (condition[0] in player_2 and condition[2] in player_2) or (condition[1] in player_2 and condition[2] in player_2)):
                    for spot in condition:
                        if(spot not in player_2 and spot not in player_1):
                            target_spot = spot
                    if(target_spot != ''):
                        break
            #Prevents opponent from winning
            if(target_spot == ''):
                for condition in win_conditions:
                    if((condition[0] in player_1 and condition[1] in player_1) or (condition[0] in player_1 and condition[2] in player_1) or (condition[1] in player_1 and condition[2] in player_1)):
                        for spot in condition:
                            if(spot not in player_1 and spot not in player_2):
                                target_spot = spot
                        if(target_spot != ''):
                            break
            #Takes second piece in winning set
            if(target_spot == ''):
                if('mid_cent' in player_2):
                    if('top_left' not in player_1 and 'bot_right' not in player_1):
                        target_spot = 'top_left'
                    elif('top_right' not in player_1 and 'bot_left' not in player_1):
                        target_spot = 'top_right'
            if(target_spot == ''):
                if('top_left' in player_2):
                    if('top_cent' not in player_1 and 'top_right' not in player_1):
                        target_spot = 'top_right'
                    elif('mid_left' not in player_1 and 'bot_left' not in player_1):
                        target_spot = 'bot_left'
            if(target_spot == ''):
                if('top_right' in player_2):
                    if('top_left' not in player_1 and 'top_cent' not in player_1):
                        target_spot = 'top_left'
                    elif('mid_right' not in player_1 and 'bot_right' not in player_1):
                        target_spot = 'bot_right'
            if(target_spot == ''):
                if('bot_left' in player_2):
                    if('top_left' not in player_1 and 'mid_left' not in player_1):
                        target_spot = 'top_left'
                    elif('bot_right' not in player_1 and 'bot_cent' not in player_1):
                        target_spot = 'bot_right'
            if(target_spot == ''):
                if('bot_right' in player_2):
                    if('bot_left' not in player_1 and 'bot_cent' not in player_1):
                        target_spot = 'bot_left'
                    elif('top_right' not in player_1 and 'mid_right' not in player_1):
                        target_spot = 'top_right'
            if(target_spot == ''):
                if('mid_cent' in player_2):
                    if('top_cent' not in player_1 and 'bot_cent' not in player_1):
                        target_spot = 'top_cent'
                    elif('mid_left' not in player_1 and 'mid_right' not in player_1):
                        target_spot = 'mid_left'
            if(target_spot == ''):
                if('top_cent' in player_2):
                    if('mid_cent' not in player_1 and 'bot_cent' not in player_1):
                        target_spot = 'mid_cent'
                    elif('top_left' not in player_1 and 'top_right' not in player_1):
                        target_spot = 'top_left'
            if(target_spot == ''):
                if('bot_cent' in player_2):
                    if('mid_cent' not in player_1 and 'top_cent' not in player_1):
                        target_spot = 'mid_cent'
                    elif('bot_left' not in player_1 and 'bot_right' not in player_1):
                        target_spot = 'bot_left'
            if(target_spot == ''):
                if('mid_left' in player_2):
                    if('mid_cent' not in player_1 and 'mid_right' not in player_1):
                        target_spot = 'mid_cent'
                    elif('top_left' not in player_1 and 'bot_left' not in player_1):
                        target_spot = 'top_left'
            if(target_spot == ''):
                if('mid_right' in player_2):
                    if('mid_cent' not in player_1 and 'mid_left' not in player_1):
                        target_spot = 'mid_cent'
                    elif('top_right' not in player_1 and 'bot_right' not in player_1):
                        target_spot = 'top_right'
            #Claiming middle
            if(target_spot == ''):
                if('mid_cent' not in player_1 and 'mid_cent' not in player_2):
                    target_spot = 'mid_cent'
            #Claiming a corner
            if(target_spot == ''):
                if('top_left' not in player_1 and 'top_left' not in player_2):
                    target_spot = 'top_left'
            if(target_spot == ''):
                if('top_right' not in player_1 and 'top_right' not in player_2):
                    target_spot = 'top_right'
            if(target_spot == ''):
                if('bot_left' not in player_1 and 'bot_left' not in player_2):
                    target_spot = 'bot_left'
            if(target_spot == ''):
                if('bot_right' not in player_1 and 'bot_right' not in player_2):
                    target_spot = 'bot_right'
            #Taking an edge
            if(target_spot == ''):
                if('top_cent' not in player_1 and 'top_cent' not in player_2):
                    target_spot = 'top_cent'
            if(target_spot == ''):
                if('bot_cent' not in player_1 and 'bot_cent' not in player_2):
                    target_spot = 'bot_cent'
            if(target_spot == ''):
                if('mid_left' not in player_1 and 'mid_left' not in player_2):
                    target_spot = 'mid_left'
            if(target_spot == ''):
                if('mid_right' not in player_1 and 'mid_right' not in player_2):
                    target_spot = 'mid_right'
            #Taking spot
            if(target_spot == 'top_left'):
                top_left_button.configure(bg = 'orange red')
                used_buttons += [top_left_button]
            elif(target_spot == 'top_cent'):
                top_cent_button.configure(bg = 'orange red')
                used_buttons += [top_cent_button]
            elif(target_spot == 'top_right'):
                top_right_button.configure(bg = 'orange red')
                used_buttons +=[top_right_button]
            elif(target_spot == 'mid_left'):
                mid_left_button.configure(bg = 'orange red')
                used_buttons += [mid_left_button]
            elif(target_spot == 'mid_cent'):
                mid_cent_button.configure(bg = 'orange red')
                used_buttons += [mid_cent_button]
            elif(target_spot == 'mid_right'):
                mid_right_button.configure(bg = 'orange red')
                used_buttons += [mid_right_button]
            elif(target_spot == 'bot_left'):
                bot_left_button.configure(bg = 'orange red')
                used_buttons += [bot_left_button]
            elif(target_spot == 'bot_cent'):
                bot_cent_button.configure(bg = 'orange red')
                used_buttons += [bot_cent_button]
            elif(target_spot == 'bot_right'):
                bot_right_button.configure(bg = 'orange red')
                used_buttons += [bot_right_button]
            player_2 += [target_spot]
            grid_pos.remove(target_spot)
            for condition in win_conditions:
                if(condition[0] in player_2 and condition[1] in player_2 and condition[2] in player_2):
                    winner = 'Player 2'
            if(len(grid_pos) == 0):
                winner = 'Tie'
            if(winner == ''):
                turn_changeover()    

        if(winner != ''):
            if(winner != 'Tie'):
                messagebox.showinfo('WINNER', (winner+' has won the game!'))
            else:
                messagebox.showinfo('TIE', 'The game has ended in a Tie!')
            player_1 = []
            player_2 = []
            grid_pos = ['top_left', 'top_cent', 'top_right', 'mid_left', 'mid_cent', 'mid_right', 'bot_left', 'bot_cent', 'bot_right']
            for button in used_buttons:
                button.configure(bg = 'snow')
            winner = ''
            turn.configure(fg = 'DodgerBlue2', text = 'Player 1')
            player = 1



def turn_changeover():
    global player
    if(player == 1):
        turn.configure(fg = 'orange red', text = 'Player 2')
        player = 2
    else:
        turn.configure(fg = 'DodgerBlue2', text = 'Player 1')
        player = 1

#Creating root
root = Tk()
root.title('Tic Tac Toe')
root.geometry('500x500')
root.configure(bg = 'snow')

turn_frame = Frame(root, bg = 'snow')
turn_frame.pack(fill = X)

turn_label = Label(turn_frame, text = 'Player Turn: ', fg = 'gray15', bg = 'snow', font = 'Courier, 20', anchor = W, justify = LEFT)
turn_label.grid(column = 0, row = 0, sticky = N+E+S+W)

global turn
turn = Label(turn_frame, text = 'Player 1', fg = 'DodgerBlue2', bg = 'snow', font = 'Courier, 20', anchor = W, justify = LEFT)
turn.grid(column = 1, row = 0, sticky = N+E+S+W)

#Creating Board
game = Canvas(root, width = game_x, height = game_y, bg = 'snow')
game.pack()

game.create_line((game_x/3), (0+10), (game_x/3), (game_y-10), fill = 'gray15', width = 5)
game.create_line(((game_x/3)*2), (0+10), ((game_x/3)*2), (game_y-10), fill = 'gray15', width = 5)

game.create_line((0+10), (game_y/3), (game_x-10), (game_y/3), fill = 'gray15', width = 5)
game.create_line((0+10), ((game_y/3)*2), (game_x-10), ((game_y/3)*2), fill = 'gray15', width = 5)

top_left_button = Button(root, command = lambda: place('top_left', top_left_button))
top_left_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window((game_x/6), (game_y/6), window = top_left_button)
top_left = [top_left_button, 0]

top_cent_button = Button(root, command = lambda: place('top_cent', top_cent_button))
top_cent_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*3), (game_y/6), window = top_cent_button)
top_cent = [top_cent_button, 0]

top_right_button = Button(root, command = lambda: place('top_right', top_right_button))
top_right_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*5), (game_y/6), window = top_right_button)
top_right = [top_right_button, 0]

mid_left_button = Button(root, command = lambda: place('mid_left', mid_left_button))
mid_left_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window((game_x/6), ((game_y/6)*3), window = mid_left_button)
mid_left = [mid_left_button, 0]

mid_cent_button = Button(root, command = lambda: place('mid_cent', mid_cent_button))
mid_cent_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*3), ((game_y/6)*3), window = mid_cent_button)
mid_cent = [mid_cent_button, 0]

mid_right_button = Button(root, command = lambda: place('mid_right', mid_right_button))
mid_right_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*5), ((game_y/6)*3), window = mid_right_button)
mid_right = [mid_right_button, 0]

bot_left_button = Button(root, command = lambda: place('bot_left', bot_left_button))
bot_left_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window((game_x/6), ((game_y/6)*5), window = bot_left_button)
bot_left = [bot_left_button, 0]

bot_cent_button = Button(root, command = lambda: place('bot_cent', bot_cent_button))
bot_cent_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*3), ((game_y/6)*5), window = bot_cent_button)
bot_cent = [bot_cent_button, 0]

bot_right_button = Button(root, command = lambda: place('bot_right', bot_right_button))
bot_right_button.configure(width = 17, height = 8, bg = 'snow', relief = FLAT)
game.create_window(((game_x/6)*5), ((game_y/6)*5), window = bot_right_button)
bot_right = [bot_right_button, 0]

#Mainloop
root.mainloop()