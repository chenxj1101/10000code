# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-02-01 11:06:26
@LastEditTime: 2019-02-01 13:25:12
@Description: 克隆图
'''


import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def clone_graph1(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighbor_copy
                dic[node].neighbors.append(neighbor_copy)
                queue.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return node_copy


def clone_graph2(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighbor_copy
                dic[node].neighbors.append(neighbor_copy)
                stack.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return node_copy


def clone_graph(node):
    if not node:
        return
    node_copy = UndirectedGraphNode(node.label)
    dic = {node: node_copy}
    dfs(node, dic)
    return node_copy


def dfs(node, dic):
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighbor_copy = UndirectedGraphNode(neighbor.label)
            dic[neighbor] = neighbor_copy
            dic[node].neighbors.append(neighbor_copy)
            dfs(neighbor, dic)
        else:
            dic[node].neighbors.append(dic[neighbor])