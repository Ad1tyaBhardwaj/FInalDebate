# Debate Master

## Overview

Debate Master is a Streamlit-based web application that allows users to engage in debates with an AI assistant powered by OpenAI's GPT-3.5 Turbo model. The AI assistant can provide responses to user statements and engage in a debate on a given topic with adjustable difficulty levels.

## How it Works

### AI Assistant
The AI assistant uses the OpenAI GPT-3.5 Turbo model for generating responses. It receives user statements, formulates counterarguments based on the given topic, and responds according to the specified difficulty level.

### Configuration
Debate Master provides a simple user interface to configure the AI assistant:
- Users can enter the topic for the debate.
- Users can set the difficulty level on a scale of 0 to 10.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/debate-master.git

2. Install the required Python libraries:
   ```python
   pip install streamlit openai pyttsx3 langchain gtts

3. Set up your OpenAI API key:
   Obtain your OpenAI API key by signing up for an account on the OpenAI platform.
   Create a file named .env in the project directory and add your API key:
   
   ```python
   OPENAI_API_KEY=your_openai_api_key

4. Run the application:
   ```python
   streamlit run clone.py

5. Access the web application in your browser by navigating to http://localhost:8501.


The web app should be accessible in your browser at `http://localhost:8501`.

## Usage

- Launch the application by running the Streamlit app as instructed in the installation section.
- Configure the AI assistant by entering the debate topic and selecting the difficulty level in the sidebar.
- Interact with the AI assistant by typing your statements in the chat input box.
- The AI assistant will provide responses based on the topic and difficulty level.

## Acknowledgments

- Debate Master utilizes the OpenAI GPT-3.5 Turbo model for generating responses.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

## Declaration

This codebase for Debate Master was primarily developed during Hackout 2023. While certain components and ideas were created during the hackathon, it's important to note that some parts of the project were either pre-built or based on prior work. To provide transparency, the codebase includes the following components:

- **Hackathon Development:** The following components were developed from scratch or significantly modified during the hackathon:
  - Chat functionality for user interaction with the AI assistant.
  - Integration with OpenAI's GPT-3.5 Turbo model for generating responses.
  - The Streamlit web application for user interaction.

- **Pre-built Components:** The project may have utilized pre-existing libraries, frameworks, or code for specific functionalities. These pre-built components include:
  - Streamlit: This is the main framework for building the web application.
  - OpenAI GPT-3.5 Turbo: You're using OpenAI's GPT-3.5 Turbo model for generating responses.
  - pyttsx3: This library is used for text-to-speech functionality, which is part of your application.
  - gtts (gTTS): This library is also used for text-to-speech functionality.
  - dotenv: Used for loading environment variables from a .env file.

We believe in the spirit of transparency and want to acknowledge any pre-existing work that contributed to this project. Our goal was to create a meaningful project within the constraints of the hackathon while being open about its development process.

---

Feel free to customize the `README.md` file further to add more details, information, or sections specific to your project's requirements.



