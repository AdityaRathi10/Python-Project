import openai
import re
import os
import sys
import time

def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./8)

openai.api_key = "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"

model_engine = "text-davinci-002"
prompt_start = "You say:"

# Define function to generate response from GPT-2 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Define function to clean up user input
def clean_input(text):
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\d", "", text)  # Remove digits
    text = text.lower()  # Convert to lowercase
    text = text.strip()  # Remove leading/trailing whitespace
    return text

# Define main function to run chatbot
def run_chatbot():
    slowprint("\t\tWelcome to ChatGPT!\n")
    while True:
        slowprint("\nChatGPT")
        user_input = input(": ")
        user_input = clean_input(user_input)
        if user_input == "bye":
            slowprint("Goodbye!")
            break
        if user_input=="open chrome":
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        if user_input == 'exit' or user_input=="quit":
            quit()
        prompt = prompt_start + " " + user_input + "\nChatGPT:"
        response = generate_response(prompt)
        slowprint(response+"\n")

# Call main function to start chatbot
if __name__ == "__main__":
    run_chatbot()