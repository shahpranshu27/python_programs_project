import random

def play():
    user = input("What\s your choice ? \n'r' for rock,'p' for paper, 's' for scissor ")
    computer = random.choice(['r','p','s'])
    if user ==  computer : 
        # print("Draw")
        return 'tie'
    if is_win(user, computer):
        return "you won!"
    
    return "You lost!"
    # r>s,s>p,p>r
    # elif user == 'r' and computer == 'p':
    #     print("computer wins!")
def is_win(player, opponent):
        # returns true f player wins
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == ' p' and opponent == 'r'):
            return True
print(play())