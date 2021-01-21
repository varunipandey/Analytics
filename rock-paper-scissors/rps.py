import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors.\n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It\'s a tie"
    if is_win(user, computer):
        return f"You won! Your choice -> {user} and computer's choice -> {computer}"
    return f"You lost! Your choice -> {user} and computer's choice -> {computer}"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())
