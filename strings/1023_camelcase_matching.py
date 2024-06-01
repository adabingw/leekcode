class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        result = [ True ] * len(queries)

        for index, query in enumerate(queries):
            upper_pattern = []
            for p1 in pattern:
                if p1.isupper():
                    upper_pattern.append(p1)

            upper_query = []
            for q1 in query:
                if q1.isupper():
                    upper_query.append(q1)
            
            if upper_pattern != upper_query:
                result[index] = False
                continue
                    
            p = 0
            q = 0
            while q < len(query) and p < len(pattern):
                if query[q].isupper():
                    if pattern[p].isupper() and pattern[p] == query[q]:
                        q += 1
                        p += 1
                    else:
                        result[index] = False
                        break
                elif query[q].islower() and pattern[p].isupper():
                    while query[q] != pattern[p]:
                        if query[q].isupper() and query[q] != pattern[p]:
                            result[index] = False
                            break
                        q += 1
                        if q >= len(query):
                            result[index] = False
                            break
                    q += 1
                    p += 1
                elif query[q].islower() and pattern[p].islower():
                    while query[q] != pattern[p]:
                        q += 1
                        if q >= len(query) or query[q].isupper():
                            result[index] = False
                            break
                    q += 1
                    p += 1
                
                if p >= len(pattern):
                    for i in range(q, len(query)):
                        if query[i].isupper():
                            result[index] = False
                            break

        return result