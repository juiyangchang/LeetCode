from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        ref: https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
        """

        targets = defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            targets[a] += [b]

        route, stack = [], ['JFK']

        for _ in range(len(tickets)+1):
            while targets[stack[-1]]:
                stack += [targets[stack[-1]].pop()]
            route += [stack.pop()]

        return route[::-1]
