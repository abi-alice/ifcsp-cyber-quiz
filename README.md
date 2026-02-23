# Cyber Security Awareness Quiz Application

Welcome to the Cyber Quiz App repository! 
This simple tkinter GUI-based application using [Python 3.11](https://www.python.org/downloads/release/python-3110/) will test users on their basic cyber security knowledge, and stores their name and result in a CSV file. My organisation is constructing a nuclear power station, so all employees must have basic cyber security awareness.
This is vital as without it, the risk of classified information being leaked is at a much greater risk, and a data breach could put millions of people in danger.
There is a large variety of teams with specific functions throughout the organisation, including many external contractors. However all teams handle organisational data in some way, and as construction progresses, the sensitivity of the data will only increase.
It is best to ensure cyber security principles are well ingrained among the workforce so that good habits are built and risk from lack of knowledge stays as low as possible.

## Design

### Functional Requirements

- The application will raise awareness of basic cyber security.
- The application will allow the user to input their name.
- The application will read questions and answers from a CSV.
- The application will store results, user's name, and timestamp in another CSV.
- The application will display 13 questions, with each showing after the previous answer was submitted.
- The application will allow the user to select an answer from four choices.
- The application will show a "Submit" button below any input.
- Once the quiz is complete, the application will display a messagebox with the final score and verification that the result has been saved.
  
### Non-Functional Requirements

- The application will handle invalid inputs gracefully without crashing.
- The application will respond to input within one second.
- The application will run on any system supporting Python and Tkinter.
- The application will have pure functions with well-structured code.
- The application will have appropriately readable font sizes and colours.
- The application will be well documented to allow for easy understanding of the code.
- The design for the application will allow for easy addition of new features.
- The application will display a window titled "Cyber Security Quiz".
- The background colour of the window will be #afeeee.
- The dimensions of the application window will be 900x700 pixels.
- The application will have an uncomplicated, easy to follow design.

  
### GUI Design

The app was prototyped using Figma, with the first two and last two screens being shown without the bulk of the questions in between.
The interactive prototype can be found [here](https://www.figma.com/proto/XhfVawua1lscAGsC1LFh0Z/Quiz-Plan?node-id=0-1&t=wTGycgCyPZGa6Z6B-1).  

![first screen](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/prototype%201.png)   
**Figure 1:** The first screen shown to the user on running the quiz.
![second screen](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/prototype%202.png)    
**Figure 2:** The screen shown to the user after entering a valid name.
![penultimate screen](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/prototype%203.png)   
**Figure 3:** The screen of the last question of the quiz with an answer having been selected.
![last screen](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/prototype%204.png)   
**Figure 4:** The messagebox showing the user's result once the last answer has been submitted.   
Figures 1-4 show each stage of the interactive prototype, which illustrates the first, second, penultimate, and last screens of the quiz.

### Code Design

The class diagram (Figure 5) was created using [diagrams.net](diagrams.net) and summarises the code design.
The ```CyberQuiz``` class inherits from the ```tk.Tk``` class, which provides the GUI functionality using Tkinter. This inheritance allows ```CyberQuiz``` to use and the methods and attributes of ```tk.Tk```, creating a customised window with features for user input, input validation, displaying message boxes, and using CSVs.

![class diagram for the CyberQuiz class](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/class%20diagram.png)      
**Figure 5:** The class diagram of the application

### Tech Stack Outline

This app was developed in [Visual Studio Code](https://code.visualstudio.com/) using Python 3.11, [Pytest](https://docs.pytest.org/en/stable/), and [Tkinter](https://docs.python.org/3/library/tkinter.html). It uses CSVs to store results and read questions and answers .

## Development

The various comments at the beginning of the code explain the reasons for each import, and the brief docstrings in the class ```CyberQuiz``` and in each function give an overview of their purpose.  
```super().__init__()``` in the function ```__init__``` is used to intialise the attributes of the parent class, which in this case is Tkinter, as well as any attributes defined in the child class, ```CyberQuiz```.  

Labels, buttons, and radio buttons are all initialised similarly, for example the 'Start Quiz' button, which is intialised below:   
```tk.Button(self.name_frame, text="Start Quiz", command=self.get_name, font=("Arial", 16)).pack(pady=10)```   
```name_frame``` is a Tkinter frame, and defines the frame in which the button will be initialised. The text variable defines the text that will be displayed on the button, and the command variable defines what will happen when the button is pressed, in this case it is the function ```get_name```.
The font variable determines the font and size.  
```pack(pady=10)``` adds space above the button to allow for better readability.  

The initialisation of the radio buttons takes place in a loop as there are four of them for each question and saves time having to type the same block of code four times.  

```  
def load_quiz(self, filepath):
        """Loads questions, options, and answer index from CSV."""
        questions = []
        try:
            with open(filepath, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 6:
                        question = row['question']
                        options = [row['option_a'], row['option_b'], row['option_c'] ,row['option_d']]
                        correct_answer = int(row['correct_answer'])
                        questions.append((question, options, correct_answer))
        except FileNotFoundError:
            self.error_handler("The question file couldn't be found, please close the program and restart.")
        return questions
```
This function starts by creating an empty list of questions, and opens the file with UTF-8 encoding to allow any accented letters to be read accurately.
```csv.DictReader``` reads the rows as dictionaries, as the file has headers which should be ignored when printing the questions.
For each row, the program checks that there are at least six columns, and appends the questions, options, and answers as tuples to the list.
If there is no file in the specified filepath when the function is called, a messagebox appears prompting the user to restart the program.

```
def load_question(self):
        """Displays currrent question and answer options"""
        self.selected.set(-1)
        q, options, _ = self.questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}: {q}")
        for i, opt in enumerate(options):
            self.radio_buttons[i].config(text=opt)
        self.start_timer()
```
This function begins by clearing the selected option.
The next line gets the current question tuple by using the question number as an index, unpacking it into the question text and list of answer options, and throwing away the correct index as it isn't needed in the question display.
The following line updates the question label to show the question, with the ```+1``` used so the display starts at Q1 instead of Q0.
Next, the options list is looped over to set each radio button's label to one of the answer options, and finally the ```start_timer``` function is called.  

```
def stop_timer(self):
        """Stops timing when answer is submitted and records time elapsed in seconds."""
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        elapsed = time.time() - self.start_time
        self.times.append(elapsed)
        self.start_time = None
        return elapsed
```
```if self.timer_id``` checks if a timer is currently running. If it is, the timer is stopped and marked as such.
The elapsed time calculates how many seconds have passed, and adds it to a list which will be used to calculate the total time later.
The start time is then reset ready for the next question and elapsed time is returned, so the function can be used in unit testing.

```
def save_result(self, name, percentage):
        """Save quiz result to CSV file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(results, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, percentage, round((self.average_time()), 1), round((self.total_time()), 1), timestamp])
```
To save the result, first a timestamp is created with the date and time of when the final 'Submit' button is clicked.
The CSV which stores the results is then appended to add the name, percentage, average time to answer a question, total time to complete the quiz, and timestamp.
The times are rounded to the nearest 0.1 second for ease of reading.

## Testing

The application was tested by both manual and automated unit testing. Automated testing and the use of continuous integration (CI) when developing the timer feature was useful as I didn't have to keep running the application.
However, especially when testing GUI features it was best to use manual testing too as I could then adopt the perspective of an end user.
This made functional and non-functional requirement testing more effective, for example checking that the text contrasted the background enough and was big enough to read easily.
I used Pytest in my automated testing, however only incorporated CI when I added the timer function.

### Manual Testing

**Table 1:** Shows various manual test cases and results
| Test Case ID | Functionality | Test Description | Expected Result | Actual Result | Pass/Fail |
|--------------|---------------|------------------|-----------------|---------------|-----------|
| 1 | Accessibility | Test the application is easy to read | Adequate colour contrast and text size | Application can be read and understood easily thanks to text size and contrast | Pass |
| 2 | Display | Tests messageboxes show | Messagebox appears in the case of invalid name entry and at completion of the quiz | Messagebox appears and displays correct message | Pass |
| 3 | Display | Tests that timer is visible and counts up | Purple timer counting up each second | Timer not visible | Fail |
| 4 | Display | Tests that timer is visible and counts up | Purple timer counting up each second | Timer visible and updating | Pass |
| 5 | Core function | Tests that program is writing results correctly to CSV | CSV updated with name and statistics | CSV stays empty | Fail |
| 6 | Core function | Tests that program is writing results correctly to CSV | CSV updated with name and statistics | CSV is updated correctly | Pass |
| 7 | Error handling | Tests that invalid name input isn't accepted | Messagebox appears with error message | Quiz starts as normal | Fail |
| 8 | Error handling | Tests that invalid name input isn't accepted | Messagebox appears with error message | Messagebox repeatedly appears even after dismissing error message | Fail |
| 9 | Error handling | Tests that invalid name input isn't accepted | Messagebox appears with error message | User can retype name and quiz starts if valid | Pass |  

Table 1 shows some of the manual tests carried out on the application as development continued.

### Automated Testing

![1 test passing](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/1%20test%20passed.png)
**Figure 6:** One test passing.
![5 tests passing](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/5%20tests%20passing.png)
**Figure 7:** Five tests passing.
![all tests passing](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/all%20tests%20passing.png)
**Figure 8:** All nine tests passing.

Figures 6-8 show automated tests gradually passing. Almost all of them failed in the first photo as the testing file was written badly, and the following pictures required tweaks to the main quiz file and creating a separate file of the quiz logic to be tested, the reason for which is explained in the technical documentation.

## Documentation

### User Documentation

This application was designed for SZC employees and contractors to gauge general cyber and information security awareness in a more interesting way.

#### Step 1: Installing Python

If you already have Python installed, you can skip this step and start from **Step 2**.  
More comprehensive documentation on the installation of Python can be found [here](https://docs.python.org/3/using/index.html).  
The recommended way to run projects is in a virtual environment (or venv), and instructions can be found in **Step 3**, however this is optional.

##### Windows

Download Python 3.11 from [the Python website](https://www.python.org/downloads/). From there, you can run Python in the terminal by simply typing ```python```.  

##### macOS

A list of installers is available [here](https://www.python.org/downloads/macos/) for macOS. [This page](https://docs.python.org/3/using/mac.html) provides screenshots and instructions of how to properly install Python.

#### Step 2: Cloning the repository
As shown in Figure 9, copy the HTTPS web URL to your clipboard.  
![Cloning the repository](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/clone%20repo%201.png)
**Figure 9:** How to clone the repository using HTTPS.

#### Step 3: Opening the quiz

Open a terminal on your device, and type:  
``` cd /path/to/where/you/want/to/save/the/repository ```  
Then, type  
``` git clone https://github.com/abi-alice/ifcsp-cyber-quiz.git ```.  
Now you can create a venv if you choose to do so. Navigate to the repository using   
```cd /path/to/repository/ ``` 
then create the venv:  
```python -m venv <name for venv>```  
To activate in Windows, type ```.\<venv name>\Scripts\activate```, and to activate in macOS/Linux type ```source <venv name>/bin/activate```.  
You can now open the repository in your chosen code editor and follow the next steps to play the quiz.  
Once you're finished with the quiz, type ```deactivate``` into your venv to deactivate it. 
#### Step 4: Playing the quiz
Make sure that the ```quiz.py``` file is selected and run the quiz. Figure 10 shows how to do this in Visual Studio Code.  
![Running the quiz](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/vs%20code%20run%20quiz.png)  
**Figure 10:** How to run the quiz in VS Code.
Follow the instructions shown in the application window; good luck and have fun! 🌟

### Technical Documentation

Explanations of the code which are more detailed than the docstrings can be found in the **Development Section** above.
This application used PEP8 naming conventions for variables and classes.
Screen resolution must be minimum 900x700 pixels as this is the size of the quiz window.

#### Running your own tests

If you would like to run your own tests locally for the quiz, follow the above steps to clone the repository, and ensure that pytest is installed.
You can do this by running ```pip install pytest``` in the venv. 
To run pytest, simply type ```pytest``` in a terminal which is open in the folder of the repository. 
You can also add more tests in the ```test_quiz.py``` file, however they must use the logic in the ```quiz_logic.py``` file.
The current tests aren't very extensive but try to cover the main logic and a few edge instances.
A separate file for the logic was created to avoid errors when the tests were running by separating the logic from the GUI, so the tests don't try to load the Tkinter GUI. 
The functions from the main quiz file were directly copied to the logic file, and only altered as they were no longer in the ```CyberQuiz``` class.

#### Dependencies

As detailed in the comments of the code, ```tkinter``` is used for the GUI and is included with standard Python installations, so no additional packages are required.
```time``` and ```datetime``` are used for the timer and timestamps respectively, both of which are stored in the results CSV.
```csv``` is used for reading questions and saving results, as both utilise CSVs.
```re``` provides regular expression matching operations, which was used in the ```format_check``` to ensure no special characters or numbers are used in the user's name input.

## Evaluation

I think designing the GUI went well even though it was relatively simple, as I hadn't used Tkinter before this. 
I also enjoyed finding relevant questions to include on the quiz and the process of making the quiz flow from one question to the next. 
I struggled adding the timer feature as I also hadn't done much work with live timing in Python before, so I had to do a lot of research throughout the process of adding it.
However, it was a good experience for me as it helped to further develop my programming skills.
Finally, I think writing the user documentation went well and I also enjoyed writing the steps for others to run the code on their own devices.  
To further improve on this project, I could've incorporated GUI tests as well as logic tests and implemented CI earlier in the process.
This would have improved my development process as the tests would be more in depth and the features to fix would be clearer.  
I could have also made the GUI and hence Figma diagram slightly more detailed which would make the quiz more interesting for the end user.
To better show the development of the project, I should've uploaded the Figma diagram and class diagram earlier in the process to show that I created them in advance, and I shouldn't have updated the class diagram after adding the timer, as this would show more progression in my ideas for the project.
Overall, the development of the project went well and I enjoyed the whole process as it developed my skills and pushed me from my comfort zone.
