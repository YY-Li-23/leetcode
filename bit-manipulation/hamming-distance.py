class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_1= list(format(x, '04b'))
        y_1= list(format(y, '04b'))
        diff = sum(x != y for x, y in zip(x_1, y_1))
        return diff
