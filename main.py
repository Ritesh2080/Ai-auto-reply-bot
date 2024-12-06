import os
import random
import time

import google.generativeai as genai
import pyautogui
import pyperclip

api_key = os.environ.get("api_key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


# checks if the last message in the copied text is from the person who we are chatting 
# to ensure that we are not replying to out own message 
def is_last_message_from_sender(chat,sender_name="Meta"):
    messages = str(chat.strip().split("] ")[-1])
    if messages.startswith(sender_name):
        return True
    return False

# processes the copied text and returns a suitable response using google gemini ai
def ai_process(command):
    response = model.generate_content(command)
    text = list(response.text.split("\n"))
    responses_as_text = []
    print(response)
    for x in text:
        if x.startswith("* **Option"):
            parts = x.split("):** ")
            responses_as_text.append(parts[1])
        if "ritesh" in x:
            parts = x.split("ritesh: ")
            responses_as_text.append(parts[1])

    return random.choice(responses_as_text)

# clicking the chrome icon in the taskbar
pyautogui.moveTo(843,768)
pyautogui.moveTo(615,743)
pyautogui.click(615,743)
time.sleep(1)

while True:

    # to select from top left to bottom right
    # time.sleep(5)
    # pyautogui.moveTo(502,226)
    # pyautogui.dragTo(1302,674,duration=2.0,button='left')
    # pyautogui.hotkey('ctrl','c')
    # time.sleep(2)
    # pyautogui.click(619,734)  

    # to select from bottom right to top left
    pyautogui.moveTo(1302,674)
    pyautogui.dragTo(502,226,duration=2.0,button='left')
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    pyautogui.click(619,734) 

    chat = pyperclip.paste()


    if is_last_message_from_sender(chat):
        command = "Give me a proper response to given chat \n" + chat
        response =  ai_process(command)
        pyperclip.copy(response)
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pyautogui.press('enter')
