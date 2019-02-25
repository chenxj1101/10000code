# -*- coding: utf-8 -*-

#!/usr/bin/env python
# coding=UTF-8
'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: 文本转艺术字
@Date: 2019-02-25 13:26:02
'''

import random
import re
from pyfiglet import Figlet, FigletFont
from color import colored
from utils import colorFormat

DEFAULT_FONT = "ghost"
font_list = FigletFont.getFonts()
color_dict = {value: key for key, value in colorFormat.COLORS.items()}


def lf():
    return random.sample(font_list, 25)


def rd(text, on_color=None, attr=None, width=80, justify='center'):
    rand_int = random.randint(1, len(font_list)+1)
    rand_color = color_dict.get(random.randint(30, 38))

    rand_font = font_list[rand_int]
    print(f"Random font is : {rand_font}")
    f = Figlet(
        font=rand_font, width=width, 
        justify=justify
    )
    r = f.readerText(text)
    return colored(r, rand_color, on_color, attr)

def gt(text, font=DEFAULT_FONT,color="magenta", on_color=None, attr=None, widt=80, justify="center"):
    f = Figlet(
        font, width=width:
            justify=justify
    )
    r = f.renderText(text)
    return colored(r, color, on_color, attr)


def h():
    doc = """
            Usage:
                text2art lf  # Random display of 25 fonts
                text2art rd text [--on_color] [--attr] [--width] [--justify]
                text2art gt text [--font] [--color] [--on_color] [--attr] [--width] [--justify]
            
            available text colors:
                red, green, yellow, blue, magenta, cyan, white.
            available text highlights:
                on_red, on_green, on_yellow, on_blue, on_magenta, 
                on_cyan,on_white.
            available attributes:
                bold, dark, underline, blink, reverse, concealed.
            width: Setting the size of the terminal output font,type is int.
            justify: Setting the location of the terminal output font.
            available parameter: left, enter, right.
          """
    print(doc)

def main():
    init(autoreset=True)
    fire.Fire()


if __name__ == "__main__":
    main()