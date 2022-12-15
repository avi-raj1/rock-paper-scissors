from common.utils import scoring_profile, key_beats_value_map
import logging

logging.basicConfig(filename="logs/history.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Turn:
    def __init__(self, user_choice: str, computer_choice: str):
        self.user_choice = user_choice
        self.computer_choice = computer_choice
        logger.info(f'User choice = {user_choice}, Computer Choice = {computer_choice}')

    def execute(self):
        if self.user_choice == self.computer_choice:
            print('Result: It is a draw')
            return scoring_profile['draw'], scoring_profile['draw']
        elif key_beats_value_map[self.computer_choice] == self.user_choice:
            print('Result: Computer wins!')
            return scoring_profile['lose'], scoring_profile['win']
        else:
            print('Result: User wins!')
            return scoring_profile['win'], scoring_profile['lose']
