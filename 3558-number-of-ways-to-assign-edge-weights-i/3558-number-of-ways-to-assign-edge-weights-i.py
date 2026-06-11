class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque([(1, 0, -1)]) # (node,lvl, par)
        mxlvl = 0
        while q:
            node, lvl, par = q.popleft()
            mxlvl = max(mxlvl, lvl)
            for nei in adj[node]:
                if nei != par: q.append((nei, lvl + 1, node))

        # all = pow(2, mxlvl, MOD)
        # Odd = (All * Pow(2, -1, MOD)) % MOD
        # return odd
        return pow(2, mxlvl - 1, MOD)