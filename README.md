# Groq CLI Chatbot

A command-line AI chatbot built with Python and the Groq API.

The application allows users to chat with an AI assistant directly through the terminal. Responses are displayed in real time using streaming, and the conversation history is maintained during the session.

## Demo

```text
Welcome to the AI chatbot!
Type 'exit' to close the application.

You: What is Python?
Assistant: Python is a high-level programming language...
```

## Features

- Command-line chat interface
- Real-time streaming responses
- Conversation history during the session
- Secure API key management with environment variables
- Input validation
- Basic error handling
- Colored terminal messages
- Exit command to close the application

## Technologies Used

- Python
- Groq API
- python-dotenv
- Colorama

## Project Structure

```text
groq-cli-chatbot/
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

The `.env` file is not included in the repository because it contains the private API key.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/groq-cli-chatbot.git
```

### 2. Enter the project folder

```bash
cd groq-cli-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the main project folder.

Use the `.env.example` file as a reference:

```env
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

Replace `your_api_key_here` with your own Groq API key.

Never publish or share your real API key.

## How to Run

Run the application with:

```bash
python chatbot.py
```

Type a message and press Enter to start chatting.

To close the application, type:

```text
exit
```

## Skills Demonstrated

This project demonstrates knowledge of:

- Python programming
- API integration
- Environment variables
- Streaming responses
- Functions
- Loops
- Conversation history
- Input validation
- Exception handling
- Git and GitHub

## Possible Business Applications

This project can be used as a foundation for:

- Customer support assistants
- Frequently asked questions chatbots
- Internal company assistants
- AI-powered terminal tools
- Custom AI integrations
- Automated response systems

## Future Improvements

- Add a graphical interface
- Add a web version
- Save conversation history
- Allow users to select different AI models
- Add automated tests
- Add a logging system
- Add Docker support

## About the Project

This is a personal portfolio project created to practice Python development, API integration and artificial intelligence applications.

## License

This project is available under the MIT License.
