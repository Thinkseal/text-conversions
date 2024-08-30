import logging
import pyperclip


logging.basicConfig(filename='output.txt', level=logging.INFO, format='')

i = 0

def output_converted(case, text):
    if case == 1:
        converted_text = text.upper()
    elif case == 2:
        converted_text = text.lower()
    else:
        print("Something went wrong.")
        error = 1
        break
    print(f"The result is: {converted_text}")
    pyperclip.copy(converted_text)
    with open('output.txt', 'a') as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I added the converted text into a file called output.txt, if it's easier to copy from there.")

def prompt_redo():
    if error == 1: 
        redo = str(input("Restart? (y/n) "))
    else:
        redo = str(input("Continue? (y/n) "))
    if redo == "y":
        i += 1
        error = 0
    elif redo == "n":
        break

print("At any time, type EXIT to stop. ")
while i < 1:
    mode = int(input("Type 1 for uppercase, 2 for lowercase. "))
    text_input = str(input("What would you like to fully uppercase/lowercase? "))

    if mode == 1:
        output_converted(mode, text_input)
        prompt_redo()
    elif mode == 2:
        output_converted(mode, text_input)
        prompt_redo()