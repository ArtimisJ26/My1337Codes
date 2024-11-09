class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = []
        N = len(arr)
        for idx, x in enumerate(arr):
            n = len(x)
            y = "#".join([arr[i] for i in range(N) if i != idx])
            tmp = None
            for t in range(1, n + 1):
                for l in range(0, n - t + 1):
                    c = x[l:l+t]
                    if c not in y:
                        if tmp is None:
                            tmp = c
                        else:
                            tmp = min(tmp, c)
                if tmp is not None:
                    res.append(tmp)
                    break
            if tmp is None:
                res.append("")
        return res
                        
                    
                    
                