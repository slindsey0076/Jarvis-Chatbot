
# Jarvis Chatbot: Bringing Iron Man's AI Assistant to Life

Jarvis is a Python-based chatbot inspired by the AI assistant from the Marvel universe. The chatbot uses the OpenAI API to generate conversational responses, making it a useful virtual assistant for casual conversations or handling basic user queries. This project showcases the potential of chatbots as engaging tools to assist users with daily tasks and provide general conversation.

## Features

- **Conversational Abilities**: Jarvis can handle basic conversational scenarios, such as greetings, answering questions, and responding to user inputs.
- **Error Handling**: It can detect and respond to invalid data, providing clear error messages to help the user correct their input.
- **Extensible Design**: The chatbot is built with future enhancements in mind. Additional features can be integrated seamlessly.
- **Easy to Use**: Jarvis provides clear prompts and responses, making it simple for users to interact with.

## Installation

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your system.
2. **Install required Python packages**: Install the necessary libraries by running:

```bash
pip install openai PyQt5
```

### OpenAI API Key

Jarvis uses OpenAI to generate responses. To run the chatbot, you need an API key from OpenAI:

1. Go to [OpenAI](https://beta.openai.com/signup/) and sign up for an API key.
2. Once you have the key, open the `Chatbot.py` file and replace the placeholder in the following line with your key:

```python
openai.api_key = 'your-api-key-here'
```

## Running the Chatbot

1. Clone this repository:

```bash
git clone https://github.com/yourusername/jarvis-chatbot.git
cd jarvis-chatbot
```

2. Run the chatbot using Python:

```bash
python Chatbot.py
```

3. Once launched, the chatbot window will open. You can type in your questions or commands, and Jarvis will respond.

## Project Structure

- `Chatbot.py`: Main Python script containing the chatbot implementation.
- `README.md`: Project description and instructions (this file).

## Technologies Used

- **Python**: The core programming language used.
- **OpenAI API**: Used to generate responses based on the user's input.
- **PyQt5**: Python library used to build the graphical user interface for the chatbot.
  
## Challenges Faced

During development, I encountered several challenges:
- **API Integration**: Initial issues with the OpenAI prompt response, which required debugging and corrections.
- **Outdated Libraries**: Initially planned to use ChatterBot, but it was deprecated, leading to switching to the OpenAI API.

