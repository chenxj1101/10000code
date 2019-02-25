# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-02-22 15:37:18
@LastEditTime: 2019-02-22 16:43:30
@Description: text2art-utils
'''

class colorFormat:
    COLORS = dict(
        list(
            zip(
                [
                    "grey",
                    "red",
                    "green",
                    "yellow",
                    "blue",
                    "magenta",
                    "cyan",
                    "white"
                ],
                list(range(30, 38))
            )
        )
    )

    HIGHLIGHTS = dict(
        list(
            zip(
                [
                    "on_grey",
                    "on_red",
                    "on_green",
                    "on_yellow",
                    "on_blue",
                    "on_magenta",
                    "on_cyan",
                    "on_white",
                ],
                list(range(40, 48))
            )
        )
    )

    ATTRIBUTES = dict(
        list(
            zip(
                [
                    "hold",
                    "dark",
                    "",
                    "underline",
                    "blink",
                    "",
                    "reverse",
                    "concealed"
                ],
                list(range(1, 9))
            )
        )
    )

    del ATTRIBUTES[""]

    RESET = "\033[0m"
    FMT_STR = "\033[%dm%s"
    RESET_REGEX = "\033\[0m"
    COLOR_REGEX = "\033\[(?:{:s})m".format("|".join(["%d" % v for v in COLORS.values()]))
    HIGHLIGHTS_REGEX = "\033\[?:{:s})m".format("|".join(["%d" % v for v in HIGHLIGHTS.values()]))
    ATTRIBUTES_REGEX = "\033\[?:{:s})m".format("|".join(["%d" % v for v in ATTRIBUTES.values()]))