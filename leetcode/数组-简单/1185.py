# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-25 13:47:56
@LastEditTime : 2019-12-25 13:50:57
@Description: 一周中的第几天-简单  https://leetcode-cn.com/problems/day-of-the-week
'''


import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_day_dict = {
            0:"Sunday",
            1:"Monday",
            2:"Tuesday",
            3:"Wednesday",
            4:"Thursday",
            5: "Friday",
            6:"Saturday"
        }
                
        anyday=datetime.datetime(year,month,day).strftime("%w")
        
        return week_day_dict[int(anyday)]
