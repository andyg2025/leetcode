class Solution:

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islands = []
        result = []
        
        for r, c in positions:
            newisland = set()
            removed = []
            print(islands)
            for island in islands:
                if (r,c) in island or (r-1>=0 and (r-1, c) in island) or (r+1<m and (r+1, c) in island) or (c-1>=0 and (r, c-1) in island) or (c+1<n and (r, c+1) in island):
                    newisland |= island
                    removed.append(island)

            for island in removed:
                islands.remove(island)

            newisland.add((r,c))
            islands.append(newisland)
            result.append(len(islands))

        return result
