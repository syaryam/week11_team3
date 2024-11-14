import random

def play_round():
    user = input("가위 = s, 바위 = r, 보 = p: ")
    computer = random.choice(['r', 's', 'p'])
    
    if user == computer:
        print("비겼습니다.")
        return 0
    elif win(user, computer):
        print("이겼습니다.")
        return 1
    else:
        print("졌습니다.")
        return -1

def win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play_game():
    user_wins = 0
    computer_wins = 0
    
    while user_wins < 2 and computer_wins < 2:
        print(f"\n현재 스코어 - 사용자: {user_wins}, 컴퓨터: {computer_wins}")
        result = play_round()
        
        if result == 1:
            user_wins += 1
        elif result == -1:
            computer_wins += 1
            
    # 최종 결과 출력
    if user_wins == 2:
        print("\n축하합니다! 승리했습니다!")
    else:
        print("\n아쉽습니다. 컴퓨터가 승리했습니다.")

# 게임 시작
play_game()
