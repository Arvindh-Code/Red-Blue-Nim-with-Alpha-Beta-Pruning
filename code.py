import sys

'''
Following alphabetadecision,maxvalue,minvalue function were referred on the class ppt - "Alpha - Beta Pruning[3]"
where we have pseudo code for these three function. So I implemented AlphaBeta Pruning using that pseudo code. 
'''
def alphabetadecision(state, version):
    '''
    :param state: state of the pile
    :param version: game version - standard/misere
    :return : min/max value and pile - red/blue
    :reference : "Alpha - Beta Pruning[3]" ppt
    This function finds the best move for a given state with help of MaxValue function,
    and efficiently find computer's move.
    '''
    if version == "standard":
        return minvalue(state, -1e308, 1e308)[1]
    else:
        return maxvalue(state, -1e308, 1e308)[1]

def maxvalue(state, alpha, beta):
    '''
    :param state: state of the pile
    :param alpha: possible values of lower bound
    :param beta: possible values of upper bound
    :return : min/max value and pile - red/blue
    :reference : "Alpha - Beta Pruning[3]" ppt
    This function finds the maximum utlity value for the given state using evan method
    and considering the alpha-beta value take the value using tree like structure,
    and return that efficiently value.
    '''

    if state[0] == 0 or state[1] == 0:
        return ((2 * state[0] - 3 * state[1]), None)
    v = -1e308
    move = None
    for a in ["red", "blue"]:
        minimumvalue = minvalue(successor_state(state, a), alpha, beta)
        if minimumvalue[0] > v:
            v = minimumvalue[0]
            move = a
        if v >= beta:
            return (v, move)
        alpha = max(alpha, v)
    return (v, move)

def minvalue(state, alpha, beta):
    '''
    :param state: state of the pile
    :param alpha: possible values of lower bound
    :param beta: possible values of upper bound
    :return : min/max value and pile - red/blue
    :reference : "Alpha - Beta Pruning[3]" ppt
    This function finds the maximum utlity value for the given state using evan method
    and considering the alpha-beta value take the value using tree like structure,
    and return that efficiently value.
    '''

    if state[0] == 0 or state[1] == 0:
        return ((2 * state[0] - 3 * state[1]), None)
    v = 1e308
    move = None
    for a in ["red", "blue"]:
        maximumvalue = maxvalue(successor_state(state, a), alpha, beta)
        if maximumvalue[0] < v:
            v = maximumvalue[0]
            move = a
        if v <= alpha:
            return (v, move)
        beta = min(beta, v)
    return (v, move)

def successor_state(state, action):
    '''
        Calculating the sucessor state based on action and state passed to the function
    '''

    if action == "red":
        return (state[0] - 1, state[1])
    else:
        return (state[0], state[1] - 1)

def nim(redmarbles, bluemarbles,version, playerone):
    '''
    :param redmarbles: count of red marbels in the pile
    :param bluemarbles:count of blue marbels in the pile
    :param version: standard/misere - based on the user input
    :param playerone: computer/human - based on the user input
    :return: no return type
    initializing a while loop where it iterates till either of the pile become 0.
    Based on the computer's and user player turn marble gets reduced from the pile.
    Computer's turn - Using MinMax - AlphaBeta Pruning the marble get reduced
    User player turn - player will choose the pile to reduce a marble.
    After either of the pile of become empty result will be print based on version of the game.
    '''
    version = version.strip().lower()
    playerone = playerone.strip().lower()
    while redmarbles > 0 and bluemarbles > 0:
        print("Red Marbles : ", redmarbles, "\nBlue Marbles: ", bluemarbles)
        #print(first_player)
        if playerone == "human":
            print("User player turn:")
            print("Red Marbles : ", redmarbles, "\nBlue Marbles: ", bluemarbles)
            while True:
                inputpile = input("Choose a pile (Red or Blue): ").strip().lower()
                if inputpile in ["red", "blue"]:
                    break
                else:
                    print("Type valid input - Red/Blue")
            if inputpile == "red":
                redmarbles -=1
            if inputpile == "blue":
                bluemarbles -=1
            playerone = "computer"
        if playerone == "computer":
            print("Computer turn")
            action = alphabetadecision((redmarbles, bluemarbles), version)
            state = (redmarbles, bluemarbles)
            if action == "blue" and state[1] != 0 and state[0] != 0:
                print("Computer removed - Blue Marble")
                state = successor_state(state, action)
                redmarbles, bluemarbles = state
            if action == "red" and state[1] != 0 and state[0] != 0:
                print("Computer removed - Red Marble")
                state = successor_state(state, action)
                redmarbles, bluemarbles = state
            playerone = "human"

    print("End of the Game!!!\nRemaining Marble in the pile:")
    print("Red Marbles : ", redmarbles, "\nBlue Marbles: ", bluemarbles)
    if redmarbles == 0 or bluemarbles == 0:
        score = 2 * redmarbles - 3 * bluemarbles
        if score < 0:
            score *= -1
        if version == "standard":
            if playerone == "human":
                print("Human Lose :(","\nComputer won :) with score of ", score)
            else:
                print("computer Lose :(","\nHuman won :) with score of ", score)
        if version == "misere":
            if playerone == "computer":
                print("Human Lose :(","\ncomputer won :) with score of ", score)
            else:
                print("Computer Lose :(","\nhuman won :) with score of ", score)

'''
main excution of the code starts from here
'''

if len(sys.argv) < 3:
    print("Enter the correct command like - red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>")
    sys.exit()
numred = int(sys.argv[1])
numblue = int(sys.argv[2])
#default option if <version> is not given
version = "standard"
    #default option if <first-player> is not give
playerone = "computer"
depthlimit = None
if len(sys.argv) > 3:
    version = sys.argv[3]
if len(sys.argv) > 4:
    playerone = sys.argv[4]
if len(sys.argv) > 5:
    depthlimit = int(sys.argv[5])
if version not in ["standard", "misere"]:
    print("Enter correct version - standard/misere")
    sys.exit()
if playerone not in ["computer", "human"]:
    print("Enter correct first-player - computer/human")
    sys.exit()
if depthlimit is not None and depthlimit <= 0:
    print("Enter correct depth limit")
    sys.exit()
nim(numred, numblue, version, playerone)