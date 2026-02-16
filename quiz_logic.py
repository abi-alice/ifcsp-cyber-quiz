import re
import csv


def length_check(name):
    return 3 <= len(name) <= 20


def format_check(name):
    format_pattern = re.compile(r"^[a-zA-Z- ]+$")
    return bool(format_pattern.match(name))


def presence_check(name):
    return bool(name)


def load_quiz(filepath):
    questions = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if len(row) >= 6:
                    question = row['question']
                    options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']]
                    correct_answer = int(row['correct_answer'])
                    questions.append((question, options, correct_answer))
    except FileNotFoundError:
        return []
    return questions


def calculate_total_time(times):
    return sum(times)


def calculate_average_time(times):
    if not times:
        return 0
    return sum(times) / len(times)