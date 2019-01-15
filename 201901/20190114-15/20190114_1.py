# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-14 15:59:16
@LastEditTime: 2019-01-15 11:22:17
@Description: 决策树的python实现
'''

import csv
import pydotplus
import numpy as np
from collections import defaultdict


class Tree:
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
    return 1 - imp


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


def buildDecisionTree(rows, evaluationFunction=gini):
    currentGain = evaluationFunction(rows)
    column_length = len(rows[0])
    rows_length = len(rows)
    best_gain = 0.0
    best_value = None
    best_set = None

    for col in range(column_length - 1):
        col_value_set = set([x[col] for x in rows])
        for value in col_value_set:
            list1, list2 = splitDatas(rows, value, col)
            p = len(list1) / rows_length
            gain = currentGain - p * evaluationFunction(list1) - (1 - p) * evaluationFunction(list2)
            if gain > best_gain:
                best_gain = gain
                best_value = (col, value)
                best_set = (list1, list2)
    
    dcY = {f"impurity: {currentGain:.3f}, samples: {rows_length}"}

    if best_gain > 0:
        true_branch = buildDecisionTree(best_set[0], evaluationFunction)
        false_branch = buildDecisionTree(best_set[1], evaluationFunction)
        return Tree(col=best_value[0], value=best_value[1], true_branch=true_branch, false_branch=false_branch, summary=dcY)
    else:
        return Tree(results=calculateDiffCount(rows), summary=dcY, data=rows)


def prune(tree, miniGain, evaluationFunction=gini):
    if tree.true_branch.results == None: prune(tree.true_branch, miniGain, evaluationFunction)
    if tree.false_branch.results == None: prune(tree.false_branch, miniGain, evaluationFunction)

    if tree.true_branch.results != None and tree.false_branch.results != None:
        len1 = len(tree.true_branch.data)
        len2 = len(tree.false_branch.data)
        len3 = len(tree.true_branch.data + tree.false_branch.data)
        p = float(len1) / (len1 + len2)
        gain = evaluationFunction(tree.true_branch.data + tree.false_branch.data) - p * evaluationFunction(
            tree.true_branch.data) - (1 - p) * evaluationFunction(tree.false_branch.data)
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

# 画图部分

def plot(decisionTree):

    def toString(decisionTree, indent=''):
        if decisionTree.results != None:
            return str(decisionTree.results)
        else:
            szCol = 'Column %s' % decisionTree.col
            if szCol in dcHeadings:
                szCol = dcHeadings[szCol]
            if isinstance(decisionTree.value, int) or isinstance(decisionTree.value, float):
                decision = '%s >= %s?' % (szCol, decisionTree.value)
            else:
                decision = '%s == %s?' % (szCol, decisionTree.value)
            true_branch = indent + 'yes -> ' + toString(decisionTree.true_branch, indent + '\t\t')
            false_branch = indent + 'no  -> ' + toString(decisionTree.false_branch, indent + '\t\t')
            return (decision + '\n' + true_branch + '\n' + false_branch)

    print(toString(decisionTree))


def dotgraph(decisionTree):
    global dcHeadings
    dcNodes = defaultdict(list)

    def toString(iSplit, decisionTree, bBranch, szParent= 'null', indent=''):
        if decisionTree.results != None:
            lsY = []
            for szX, n in decisionTree.results.items():
                lsY.append('%s:%d' % (szX, n))
            dcY = {"name": "%s" % ', '.join(lsY), "parent": szParent}
            dcSummary = decisionTree.summary
            dcNodes[iSplit].append(['leaf', dcY['name'], szParent, bBranch, dcSummary['impurity'], dcSummary['samples']])
            return dcY

        else:
            szCol = 'Column %s' % decisionTree.col
            if szCol in dcHeadings:
                szCol = dcHeadings[szCol]
            if isinstance(decisionTree.value, int) or isinstance(decisionTree.value, float):
                decision = '%s >= %s' % (szCol, decisionTree.value)
            else:
                decision = '%s == %s' %(szCol, decisionTree.value)
            true_branch = toString(iSplit + 1, decisionTree.true_branch, True, decision, indent + '\t\t')
            flase_branch = toString(iSplit + 1, decisionTree.false_branch, False, decision, indent + '\t\t')
            dcSummary = decisionTree.summary
            dcNodes[iSplit].append([iSplit + 1, decision, szParent, bBranch, dcSummary['impurity'], dcSummaryp['samples']])
            return
        
    toString(0, decisionTree, None)
    lsDot = ['digraph Tree {',
             'node [shape=box, style="filled, rounded", color="black", fontname=helvetica] ;',
             'edge [fontname=helvetica] ;'
            ]
    
    i_node = 0
    dcParent = {}
    for nSplit, lsY in dcNodes.items():
        for lsX in lsY:
            iSplit, decision, szParent, bBranch, szImpurity, szSamples = lsX
            if type(iSplit) == int:
                szSplit = '%d-%s' % (iSplit, decision)
                dcParent[szSplit] = i_node
                lsDot.append('%d [label=<%s<br/>impurity %s<br/>samples %s>, fillcolor="#e5813900"] ;' % (i_node,
                decision.replace('>=', '&ge;').replace('?', ''), szImpurity, szSamples))
            else:
                lsDot.append('%d [label=<impurity %s<br/>samples %s<br/>class %s>, fillcolor="#e5813900"] ;' % (i_node, szImpurity, szSamples, decision))

            if szParent != 'null':
                if bBranch:
                    szAngle = '45'
                    szHeadLabel = 'True'
                else:
                    szAngle = '-45'
                    szHeadLabel = 'False'
                szSplit = '%d-%s' % (nSplit, szParent)
                p_node = dcParent[szSplit]
                if nSplit == 1:
                    lsDot.append('%d -> %d [labeldistance=2.5, labelangle=%s, headlabel="%s"] ;' % (p_node, i_node, szAngle, szHeadLabel))
                else:
                    lsDot.append('%d -> %d ;' % (p_node, i_node))
            i_node += 1
            lsDot.append('}')
            dot_data = '\n'.join(lsDot)
            return dot_data


def loadCSV(file):
    def convertTypes(s):
        s = s.strip()
        try:
            return float(s) if '.' in s else int(s)
        except ValueError:
            return s
    
    reader = csv.reader(open(file, 'rt', encoding='utf-8'))
    dcHeader = {}
    if bHeader:
        lsHeader = next(reader)
        for i, szY in enumerate(lsHeader):
            szCol = 'Column %d' % i
            dcHeader[szCol] = str(szY) 
    return dcHeader, [[convertTypes(item) for item in row] for row in reader]


bHeader = True
dcHeadings, trainingData = loadCSV('fishiris.csv')
decisionTree = buildDecisionTree(trainingData, evaluationFunction=gini)
result = plot(decisionTree)
prune(decisionTree, 0.4)
result = plot(decisionTree)
dot_data = dotgraph(decisionTree)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png("prune.png")