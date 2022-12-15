from scripts.turn import Turn
from common.utils import short_cut_map, scoring_profile
import random
import logging

logging.basicConfig(filename="logs/history.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Game:
    def __init__(self):
        self.turns_played, self.user_score, self.computer_score = 0, 0, 0
        self.is_live = True
        print('Welcome to Rock Paper Scissors Game against Computer')
        print(
            f"Scoring: Winner gets {scoring_profile['win']} point and Loser gets {scoring_profile['lose']} point. In case of draw, they both get {scoring_profile['draw']} point")

    def display_score(self):
        print(f'Total rounds played = {self.turns_played}, Computer score = {self.computer_score}, User score = {self.user_score}')

    def exit_game(self):
        self.is_live = False
        if self.computer_score < self.user_score:
            final_result = 'User wins'
        elif self.computer_score > self.user_score:
            final_result = 'Computer wins'
        else:
            final_result = 'Draw'
        print(f'Thank you for playing Rock Paper Scissors! Here is the final result: {final_result}')
        logger.info(f"Final score: user = {self.user_score} computer = {self.computer_score}. Result: {final_result}")

    def play_valid_turn(self, user_choice: str):
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        print(f'Computer Choice: {computer_choice}')
        turn = Turn(user_choice, computer_choice)
        user_turn_score, computer_turn_score = turn.execute()
        self.turns_played += 1
        self.user_score += user_turn_score
        self.computer_score += computer_turn_score
        self.display_score()

    def play(self):
        print('-' * 100)
        user_input = input("Please Type and Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors or 'Q' to Quit the game : ")
        if user_input not in short_cut_map:
            print('Error: Wrong Input !!')
        else:
            user_choice = short_cut_map[user_input]
            print(f'User Choice: {user_choice}')
            if user_choice == 'Quit':
                self.exit_game()
            else:
                self.play_valid_turn(user_choice)
