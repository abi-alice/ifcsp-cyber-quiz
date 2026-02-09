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
### Technical Documentation
## Evaluation
