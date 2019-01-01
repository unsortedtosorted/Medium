    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        r=""
        for x in (zip(*strs)):
            prev=None
            for y in x:
                if not prev:
                    prev=y
                    continue
                if prev!=y:
                    return r
            
            r=r+prev
        return r
