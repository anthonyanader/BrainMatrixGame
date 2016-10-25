import random

def create_board(size):
    '''int->(list of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    
    if size % 2 == 0 and size > 1 and size < 53:
        board = [None]*size

        letter='A'
        
        for i in range(len(board)//2):
            board[i]=letter
            board[i+len(board)//2 ]=board[i]
            letter=chr(ord(letter)+1)
        random.shuffle(board)
        return board
    else:
        print("That was not an even number between 2 and 52.")

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
   
    for i in range(len(a)):
        if a[i] == True:
            print('{0:4}'.format(board[i]), end=' ')
        else:
            print('{0:4}'.format('*'), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''(None)->None

       Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass

def check_win(a, guess_count, max_guess):
    '''(list of str), int, int -> bool
    '''
    if False not in a:
        print()
        print("Congratulations! You completed the game with "+str(guess_count)+" guesses.")
        print("That is "+str(guess_count - max_guess)+" more than the best possible.")
        replay()
        return False
    else:
        return True
    
def replay():
    '''str -> None

       Function that asks the user if they wish to restart the game with the same
       board size
    '''
    print()
    print('Would you like to replay this game with same board size?')
    replay = input('Yes or no? ')

    replay = replay.strip().lower()

    if replay == 'yes':
        clear_screen()
        play_game(board)
    elif replay == 'no':
        exit()
        
def clear_screen():
    '''None -> None

       Function that clears the screen.
    '''   
    for i in range(50):
        print()

def read_positions(discovered, board, input1, input2):
    '''(list of str), (list of str, int, int -> none

       Function that determines the position by reading the input of the user
    '''
    discovered[input1-1] = True 
    discovered[input2-1] = True 
    print_board(discovered)
    print()

def check_positions(discovered,input1,input2):
    '''(list of str), int, int -> (list of str)

       Function that checks if the user input matches the position the variable discovered.
       Prints a list of string of '*' if positions don't match, and prints the correct value
       if they match.
    '''
    
    if board[input1-1] != board[input2-1]:
        discovered[input1-1] = False 
        discovered[input2-1] = False 
        print_board(discovered)
        print()
        return discovered
    
    else:
        print_board(discovered)
        print()
        return discovered


def play_game(board):
    '''(list of str)->None

       Function that starts the game , using try and except statement to validate user input
    '''
    try:
        discovered = [False]*len(board)
        size = len(board)
        print_board(discovered)
        print("\n")
        stop = False
        game = True
        guess_count = 0
        max_guess = (size//2)

        
        while game == True:
            while(stop == False):
                try:
                    print("Enter two distinct locations on the board you want revealed.")
                    print("i.e two integers in the range [1, "+str(size)+"]")
                    print()
                    input1 = int(input("Player: "))
                    input2 = int(input("        "))
                    print()
                    
                    if (input1 > 0 and input1 <= len(board)) and (input2 > 0 and input2 <= len(board)) and input1 != input2:
                        if discovered[input1-1] != False or discovered[input2-1] != False:
                            print("One or more of those selections have already been discovered.")
                            print()
                        else:
                            stop = True
                    else:
                        print("The input needs to be two distinct numbers within the range, [1, "+str(size)+"]")
                        print()
                except ValueError:
                    print("The input needs to be two distinct numbers within the range, [1, "+str(size)+"]")
                    print()

            
            read_positions(discovered,board,input1,input2)
            wait_for_player()
            clear_screen()
            discovered = check_positions(discovered,input1,input2)
            guess_count += 1
            stop = False
            game = check_win(discovered,guess_count,max_guess)

    
    except TypeError:
        print("Your input is invalid. You might need to restart the module.")
        print()
        stop = False
        try:
            while stop == False:
                print("How many cards do you want to play with?")
                size = input("Please enter an even number between 2 and 52: ")
                if size.isalpha():
                    print("That was not a number.")
                else:
                    size = (int)(size)
                    board = create_board(size)
                if board != None:
                    stop = True
                print("\n")
        except ValueError:
            print("Please enter an even number between 2 and 52: ")
            print()
        play_game(board)



# MAIN
stop = False
size = ''
board = None


try:
    while stop == False:
        print("How many cards do you want to play with?")
        size = input("Please enter an even number between 2 and 52: ")
        if size.isalpha():
            print("That was not a number.")
        else:
            size = int(size)
            board = create_board(size)
        if board != None:
            stop = True
        print("\n")
except ValueError:
    print("Please enter an even number between 2 and 52: ")
    print()


play_game(board)

