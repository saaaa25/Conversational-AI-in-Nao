# Conversational AI in Nao
This project contains the necessary files to create a conversational AI using Nao, a humanoid robot, and various software tools such as UiPath, Python, and NLTK. The AI is capable of understanding and responding to natural language queries and commands.

## Files included
chat.py: Python file containing the code to generate answers for user queries.
intents.json: JSON file containing tags and replies for various intents.
model.py: Python file containing the code for the neural network model.
nltk_utils.py: Python file containing the code for natural language processing.
train.py: Python file containing the code to train the model on the intents.json file.
UiPath File: UiPath file for putting generated answers into choreography.

## How to use
To use this conversational AI, follow these steps:

- Train the model by running train.py. This will create a new file called data.pth which will contain the trained neural network model.
- Open chat.py and make sure that the path to the data.pth file is correct.
- Run chat.py. This will start the chatbot.
- Type a query or command into the chatbot and press Enter.
- The chatbot will generate a response based on the trained model and the intents.json file.

To use the UiPath file for putting generated answers into choreography, follow these steps:

- Open UiPath.
- Open the included UiPath file.
- Run the UiPath file.
- The generated answers will be put into the choreography.

## Dependencies
This project requires the following dependencies:

- Python 3
- Python 2
- PyTorch
- NLTK
- UiPath





