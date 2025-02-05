from heapq import heappop, heappush


def minInterval(intervals, queries):
    ans = [-1] * len(queries)

    intervals.sort()
    qidxs = list(range(len(queries)))
    qidxs.sort(key=lambda i: queries[i])

    k = 0
    ivals = []
    for i in qidxs:
        q = queries[i]

        while ivals and ivals[0][2] < q: heappop(ivals)

        while k < len(intervals) and intervals[k][0] <= q:
            if intervals[k][1] >= q:
                heappush(ivals, (intervals[k][1] - intervals[k][0] + 1, intervals[k][0], intervals[k][1]))
            k += 1

        if ivals:
            ans[i] = ivals[0][0]

    return ans


print(minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))
