class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
        
        for source in graph:
            graph[source].sort(reverse=True)

        stack = ['JFK']
        result = []

        print(graph)

        while stack: 
            print(stack[-1], graph[stack[-1]])
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
                print("- ", stack[-1], graph[stack[-1]])
            else: 
                result.append(stack.pop())
        
        return result[::-1]
