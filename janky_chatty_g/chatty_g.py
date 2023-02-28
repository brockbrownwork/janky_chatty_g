import pyautogui
import time
import webbrowser

def extract_chat_history(input_string):
    # Split the string into lines
    lines = input_string.split('\n')
    
    # Remove the first two lines
    del lines[:2]
    
    # Find the index of the line containing "Regenerate response" and "New chat"
    start_index = 0
    end_index = -1
    for i, line in enumerate(lines):
        if "Regenerate response" in line:
            end_index = i
    
    # Return the resulting string
    if start_index >= 0 and end_index >= 0:
        return '\n'.join(lines[start_index:end_index])
    else:
        return ""

# Read the input string from a file
with open("test.txt", "r") as f:
    input_string = f.read()

# Process the input string and print the result
result = extract_chat_history(input_string)
print(result)
input("")

webbrowser.open("https://chat.openai.com/chat")

# Wait for 5 seconds before starting the automation
time.sleep(5)

# Find and click the "new_chat.png" button
new_chat_button = pyautogui.locateOnScreen('new_chat.png')
if new_chat_button is not None:
    pyautogui.click(new_chat_button)

# Wait for 2 seconds before proceeding
time.sleep(2)

# Find and click the "input_text.png" button
input_text_button = pyautogui.locateOnScreen('input_text.png')
if input_text_button is not None:
    pyautogui.click(input_text_button)

# Wait for 2 seconds before proceeding
time.sleep(2)

# Type "hello world!" and press Enter
pyautogui.write('hello world!')
pyautogui.press('enter')

# Find and click the "regenerate_response.png" button
regenerate_response_button = pyautogui.locateOnScreen('regenerate_response.png')
while regenerate_response_button is None:
    regenerate_response_button = pyautogui.locateOnScreen('regenerate_response.png')

time.sleep(0.1)

# Find and click the "input_text.png" button
input_text_button = pyautogui.locateOnScreen('input_text.png')
if input_text_button is not None:
    pyautogui.click(input_text_button)

# Wait for 2 seconds before proceeding
time.sleep(2)

# Type "test successful! :)" and press Enter
pyautogui.write('test successful! :)')
pyautogui.press('enter')
