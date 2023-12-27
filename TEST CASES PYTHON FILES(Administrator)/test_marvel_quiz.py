import unittest
from unittest.mock import patch
from io import StringIO

# Import the functions to be tested
from marvel_quiz import ask_question, play_marvel_quiz

class TestMarvelQuiz(unittest.TestCase):

    @patch('builtins.input', side_effect=['6'])
    def test_ask_question_correct_answer(self, mock_input):
        global score
        global ques
        score = 0
        ques = 0
        ask_question(1, '6', 'How many Infinity Stones are there?')
        self.assertEqual(score, 1)
        self.assertEqual(ques, 1)

    @patch('builtins.input', side_effect=['5'])
    def test_ask_question_incorrect_answer(self, mock_input):
        global score
        global ques
        score = 0
        ques = 0
        ask_question(1, '6', 'How many Infinity Stones are there?')
        self.assertEqual(score, 0)
        self.assertEqual(ques, 1)

    @patch('builtins.input', side_effect=['yes', '6', 'captain america civil war', 'mjolnir', 'shield', 'endgame'])
    def test_play_marvel_quiz(self, mock_input):
        global score
        global ques
        score = 0
        ques = 0
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            play_marvel_quiz()
            output = mock_stdout.getvalue().strip()
            self.assertIn('You are', output)

if __name__ == '__main__':
    unittest.main()
