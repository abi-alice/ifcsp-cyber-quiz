# Cyber Security Awareness Quiz Application

Welcome to the Cyber Quiz App repository! 
This simple tkinter GUI-based application using Python 3.11 will test users on their basic cyber security knowledge, and stores their name and result in a CSV file. My organisation is constructing a nuclear power station, so all employees must have basic cyber security awareness.
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

### Code Design

The class diagram below was created using [diagrams.net](diagrams.net) and summarises the code design.
The ```CyberQuiz``` class inherits from the ```tk.Tk``` class, which provides the GUI functionality using Tkinter. This inheritance allows ```CyberQuiz``` to use and the methods and attributes of ```tk.Tk```, creating a customised window with features for user input, input validation, displaying message boxes, and using CSVs.

![class diagram for the CyberQuiz class](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/CyberQuiz.drawio.png)

### Tech Stack Outline

This app was developed in Visual Studio Code using Python 3.11, Pytest, and Tkinter. It uses CSVs to store results and read questions and answers 

## Development

## Testing

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
As shown in the below picture, copy the HTTPS web URL to your clipboard.  
![Cloning the repository](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/clone%20repo%201.png)

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
Make sure that the ```quiz.py``` file is selected and run the quiz. The screenshot below shows how to do this in Visual Studio Code.  
![Running the quiz](https://github.com/abi-alice/ifcsp-cyber-quiz/blob/main/images/vs%20code%20run%20quiz.png)  
Follow the instructions shown in the application window; good luck and have fun! 🌟

### Technical Documentation

## Evaluation
