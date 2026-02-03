import pytest
from quiz import CyberQuiz

quiz = CyberQuiz

class TestNameCheck:
    """Tests the name validation functions.""" 
    def test_length_edge(self):
        """Verifies edge instances are accepted or rejected."""
        assert quiz.length_check(self, "Cat") == True
        assert quiz.length_check(self, "Ca") == False

    def test_format(self):
        """Verifies incorrect formats are rejected."""
        assert quiz.format_check(self, "12345") == False
        assert quiz.format_check(self, "$am") == False
        assert quiz.format_check(self, "*_%") == False

    def test_presence(self):
        """Verifies user cannot progress without entering a name."""
        assert quiz.presence_check(self, "") == False

class TestLoadQuiz:
    """Tests the load_quiz function."""
    def test_load_quiz_dict(self):
        """Verifies the questions are loaded as a list"""
        questions = quiz.load_quiz(self, "question_and_answer.csv")
        assert isinstance(questions, list)

    def test_load_quiz_format(self):
        """Verifies the quiz is loaded with the correct format"""
        questions = quiz.load_quiz(self, "question_and_answer.csv")
        for q, opts, ans in questions:
            assert isinstance(q, str)
            assert len(opts) == 4
            assert 0<=ans<=3
