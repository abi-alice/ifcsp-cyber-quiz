import pytest
from quiz import CyberQuiz

@pytest.fixture
def app():
    """Creates a CyberQuiz instance for testing."""
    quiz = CyberQuiz()
    yield quiz
    if quiz.timer_id:
        quiz.after_cancel(quiz.timer_id)
    quiz.destroy()

def test_smoke():
    """Smoke test to ensure pytest works"""
    assert 2+2==4

class TestNameCheck:
    """Tests the name validation functions.""" 
    def test_length_edge(self, app):
        """Verifies edge instances are accepted or rejected."""
        assert app.length_check("Cat") is True
        assert app.length_check("Ca") is False

    def test_format(elf, app):
        """Verifies incorrect formats are rejected."""
        assert app.format_check("12345") is False
        assert app.format_check("$am") is False
        assert app.format_check("*_%") is False

    def test_presence(self, app):
        """Verifies user cannot progress without entering a name."""
        assert app.presence_check("") is False


class TestLoadQuiz:
    """Tests the load_quiz function."""
    def test_load_quiz_dict(self, app):
        """Verifies the questions are loaded as a list"""
        questions = app.load_quiz("question_and_answer.csv")
        assert isinstance(questions, list)

    def test_load_quiz_format(self, app):
        """Verifies the quiz is loaded with the correct format"""
        questions = app.load_quiz("question_and_answer.csv")
        for q, opts, ans in questions:
            assert isinstance(q, str)
            assert len(opts) == 4
            assert 0<=ans<=3

class TestTimer:
    """Tests the timer functions."""
    def test_start_timer_sets_time(self, app):
        """Verifies starting timer actually starts counter."""
        app.start_timer()
        assert app.start_time is not None

    def test_total_time(self, app):
        """Verifies summation of times."""
        app.times=[1, 2, 3]
        assert app.total_time() == 6

    def test_zero_elapsed_time(self, app):
        """Verifies seconds elapsed works."""
        app.start_time = None
        assert app.elapsed_time() == 0

    def test_average_time(self, app):
        """Verifies average is calculated correctly."""
        app.times=[5,10,15]
        assert app.average_time() == 10