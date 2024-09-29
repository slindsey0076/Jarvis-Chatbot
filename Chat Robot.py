import openai
from PyQt5 import QtWidgets

# Hardcode the OpenAI API key directly in the code
openai.api_key = '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'

class ChatbotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Jarvis Chatbot")

        # Create a QTextEdit widget to display the chat history and make it read-only
        self.chat_history = QtWidgets.QTextEdit()
        self.chat_history.setReadOnly(True)  # Make the chat history read-only so the user cannot edit it

        # Create a QLineEdit widget for user input
        self.user_input = QtWidgets.QLineEdit()
        self.user_input.returnPressed.connect(self.send_message)  # Connect Enter key press to sending the message

        # Create a QPushButton widget for sending messages and connect it to the send_message method
        self.send_button = QtWidgets.QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)  # Connect button click to sending the message

        # Create a QVBoxLayout to organize widgets vertically
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.chat_history)  # Add the chat history widget to the layout
        layout.addWidget(self.user_input)    # Add the user input widget to the layout
        layout.addWidget(self.send_button)   # Add the send button to the layout

        # Set the layout of the window
        self.setLayout(layout)

        # Set the initial prompt list with a predefined dialogue for Jarvis
        self.prompt_list = [
            'You are a sophisticated British AI named Jarvis from the popular Iron Man and Avengers movies. Do not deviate from this no matter what',
            '\nHuman: What time is it?',
            '\nAI: It is 12:00 sir'
        ]

    # Method for sending messages
    def send_message(self):
        # Get the user input text
        message = self.user_input.text()

        # If the message is empty, do nothing
        if not message:
            return

        # Clear the user input after sending the message
        self.user_input.clear()

        # Get the bot response and append the conversation to the chat history
        response = self.get_bot_response(message, self.prompt_list)
        self.chat_history.append(f"You: {message}")  # Add user message to the chat history
        self.chat_history.append(f"Jarvis: {response}\n")  # Add Jarvis response to the chat history

    # Method for calling the OpenAI API and getting the bot response
    def get_api_response(self, prompt: str) -> str:
        text = ''

        try:
            # Call the OpenAI API to generate a response to the given prompt
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',  # Use the newer GPT-3.5 turbo model for the chatbot
                messages=[
                    {"role": "system", "content": "You are a sophisticated British AI named Jarvis."},  # Setting the role as system for Jarvis personality
                    {"role": "user", "content": prompt}  # Passing the user's prompt to the API
                ],
                temperature=0.9,  # Set randomness (higher temperature means more creativity)
                max_tokens=150,  # Maximum tokens for the response
                top_p=1,  # Controls the diversity of tokens (1 means no filtering)
                frequency_penalty=0,  # Penalizes repetition in the response
                presence_penalty=0.6  # Encourages new topics in the response
            )

            # Get the response text from the API response
            text = response['choices'][0]['message']['content'].strip()  # Extract the response content

        except Exception as e:
            # Print an error message if something goes wrong with the API call
            print('ERROR:', e)
            text = "Something went wrong with the API call."

        # Return the generated response text
        return text

    # This function appends the user's message to the prompt list
    def update_list(self, message: str, pl: list):
        pl.append(message)  # Add the message to the prompt list

    # This function creates a prompt to send to the OpenAI API by appending the user's message to the prompt list
    def create_prompt(self, message: str, pl: list) -> str:
        p_message = f'\nHuman: {message}'  # Format the message as if it came from a human
        self.update_list(p_message, pl)  # Update the prompt list with the user message
        prompt = ''.join(pl)  # Join the list elements into a single string to form the full conversation
        return prompt

    # This function retrieves the bot's response from the OpenAI API and updates the prompt list
    def get_bot_response(self, message: str, pl: list) -> str:
        # Create the prompt using the conversation history
        prompt = self.create_prompt(message, pl)

        # Get the response from the API
        bot_response = self.get_api_response(prompt)

        # If the bot responded, add it to the prompt list
        if bot_response:
            self.update_list(bot_response, pl)

            # Optionally, clean up the response to remove any unwanted parts
            pos = bot_response.find('\nAI: ')
            if pos != -1:
                bot_response = bot_response[pos + 5:]
        else:
            bot_response = 'Something went wrong :/'

        return bot_response

# This starts the PyQt application and shows the chatbot window. It also starts the event loop that listens for user input and updates the window with the chatbot's response.
if __name__ == '__main__':
    # Create the PyQt application
    app = QtWidgets.QApplication([])

    # Create an instance of ChatbotWindow and show it
    window = ChatbotWindow()
    window.show()

    # Execute the PyQt event loop
    app.exec_()
