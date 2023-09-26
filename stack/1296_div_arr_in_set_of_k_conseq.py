class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        freq_keys = freq.keys()
        freq_keys = sorted(freq_keys)
        
        stack = [ freq_keys[0] ]
        freq[freq_keys[0]] -= 1

        if freq[freq_keys[0]] == 0:
            del freq[freq_keys[0]]
            freq_keys.pop(0)

        while freq_keys:
            if len(stack) == k:
                stack = [ freq_keys[0] ]
                last_stack = freq_keys[0]
            else:
                last_stack = stack[-1] + 1
                if last_stack not in freq_keys:
                    return False
                else: 
                    stack.append(last_stack)

            index = freq_keys.index(last_stack)
            freq[last_stack] -= 1
            if freq[last_stack] == 0:
                del freq[last_stack]
                freq_keys.pop(index)
                
        if len(stack) != k:
            return False
        
        return True
            