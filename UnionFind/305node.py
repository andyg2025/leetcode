class Node:
    def __init__(self, position: tuple[int, int]):
        self.position = position
        self.parent = None

class Solution:
    def get_parent(self, node: Node):
        while node.parent:
            node = node.parent
        return node

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        p_node = {}
        count = 0

        for x,y in positions:
            if (x,y) in p_node:
                result.append(count)
                continue

            new_node = Node((x,y))
            p_node[(x,y)] = new_node
            count += 1

            connected = set()

            for x1, y1 in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if x1<0 or x1>=m or y1<0 or y1>=n or (x1, y1) not in p_node:
                    continue

                node = p_node[(x1,y1)]
                parent = self.get_parent(node)
                connected.add(parent)
            
            count -= len(connected)
            result.append(count)

            for node in connected:
                node.parent = new_node
            
        return result