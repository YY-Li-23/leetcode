class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common=strs[0]
        for i in strs[1:]:
            while not i.startswith(common):
                common=common[:-1]
                if not common:
                    return ""

        return common
            