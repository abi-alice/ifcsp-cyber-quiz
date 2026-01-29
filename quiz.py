import tkinter as tk # Imports library for GUI
from tkinter import messagebox # Shows error messages
import csv # Allows writing of results to CSV file
import re # Allows format check of name entry
from datetime import datetime # Allows timestamp to be recorded with results 

questions = [
    "Passwords should be...?",
    "What does NCSC advise for password creation?",
    "How should you classify data containing personally identifiable information?",
    "What should you do if you come across a suspicious email?",
    "When using a VPN, what can't you hide?",
    "What's the best way to minimise your digital footprint?",
    "Which part of your car is the most vulnerable to hacking?",
    "Which people in a business should be responsible for cybersecurity?",
    "Which of the following are considered personal data under GDPR?",
    "What is a firewall?",
    "How often should you update software?",
    "What is malware?",
    "What is two factor authentication?"
    ] 
answer_opts = [
                ['complex and unique', 'similar and short', 'basic and easy', 'short and complex'],
                ['birth date', 'family info', 'three random words', 'name of a pet'],
                ['SNI', 'Not Protectively Marked', 'Protect-Commercial and Contracts', 'Protect-Private'],
                ['Click on all the links', 'Report and delete it', 'Forward the email to your colleagues', 'Reply to it'],
                ['Your identity', 'Your data', "The fact you're using a VPN", 'Your device'],
                ['Take less photos on your phone', 'Post less on social media', 'Travel less with your phone', 'Use your phone more'],
                ['Entertainment system', 'Wireless key fob', 'Cruise control', 'Warning lights'],
                ['Directors', 'IT specialists', 'Managers', 'All personnel'],
                ['IP address', 'Birthdate', 'Home address', 'All of the above'],
                ['A physical wall for servers', 'Software monitoring network traffic', 'A type of virus', 'When a wall catches fire'],
                ['Never', 'Twice a year', 'As soon as updates are available', 'When something breaks'],
                ['Software designed to harm', 'An antivirus program', 'A type of hardware', 'A type of clothes'],
                ['Using two passwords', 'Using a password and other authentication method', 'Having two accounts', 'Logging in twice']
               ]

answers = [0, 2, 3, 1, 2, 1, 0, 3, 3, 1, 2, 0, 1] 
results = "results.csv"


class CyberQuiz(tk.Tk):
    """A class to represent the quiz itself.
    
    Methods: 
    start_quiz()
    load_question()
    submit():
    get_name()
    display_output()
    error_handler()
    format_check()
    presence_check()
    length_check()
    finish_quiz()
    save_results()
    
    """
    def __init__(self):
        """ Name entry and constructs all the necessary attributes for the quiz object.
        
        Parameters:
        self: used to initialise within class

        Returns:
        tkinter frame
        """
        super().__init__()

        self.title("Cyber Security Quiz")
        self.geometry('900x700')
        self.config(bg="pale turquoise")
        self.q_no = 0
        self.score = 0
        self.selected = tk.IntVar()
        self.player_name = ""

        self.name_frame = tk.Frame()
        self.name_frame.pack(pady=50)
        self.name_frame.config(bg="pale turquoise")

        tk.Label(self.name_frame, text="Enter your name:", font=("Arial", 14), bg="pale turquoise").pack(pady=10)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 12))
        self.name_entry.pack(pady=10)
        
        
        
        tk.Button(self.name_frame, text="Start Quiz", command=self.start_quiz, font=("Arial", 12)).pack(pady=10)
        
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

    def start_quiz(self):
         
        #if self.valid_name(self.player_name) != "OK":
         #   self.valid_name(self.player_name)
        self.questions = questions
        if not self.questions:
            self.error_handler("No questions available, please try again")

        self.name_frame.pack_forget()
        self.quiz_frame.pack(pady=20)
        self.load_question()

    def load_question(self):
        self.selected.set(-1)
        self.question_label.config(text=f"Q{self.q_no + 1}: {questions[self.q_no]}")
        for i, opt in enumerate(answer_opts[self.q_no]):
            self.radio_buttons[i].config(text=opt)
        
    def submit(self):
        if self.selected.get() == -1:
            self.error_handler("You must select an answer!")
            return "No answer selected"
        
        if self.selected.get() == answers[self.q_no]:
            self.score +=1
        self.q_no += 1

        if self.q_no <  len(self.questions):
            self.load_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
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
