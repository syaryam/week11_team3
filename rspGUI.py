import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("가위바위보 게임")
        
        # 게임 상태 변수
        self.user_wins = 0
        self.computer_wins = 0
        
        # 위젯 생성
        self.label_score = tk.Label(root, text="현재 스코어 - 사용자: 0, 컴퓨터: 0", font=("Arial", 14))
        self.label_score.pack(pady=10)
        
        self.label_result = tk.Label(root, text="게임 시작!", font=("Arial", 16), fg="blue")
        self.label_result.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        self.button_rock = tk.Button(self.button_frame, text="바위", width=10, font=("Arial", 12), command=lambda: self.play_round('r'))
        self.button_rock.grid(row=0, column=0, padx=5)
        
        self.button_scissors = tk.Button(self.button_frame, text="가위", width=10, font=("Arial", 12), command=lambda: self.play_round('s'))
        self.button_scissors.grid(row=0, column=1, padx=5)
        
        self.button_paper = tk.Button(self.button_frame, text="보", width=10, font=("Arial", 12), command=lambda: self.play_round('p'))
        self.button_paper.grid(row=0, column=2, padx=5)
        
        self.label_final_result = tk.Label(root, text="", font=("Arial", 14), fg="red")
        self.label_final_result.pack(pady=20)
    
    def play_round(self, user_choice):
        computer_choice = random.choice(['r', 's', 'p'])
        result = ""
        
        if user_choice == computer_choice:
            result = "비겼습니다!"
        elif self.win(user_choice, computer_choice):
            result = "이겼습니다!"
            self.user_wins += 1
        else:
            result = "졌습니다!"
            self.computer_wins += 1
        
        # 결과와 점수 업데이트
        self.label_result.config(text=f"결과: {result} (사용자: {self.choice_to_text(user_choice)}, 컴퓨터: {self.choice_to_text(computer_choice)})")
        self.label_score.config(text=f"현재 스코어 - 사용자: {self.user_wins}, 컴퓨터: {self.computer_wins}")
        
        # 최종 승리 여부 확인
        if self.user_wins == 2 or self.computer_wins == 2:
            if self.user_wins == 2:
                self.label_final_result.config(text="축하합니다! 승리했습니다!")
            else:
                self.label_final_result.config(text="아쉽습니다. 컴퓨터가 승리했습니다.")
            
            # 버튼 비활성화
            self.button_rock.config(state="disabled")
            self.button_scissors.config(state="disabled")
            self.button_paper.config(state="disabled")
    
    def win(self, player, opponent):
        return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')
    
    def choice_to_text(self, choice):
        return {"r": "바위", "s": "가위", "p": "보"}[choice]

# Tkinter 초기화
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
