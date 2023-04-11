import random
import time
import json
import torch
import os
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import speech_recognition as sr

def get_user_query():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Calibrating Microphone...") 
        r.adjust_for_ambient_noise(source,duration=0.5) 
        print("Listening...")
        r.energy_threshold = 900 
        r.pause_threshold = 1 
        audio = r.listen(source) 
    try: 
        print("Recognizing...") 
        query = r.recognize_google(audio,language='en-in') 
        print(f"User said: {query}\n") 
    except Exception as e: 
        print("Say that again please...") 
        return "None" 
    return query

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Nao"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"

    sentence = get_user_query()
    print("You :", sentence)
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                r = random.choice(intent['responses'])
                print(bot_name, ":", r)
                file_path = r"C:/Users/Dell/Downloads/New Text Document.txt"
                if os.path.isfile(file_path):
                    with open(file_path, "w") as file:
                        file.write(r)

    else:
        r = "I'm sorry. I do not understand."
        print(bot_name, ":", r)
        file_path = r"C:/Users/Dell/Downloads/New Text Document.txt"
        if os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write(r)

    time.sleep(7)