import collections

class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']

        print(targets)

        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]