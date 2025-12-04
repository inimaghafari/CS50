from pyfiglet import Figlet
import sys
from random import choice as choice_randomly
figlet = Figlet()


def main():
    if len(sys.argv) < 2 :
        no_parameter()

    elif sys.argv[1] in ("-f", "--font"):
        if len(sys.argv) != 3:
            sys.exit("Invalid usage")
        have_parameter()


    else:
        sys.exit("Invalid usage")

# Random font
def no_parameter():
    font = figlet.getFonts()
    random_font = choice_randomly(font)
    figlet.setFont(font = random_font)
    text = input("Input: ")
    rendered = figlet.renderText(text)
    print(rendered)

# Selected font
def have_parameter():

        font_name = sys.argv[2]

        if font_name not in figlet.getFonts():
            sys.exit("Invalid usage")

        figlet.setFont(font=font_name)
        text = input("Input: ")
        print(figlet.renderText(text))




main()
