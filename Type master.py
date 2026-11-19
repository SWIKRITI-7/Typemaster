import time
import random

# ---------- COLORS AND DESIGN ----------

RESET = "\033[0m"
BOLD = "\033[1m"

PURPLE = "\033[95m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"

BG = "\033[40m"

def line():
    print(PURPLE + "═" * 60 + RESET)

def heading():
    print(BG + WHITE)
    print("\n")
    line()
    print(CYAN + BOLD + "             TYPEMASTER - TYPING TEST" + RESET)
    print(PURPLE + "             Measure Your Typing Speed" + RESET)
    line()


# ---------- PARAGRAPHS ----------

paragraphs = [
    "Python is a powerful programming language that is easy to learn.",
    "Practice makes progress and helps us improve our skills every day.",
    "Technology has changed the way people communicate and learn.",
    "Programming teaches us how to solve problems step by step.",
    "A good programmer writes clean and understandable code."
]


# ---------- TYPING TEST ----------

def typing_test():

    heading()

    text = random.choice(paragraphs)

    print(CYAN + BOLD + "\nYOUR PARAGRAPH:" + RESET)
    print(YELLOW + text + RESET)

    print("\n" + GREEN + "Press Enter when you are ready to start." + RESET)
    input()

    print(CYAN + BOLD + "\nStart Typing Below:" + RESET)

    start_time = time.perf_counter()

    typed_text = input(WHITE + "\n>>> " + RESET)

    end_time = time.perf_counter()

    # ---------- CALCULATIONS ----------

    time_taken = end_time - start_time
    minutes = time_taken / 60

    correct = 0

    for i in range(min(len(text), len(typed_text))):
        if text[i] == typed_text[i]:
            correct += 1

    errors = max(len(text), len(typed_text)) - correct

    if minutes > 0:
        wpm = (correct / 5) / minutes
    else:
        wpm = 0

    accuracy = (correct / max(len(text), len(typed_text))) * 100

    # ---------- RESULTS ----------

    print("\n")
    line()

    print(GREEN + BOLD + "                  YOUR RESULTS" + RESET)

    line()

    print(CYAN + "  Time Taken       : " + WHITE +
          str(round(time_taken, 2)) + " seconds")

    print(CYAN + "  Typing Speed     : " + GREEN + BOLD +
          str(round(wpm, 2)) + " WPM")

    print(CYAN + "  Accuracy         : " + YELLOW +
          str(round(accuracy, 2)) + "%")

    print(CYAN + "  Correct Characters: " + WHITE +
          str(correct))

    print(CYAN + "  Errors           : " + RED +
          str(errors))

    line()

    if wpm >= 50:
        print(GREEN + BOLD + "  Excellent typing speed!" + RESET)
    elif wpm >= 30:
        print(YELLOW + "  Good job! Keep practicing." + RESET)
    else:
        print(CYAN + "  Keep practicing to improve!" + RESET)

    line()


# ---------- MAIN PROGRAM ----------

while True:

    typing_test()

    choice = input(
        "\n" + PURPLE +
        "Do you want to try again? (yes/no): " +
        RESET
    ).lower().strip()

    if choice != "yes":
        print(GREEN + BOLD +
              "\nThank you for using TypeMaster!" + RESET)
        break