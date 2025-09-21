#Word Search Board Generator
from reportlab.pdfgen import canvas
import random
import copy
import string
def check_if_possible(board , word , key , i , j) :
    is_valid = True
    counters = 0
    if key == "up" :
        a = i
        while a >= 0 : 
            if board[a][j] != "0" :
                is_valid = False;
                break;
            a -= 1;
            counters += 1
    elif key == "down" :
        a = i
        while a < len(board) :
            if board[a][j] != "0" :
                is_valid = False;
                break;
            a += 1;
            counters += 1
    elif key == "diagonal-up-right" :
        a = i
        b = j
        while a >= 0 and b < len(board[a]) :
            if board[a][b] != "0" :
                is_valid = False;
                break;
            a -= 1
            b += 1
            counters += 1
    elif key == 'diagonal-up-left' :
        a = i
        b = j
        while a >= 0 and b >= 0 :
            if board[a][b] != "0" :
                is_valid = False;
                break;
            a -= 1
            b -= 1
            counters += 1
    elif key == 'diagonal-down-left' :
        a = i
        b = j
        while a >= 0 and b >= 0 :
            if board[a][b] != "0" :
                is_valid = False;
                break;
            a -= 1
            b -= 1
            counters += 1
    elif key == 'diagonal-down-right' :
        a = i
        b = j
        while a >= 0 and b < len(board[a]) :
            if board[a][b] != '0' :
                is_valid = False;
                break;
            a -= 1;
            b += 1;
            counters += 1
    elif key == "left" :
        b = j
        while b >= 0 :
            if board[i][b] != "0" :
                is_valid = False;
                break;
            b -= 1
            counters += 1
    elif key == "right" :
        b = j
        while b < len(board[i]) :
            if board[i][b] != "0" :
                is_valid = False;
                break;
            b += 1;
            counters += 1;
    return is_valid and counters >= len(word)



done = False
new_board = []
def generate_board(board , words , curr_index) :
        global done
        if done == True :
            return;
        if curr_index == len(words) :
            done = True
            new_board.append(copy.deepcopy(board))
            return;    
        l = ["diagonal-up-right" ,"diagonal-up-left" , "diagonal-down-right" , "diagonal-down-left" ,'up' , 'down' , 'left' , 'right']
        key = random.choice(l)
        for i in range(len(board)) :
            for j in range(len(board[i])) :
                    if key == 'up' : 
                        if check_if_possible(board , words[curr_index] , 'up' , i , j) :
                            ind = 0
                            q = i
                            while q >= 0 : 
                                board[q][j] = words[curr_index][ind]
                                ind += 1
                                q -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words, curr_index + 1)
                            ind = 0
                            q = i
                            while q >= 0 : 
                                board[q][j] = "0"
                                ind += 1
                                q -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                    elif key == 'down' : 
                        if check_if_possible(board , words[curr_index] , 'down' , i , j) :
                            ind = 0
                            q = i
                            while q < len(board) :
                                board[q][j] = words[curr_index][ind]
                                ind += 1
                                q += 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words , curr_index + 1)
                            ind = 0
                            q = i
                            while q < len(board) :
                                board[q][j] = "0"
                                ind += 1
                                q += 1
                                if ind == len(words[curr_index]) :
                                    break;
                    elif key == 'left' : 
                        if check_if_possible(board , words[curr_index] , 'left' , i , j) :
                            ind = 0
                            b = j
                            while b >= 0 :
                                board[i][b] = words[curr_index][ind]
                                ind += 1
                                b -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words ,curr_index + 1)
                            ind = 0
                            b = j
                            while b >= 0 :
                                board[i][b] = "0"
                                ind += 1
                                b -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                    elif key == 'right' : 
                        if check_if_possible(board , words[curr_index] , 'right' , i , j) :
                            ind = 0
                            b = j
                            while b < len(board[i]) :
                                board[i][b] = words[curr_index][ind]
                                ind += 1
                                b += 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words ,curr_index + 1)
                            ind = 0
                            b = j
                            while b < len(board[i]) :
                                board[i][b] = "0"
                                ind += 1
                                b += 1
                                if ind == len(words[curr_index]) :
                                    break;
                    elif key == "diagonal-up-right" :
                        if check_if_possible(board , words[curr_index] , "diagonal-up-right" , i , j) :
                            ind = 0
                            a = i
                            b = j
                            while a >= 0 and b < len(board[a]) :
                                board[a][b] = words[curr_index][ind]
                                ind += 1
                                a -= 1
                                b += 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words , curr_index + 1)
                            ind = 0
                            a = i
                            b = j
                            while a >= 0 and b < len(board[a]) :
                                board[a][b] = "0"
                                ind += 1
                                a -= 1
                                b += 1
                                if ind == len(words[curr_index]) :
                                    break;
                            
                        
                    elif key == "diagonal-up-left" :
                        if check_if_possible(board , words[curr_index] , "diagonal-up-left" , i , j) :
                            ind = 0
                            a = i
                            b = j
                            while a >= 0 and b >= 0 :
                                board[a][b] = words[curr_index][ind]
                                ind += 1
                                a -= 1
                                b -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                            generate_board(board , words , curr_index + 1)
                            ind = 0
                            a = i
                            b = j
                            while a >= 0 and b >= 0 :
                                board[a][b] = "0"
                                ind += 1
                                a -= 1
                                b -= 1
                                if ind == len(words[curr_index]) :
                                    break;
                    elif key == "diagonal-down-right" :
                        if check_if_possible(board , words[curr_index] , "diagonal-down-left" , i , j) :
                            ind = len(words[curr_index]) - 1
                            a = i
                            b = j
                            while a >= 0 and b >= 0 :
                                board[a][b] = words[curr_index][ind]
                                ind -= 1
                                a -= 1
                                b -= 1
                                if ind < 0 :
                                    break;
                            generate_board(board , words , curr_index + 1)
                            ind = len(words[curr_index]) - 1
                            a = i
                            b = j
                            while a >= 0 and b >= 0 :
                                board[a][b] = "0"
                                ind -= 1
                                a -= 1
                                b -= 1
                                if ind < 0 :
                                    break;
                    elif key == "diagonal-down-left" :
                        if check_if_possible(board , words[curr_index] , "diagonal-down-right" , i , j) :
                            ind = len(words[curr_index]) - 1
                            a = i
                            b = j
                            while a >= 0 and b < len(board[a]) :
                                board[a][b] = words[curr_index][ind]
                                ind -= 1
                                a -= 1
                                b += 1
                                if ind < 0 :
                                    break;
                            generate_board(board , words , curr_index + 1)
                            ind = len(words[curr_index]) - 1
                            a = i
                            b = j
                            while a >= 0 and b < len(board[a]) :
                                board[a][b] = "0"
                                ind -= 1
                                a -= 1
                                b += 1
                                if ind < 0 :
                                    break;
                        

width = 16
height = 16
board = [["0" for _ in range(width)] for _ in range(height)]

words = []
counter = 1;
print("~~You May Have A Maximum Of 20 Words~~")
while True : 
    query = input(f"{counter}. Enter your words here (type 'q' to quit): ")
    if len(query) > 8 : 
        print("Word length must be less than or equal to 8.");
        continue;
    elif len(query) > 0 and query != "q" : 
        words.append(query)
    else : 
        counter -= 1;
    if query == 'q' or len(words) == 20 : 
        break;
    counter += 1

generate_board(board , words , 0)
board = new_board[0]

my_canvas = canvas.Canvas("word_search.pdf")
my_canvas.setFont("Times-Bold" , 25)
my_canvas.drawString(225 , 775 , "Word Search")
my_canvas.setFont("Times-Roman" , 12)

def draw_out_board(board) : 
    starting_x = 100
    starting_y = 750
    for row in board : 
        for column in row : 
            my_canvas.line(starting_x , starting_y , starting_x + 25 , starting_y)
            my_canvas.line(starting_x , starting_y , starting_x , starting_y - 25)
            my_canvas.setFont("Times-Bold" , 12)
            if column != "0" : 
                my_canvas.drawString(int((starting_x + starting_x + 25)/2) - 3 , int((starting_y + starting_y - 25) / 2) - 3 , column.upper())
            else : 
                my_canvas.drawString(int((starting_x + starting_x + 25)/2) - 3 , int((starting_y + starting_y - 25) / 2) - 3 , random.choice(string.ascii_lowercase).upper())
            my_canvas.setFont("Times-Roman" , 12)
            starting_x += 25
        starting_y -= 25
        starting_x = 100
    my_canvas.line(starting_x + (25 * len(board[0])) , 750 , starting_x + (25 * len(board[0])) , starting_y)
    my_canvas.line(starting_x , starting_y ,  starting_x + (25 * len(board[0])) , starting_y)
    
    starting_y -= 50
    my_canvas.drawString(starting_x , starting_y , "The Words: ")
    counters = 1
    chill_y = starting_y
    for word in words : 
        starting_y -= 25
        if starting_y < 100 : 
            starting_y = chill_y - 25
            starting_x += 100

        my_canvas.drawString(starting_x , starting_y , f"{counters}. {"".join([char1.upper() for char1 in word])}")
        counters += 1
draw_out_board(board)
my_canvas.save()


