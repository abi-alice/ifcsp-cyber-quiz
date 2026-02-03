import tkinter as tk # Imports library for GUI
from tkinter import messagebox # Shows error messages
import csv # Allows writing of results to CSV file
import re # Allows format check of name entry
from datetime import datetime # Allows timestamp to be recorded with results 


quiz_questions = "question_and_answer.csv"
results = "results.csv"


class CyberQuiz(tk.Tk):
    """A tkinter based cybersecurity quiz app.
    
    This app shows multiple-choice cybersecurity questions from a CSV file, and saves the user's name and score to a CSV file.

    """
    def __init__(self):
        """ Initialise the CyberQuiz instance by initialising quiz window and loading questions. """
        super().__init__()

        self.title("Cyber Security Quiz")
        self.geometry('900x700')
        self.config(bg="pale turquoise")
        self.q_no = 0
        self.score = 0
        self.questions = self.load_quiz(quiz_questions)
        self.selected = tk.IntVar()
        self.player_name = ""

        self.name_frame = tk.Frame()
        self.name_frame.pack(pady=50)
        self.name_frame.config(bg="pale turquoise")

        tk.Label(self.name_frame, text="Enter your name:", font=("Arial", 14), bg="pale turquoise").pack(pady=10)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 12))
        self.name_entry.pack(pady=10)
        
        
        
        tk.Button(self.name_frame, text="Start Quiz", command=self.get_name, font=("Arial", 12)).pack(pady=10)
        
        self.quiz_frame = tk.Frame()
        self.quiz_frame.config(bg="pale turquoise")

        self.question_label = tk.Label(self.quiz_frame, bg="pale turquoise", text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.radio_buttons=[]
        for i in range(4):
            rb = tk.Radiobutton(self.quiz_frame, bg="pale turquoise", text="", variable=self.selected, value=i, font=("Arial", 16))
            rb.pack(anchor="w", padx=50)
            self.radio_buttons.append(rb)

        self.submit_btn = tk.Button(self.quiz_frame, text="Submit", command=self.submit)
        self.submit_btn.pack(pady=20)
        
    def get_name(self):
        """Gets user's name and validates it."""
        self.player_name = self.name_entry.get().strip().title()    
        if not self.presence_check(self.player_name):
            self.error_handler("Name cannot be left blank")
            return "Presence check failed"
        elif not self.length_check(self.player_name):
            self.error_handler("Name must be between 3 and 20 characters")
            return "Length check failed"
        elif not self.format_check(self.player_name):
            self.error_handler("Name can only include letters, hyphens, and spaces")
            return "Format check failed"
        else:
            self.start_quiz()
            return "OK"
        
        
    def format_check(self,name):
        format = re.compile(r"^[a-zA-Z- ]+$")
        return bool(format.match(name))
    def length_check(self,name):
        return 3<=len(name)<=20
    def presence_check(self, name):
        return bool(name)

    def error_handler(self, message):
        try:
            messagebox.askretrycancel("Error", message)
        except Exception as e:
            print(f"Something went wrong: {e}")

    def load_quiz(self, filepath):
        """Loads questions, options, and answer index from CSV."""
        questions = []
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 6:
                    question = row['question']
                    options = [row['option_a'], row['option_b'], row['option_c'] ,row['option_d']]
                    correct_answer = int(row['correct_answer'])
                    questions.append((question, options, correct_answer))
        return questions
    
    def start_quiz(self):
        """Loads main quiz frame and shows questions."""
        self.name_frame.pack_forget()
        self.quiz_frame.pack(pady=20)
        self.load_question()
    
    def load_question(self):
        """Displays currrent question and answer options"""
        self.selected.set(-1)
        q, options, _ = self.questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}: {q}")
        for i, opt in enumerate(options):
            self.radio_buttons[i].config(text=opt)
        

    def submit(self):
        """Checks if answer is selected, checks if selected answer is correct and updates score."""
        if self.selected.get() == -1:
            self.error_handler("You must select an answer!")
            return "No answer selected"
        
        if self.selected.get() == self.questions[self.q_no][2]:
            self.score +=1
        self.q_no += 1

        if self.q_no <  len(self.questions):
            self.load_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        """Calculates and displays final score"""
        total = len(self.questions)
        percent = round((self.score / total) * 100, 1)
        self.save_result(self.player_name, percent)

        messagebox.showinfo("Quiz Complete!", f"Well done {self.player_name}! ⭐\nScore: {self.score}/{total} ({percent}%)\nYour results were saved to {results}.")
        
    def save_result(self, name, percentage):
        """Save quiz result to CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(results, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, percentage, timestamp])

if __name__ == "__main__":
    quiz = CyberQuiz()
    quiz.mainloop()
