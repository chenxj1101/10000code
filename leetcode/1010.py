# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-10 09:51:21
@LastEditTime: 2019-12-10 13:46:53
@Description: 总持续时间可被 60 整除的歌曲-简单  https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        
        from collections import defaultdict
        d = defaultdict(int)
        
        res = 0
        for t in time:
            residue = (60 - t) % 60
            if residue in d:
                res += d[residue]
                
            d[t] += 1
        
        return res