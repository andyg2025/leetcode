from typing import Optional


class Node:
    def __init__(self, index, pre: Optional['Node'] =None, next: Optional['Node'] =None):
        self.index = index
        self.pre = pre
        self.next = next

class Circ:
    def __init__(self, node: Node):
        self.tail = node
        self.tail.pre = self.tail
        self.tail.next = self.tail

    def add(self, node: Node):
        node.next = self.tail.next
        node.pre = self.tail
        self.tail.next.pre = node
        self.tail.next = node
        self.tail = node

    def get_min_distance(self, node:Node, total_len:int):
        if self.tail.next == self.tail:
            return -1
        index = node.index
        pre_index = node.pre.index
        next_index = node.next.index
        pre_dis = (index+total_len-pre_index)%total_len
        next_dis = (next_index+total_len-index)%total_len
        return min(pre_dis, next_dis)

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        index_node = {}
        map = {}

        n = len(nums)
        for i in range(n):
            node = Node(i)
            index_node[i] = node
            if nums[i] in map:
                map[nums[i]].add(node)
            else:
                map[nums[i]] = Circ(node)
        
        result = []
        for q in queries:
            node = index_node[q]
            circ = map[nums[q]]
            dis = circ.get_min_distance(node, n)
            result.append(dis)
        
        return result
            
                