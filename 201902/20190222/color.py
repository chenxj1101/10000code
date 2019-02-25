# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-02-25 13:12:00
@Description: color.py
'''

import re
from utils import colorFormat


def colored(text, color=None, on_color=None, attr=None):
    if color is not None:
        text = re.sub(colorFormat.COLOR_REGEX + "(.*?)" + colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.COLORS[color], text)

    if on_color is not None:
        text = re.sub(colorFormat.HIGHLIGHTS_REGEX + "(.*?)" + colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.HIGHLIGHTS[on_color], text)

    if attr is not None:
        text = re.sub(colorFormat.ATTRIBUTES_REGEX + "(.*?)" + colorFormat.RESET_REGEX, r"\1", text)
        text = colorFormat.FMT_STR % (colorFormat.ATTRIBUTES[attr], text)

    return text + colorFormat.RESET