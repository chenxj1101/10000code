# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-14 15:59:16
@LastEditTime: 2019-01-14 17:05:33
@Description: 决策树的python实现
'''

import csv
import pydotplus
import numpy as np
from collections import defaultdict


class tree:
    def __init__(self, value=None, true_branch=None, false_branch=None, results=None, col=-1, summary=None, data=None):
        self.value = value
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.results = results
        self.col = col
        self.summary = summary
        self.data = data


def calculateDiffCount(datas):
    results = {}
    for data in datas:
        if data[-1] not in results:
            results[data[-1]] = 1
        else:
            results[data[-1]] += 1
    return results


def gini(rows):

    length = len(rows)
    results = calculateDiffCount(rows)
    imp = 0.0
    for i in results:
        imp += (results[i] / length) * (results[i] / length)
    return 1- imp


def splitDatas(rows, value, column):

    list1 = []
    list2 = []
    if (isinstance(value, int) or isinstance(value, float)):
        for row in rows:
            if (row[column] >= value):
                list1.append(row)
            else:
                list2.append(row)
    else:
        for row in rows:
            if row[column] == value:
                list1.append(row)
            else:
                list2.append(row)
    
    return (list1, list2)


def buildDecisionTree(rows, evaluationFuncton=gini):
    currentGain = evaluationFuncton(rows)
    column_length = len(rows[0])
    rows_length = len(rows)
    best_gain = 0.0
    best_value = None
    best_set = None

    for col in range(column_length - 1):
        col_value_set = set(x[col] for x in rows)
        for value in col_value_set:
            list1, list2 = splitDatas(rows, value, col)
            p = len(list1) / rows_length
            gain = currentGain - p * evaluationFuncton(list1) - (1 - p) * evaluationFuncton(list2)
            if gain > best_gain:
                best_gain = gain
                best_value = (col, value)
                best_set = (list1, list2)
    
    dcY = {f"impurity: {currentGain:.3f}, samples: {rows_length}"}

    if best_gain > 0:
        true_branch = buildDecisionTree(best_set[0], evaluationFuncton)
        false_branch = buildDecisionTree(best_set[1], evaluationFuncton)
        return Tree(col=best_value[0], value=best_value[1], true_branch=true_branch, false_branch=false_branch, summary=dcY)
    else:
        return Tree(results=calculateDiffCount(rows), summary=dcY, data=rows)


def prune(tree, miniGain, evaluationFuncton=gini):
    if tree.true_branch.results == None: prune(tree.true_branch, miniGain, evaluationFuncton)
    if tree.false_branch.results == None: prune(tree.false_branch, miniGain, evaluationFuncton)

    if tree.true_branch.results != None and tree.false_branch.results != None:
        len1 = len(tree.true_branch.data)
        len2 = len(tree.false_branch_data)
        len3 = len(tree.true_branch.data + tree.false_branch.data)
        p = float(len1) / (len1 + len2)
        gain = evaluationFuncton(tree.true_branch.data + tree.false_branch.data) - p * evaluationFuncton(
            tree.true_branch) - (1 - p) * evaluationFuncton(tree.false_branch.data)
        if (gain < miniGain):
            tree.data = tree.true_branch.data + tree.false_branch.data
            tree.results = calculateDiffCount(tree.data)
            tree.true_branch = None
            tree.false_branch = None


def classify(data, tree):
    if tree.results != None:
        return tree.results
    else:
        branch = None
        v = data[tree.col]
        if isinstance(v, int) or isinstance(v, float):
            if v >= tree.value:
                branch = tree.true_branch
            else:
                branch = tree.false_branch
        else:
            if v == tree.value:
                branch = tree.true_branch
            else:
                branch = tree.false_branch
        return classify(data, branch)