class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = format(x, 'b')
        by = format(y, 'b')

        max_len = max(len(bx), len(by))
        x_l = list(bx.zfill(max_len))
        y_l = list(by.zfill(max_len))

        diff = sum(a != b for a, b in zip(x_l, y_l))
        return diff