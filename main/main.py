import random

def play():
    user = input("가위 = S, 바위 = R, 보 = P: ")
    computer = random.choice(['R', 'S', 'P'])

    if user == computer:
        return "비겼습니다."
    if win(user, computer):
        return "이겼습니다."
    return "졌습니다."

def win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
    or (player == 'P' and opponent == 'R'):
        return True
    return False

#일단 기본 코드입니다