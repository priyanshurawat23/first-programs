import unittest
from HANGMAN_GAME import hangman_game

class TestHangmanGame(unittest.TestCase):
    def test_hangman_win(self):
        result, correct_word = hangman_game(['Alice', 'a', 'b', 'c', 'd', 'e', 'x', 'y', 'z', 'w', 'v'])
        self.assertEqual(result, 'win')
        self.assertIn(correct_word, ['frown', 'rainbow', 'water', 'board', 'player', 'geeks', 'python', 'science', 'rough', 'miner'])

    def test_hangman_lose(self):
        result, correct_word = hangman_game(['Bob', 'x', 'y', 'z', 'w', 'v'])
        self.assertEqual(result, 'lose')
        self.assertIn(correct_word, ['frown', 'rainbow', 'water', 'board', 'player', 'geeks', 'python', 'science', 'rough', 'miner'])

if __name__ == '__main__':
    unittest.main()