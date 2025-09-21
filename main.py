#Word Search Board Generator
from reportlab.pdfgen import canvas
import random
import copy
import string
def check_if_possible(board , word , key , i , j) :
    
    '''
    This function will check if it is possible to place a word based off of the starting position of the word (i , j), and the direction of
    the word (key).
    If the word neatly fits in the board without overlapping any other placed words or going off of the edge of the board, then the function 
    will return True. However, if the word overlaps with any other already placed words, or if the word is too long to fit in a specific
    position, then, the function will return False.
    Empty cells are "0", in the board.
    '''
    
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
    
        '''
        This function randomly chooses a 'key' in the list 'l', to determine which direction the current word should be placed as. Then,
        it will loop through the length of the board, and, the width of the board (i , j) to determine which starting points are valid for
        placing the word. It checks this using the check_if_possible() function.
        If it finds a valid starting_point, it recurses to the next word. The function keeps recursing until all the words have been validly
        placed.

        Once the function successfully places all of the words, the done variable will be equivalent to True, and, all other recursion
        stacks that were currently running will stop. It will append the valid board to the 'new_board' variable, and then the program will
        use reportlab to output a pdf using the 'new_board' variable.
        '''
    
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

#Each empty cell is "0". If the empty cell is not "0", then, that means that the cell is storing a letter for a word.
board = [["0" for _ in range(width)] for _ in range(height)]

#This is where we take in user input using the command line for the 'words' list. You MUST have less than or equal to 20 words, and, the
#words must not have a greater length than 8.
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
    
    '''
    This function is used for carving out a board in a pdf using reportlab.
    It uses the starting points 'startnig_x' and 'starting_y' as the starting points to place the FIRST cell in our board. Then, for each
    cell, it draw out a frame around the cell. If the cell is NOT empty (if it does NOT equal "0"), then, it writes whatever letter is in
    in the cell into the pdf. Howevery, if the cell IS empty (if it DOES equal "0"), then, it randomly chooses a letter to write out inside
    of the cell.
    25 pixels will be added 'starting_x' to move 25 pixels to the right, for the new cell.
    Once a row in the board has all been draw out, 25 pixels will be subtracting from 'starting_y' to move down 25 pixels. 'starting_x' will
    also be restarting to 100, to place the first cell in the new row.

    Once finished setting up the board, the function then moves on to writing all of the words in the 'words' list for the player to find.
    It uses a 'counters' variable to keep track of each word in the list. It moves down the 'starting_y' variable for each word by 25 pixels,
    and, when the 'starting_y' variable gets too low (it starts getting out of the pdf file), it gets restarted back up to the next column,
    and we move the 'starting_x' variable to the right by 25 pixels.
    '''
    
    #This is where we carve out the board in the pdf file.
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

    #This is where we write all of the words.
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


