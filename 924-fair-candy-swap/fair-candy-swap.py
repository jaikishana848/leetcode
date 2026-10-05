class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        a = sum(aliceSizes)
        b = sum(bobSizes)

        diff = (b - a) // 2

        for x in aliceSizes:
            if x + diff in bobSizes:
                return [x, x + diff]