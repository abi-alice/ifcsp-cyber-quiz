import quiz_logic # File where the modules being tested are stored

def test_smoke():
    """Smoke test to ensure pytest works"""
    assert 2+2==4

class TestNameCheck():
    """Tests the name validation functions.""" 
    def test_length_edge(self):
        """Verifies edge instances are accepted or rejected."""
        assert quiz_logic.length_check("Cat") is True
        assert quiz_logic.length_check("Ca") is False

    def test_format(self):
        """Verifies incorrect formats are rejected."""
        assert quiz_logic.format_check("12345") is False
        assert quiz_logic.format_check("$am") is False
        assert quiz_logic.format_check("*_%") is False

    def test_presence(self):
        """Verifies user cannot progress without entering a name."""
        assert quiz_logic.presence_check("") is False


class TestLoadQuiz():
    """Tests the load_quiz function."""
    def test_load_quiz_dict(self):
        """Verifies the questions are loaded as a list."""
        questions = quiz_logic.load_quiz("question_and_answer.csv")
        assert isinstance(questions, list)

    def test_load_quiz_format(self):
        """Verifies the quiz is loaded with the correct format"""
        questions = quiz_logic.load_quiz("question_and_answer.csv")
        for q, opts, ans in questions:
            assert isinstance(q, str)
            assert len(opts) == 4
            assert 0<=ans<=3

class TestTimer():
    """Tests the timer functions."""

    def test_total_time(self):
        """Verifies summation of times."""
        times=[1, 2, 3]
        assert quiz_logic.calculate_total_time(times) == 6

    def test_average_time(self):
        """Verifies average is calculated correctly."""
        times=[5,10,15]
        assert quiz_logic.calculate_average_time(times) == 10
    
    def test_average_time_empty(self):
        """Verifies average is 0 when list of times is empty."""
        times = []
        assert quiz_logic.calculate_average_time(times) == 0