from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) not in [1, 3]:
        # print(sys.argv[1])
        # print(type(sys.argv[1]))
        # print(len(sys.argv))
        sys.exit("Invalid usage")
elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")



phrase = input("Input: ")

if len(sys.argv) == 1:
        figlet.setFont(font=choice(fonts))
        print(figlet.renderText(phrase))
else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(phrase))







