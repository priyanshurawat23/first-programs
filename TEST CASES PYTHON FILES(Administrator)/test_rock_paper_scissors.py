import unittest
from unittest.mock import patch
from rock_paper_scissors import play_game

class TestRockPaperScissorsGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'n'])
    def test_play_game_draw(self, mock_input):
        with self.assertLogs() as logs:
            play_game()
        self.assertIn('<== It\'s a tie ==>', logs.output[0])

    @patch('builtins.input', side_effect=['2', 'n'])
    def test_play_game_user_wins(self, mock_input):
        with self.assertLogs() as logs:
            play_game()
        self.assertIn('<== User wins ==>', logs.output[0])

    @patch('builtins.input', side_effect=['3', 'n'])
    def test_play_game_computer_wins(self, mock_input):
        with self.assertLogs() as logs:
            play_game()
        self.assertIn('<== Computer wins ==>', logs.output[0])

if __name__ == '__main__':
    unittest.main()
