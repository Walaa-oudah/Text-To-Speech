# Text-To-Speech

This repository contains all the necessary Python code and supporting files to work through a Text-to-Speech (TTS) project using the Google Text-to-Speech (gTTS) library.


# About the Project

This project focuses on creating a Python application that converts written text into spoken words using the gTTS library. The application generates an audio file from the given text, which can then be played back on any compatible audio player.
The project is divided into two key functionalities:

1- Text Conversion: Converting a specified text string into speech.

2- Audio Playback: Saving the generated speech as an audio file and optionally playing it back.


### Text-to-Speech Purpose:

The primary purpose of the Text-to-Speech functionality is to transform written text into an audible format, making it accessible for auditory consumption. This is particularly useful for creating voiceovers, assisting the visually impaired, or simply adding a vocal element to applications.


### Structure:

#### 1. Python Script ('gTTS' and 'os.system' functions):

- Text Input: The script takes a predefined string of text that you want to convert into speech.

- Speech Synthesis: Utilizes the gTTS library to convert the text into speech, producing an audio file in MP3 format.
  
- Error Handling: Ensures that the audio file is created successfully and manages potential issues with file saving and playback.


### Audio File Creation Purpose:

Once the text is converted into speech, the application saves this as an MP3 file, allowing for easy distribution or playback. This ensures that the speech can be replayed without the need to reprocess the text each time.


### Structure:

#### 1. Text Conversion ('gTTS' object):

- Language Specification: The script allows you to specify the language of the text, with 'en' (English) being the default. (you can change it to any other language). 

- Audio File Output: The converted speech is saved to a file named output.mp3, which can be played on any device that supports MP3 playback.

#### 2. Optional Playback ('os.system' function):

- Cross-Platform Compatibility: The script includes commands to play the audio file on different operating systems (Windows, macOS, and Linux).
  

## Instructions and Navigation

- Use a server-side scripting language (Python).

### [Download and Install Visual Studio Code]: (https://code.visualstudio.com/download)


### Step 1: Install Required Libraries:

- Install the 'gtts' library for handling text-to-speech conversion.
  
### Step 2: Text Input:

- Define the text you want to convert into speech within the script.

### Step 3: Execute the Python Script:

- Run the script to generate the audio file from the text.

### Step 4: Testing:

- Play the generated 'output.mp3' file to verify the text-to-speech conversion.

#### The run code will be as shown in the pictures below:

<div> 
   
<img src="https://github.com/user-attachments/assets/c44b4fa4-25dd-4019-b47e-499c9fac195b" width="600" height="400">

</div>
   
   
# Summary:

In the Text-to-Speech project, Python is used to convert written text into spoken words, which are then saved as an MP3 file. This project showcases the simplicity and effectiveness of integrating text-to-speech capabilities into a Python application, providing a user-friendly way to create audible content from text.


### Technologies Used:

•	Python

•	Google Text-to-Speech (gTTS) Library

•	Command-Line Interface (CLI)

•	Visual Studio Code


## Thank You!

