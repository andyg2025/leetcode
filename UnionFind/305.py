class Solution:   
    def numIslands2(self, m, n, positions):
        res = []
        count = 0
        union = {}

        # define the find function like this is because: to deal with the merged island
        # if two island is merged, we don't need to modify each value of the position, like the number of island the position belong
        # instead, we only modify the value of the root island
        # for example, all the position point to the root position, and normally, the root position point to it self.
        # but when two islands is merged, we modify one root's value, and let it point to other root.
        # This find function is actually deal with it, the root function may modify more than once, like a linked list, from one root to other
        # but when the value == position itself, it means this is the true root.
        # time complexity is like the deapth of the root layer, which should be like log(n)
        # so the totally time complexity is like l*log(n*m), l=len(positions)

        def find(p):
            while p != union[p]:
                p = union[p]
            return p

        for x, y in positions:
            p = (x, y)

            # p already appear before
            if p in union:
                res.append(count)
                continue

            # assue it is a new island
            union[p] = p
            count += 1
            
            # what the fuck of arr?
            arr = set()

            # check if connected
            for r, c in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
                if r < 0 or c < 0 or r >= m or c >= n or (r, c) not in union:
                # if not connected, continue
                    continue

                # if connected, find the position of the connected node, which is should be the root?
                root = find((r, c))
                # add the root into a arr, why?
                arr.add(root)
            
            # reduce the num of the root that connected to the (r,c)?
            count -= len(arr)

            if arr:
                root = arr.pop()
                for a in arr:
                    union[a] = root
                union[p] = root
            res.append(count)
        return res