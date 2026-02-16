import pytest
from quiz import CyberQuiz

quiz = CyberQuiz

def test_smoke():
    """Smoke test to ensure pytest works"""
    assert 2+2==4

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

class TestTimer:
    """Tests the timer functions."""
    def test_start_timer_sets_time(self):
        """Verifies starting timer actually starts counter."""
        quiz.start_timer()
        assert quiz.start_time is not None

    def test_total_time(self):
        """Verifies summation of times."""
        quiz.times=[1, 2, 3]
        assert quiz.total_time() == 6

    def test_zero_elapsed_time(self):
        """Verifies seconds elapsed works."""
        quiz.start_time = None
        assert quiz.elapsed_time() == 0

    def test_average_time(self):
        """Verifies average is calculated correctly."""
        quiz.times=[5,10,15]
        assert quiz.average_time() == 10