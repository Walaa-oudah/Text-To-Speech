from gtts import gTTS
import os

# Text to convert to speech
text = "Hello, how are you today?"
# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted file (optional, requires an appropriate player installed)
os.system("start output.mp3")  # For Windows
# os.system("afplay output.mp3")  # For macOS
# os.system("mpg321 output.mp3")  # For Linux
