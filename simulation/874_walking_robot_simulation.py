class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        pos = [0, 0]
        direction = [0, 1]
        od = defaultdict(bool)

        res = 0

        for i, j in obstacles:
            od[(i, j)] = True
        
        for command in commands:
            if command == -1:
                temp_x = direction[0]
                direction[0] = direction[1] if direction[0] == 0 else 0
                direction[1] = -temp_x if direction[1] == 0 else 0
            elif command == -2:
                temp_x = direction[0]
                direction[0] = -direction[1] if direction[0] == 0 else 0
                direction[1] = temp_x if direction[1] == 0 else 0
            else:
                # k is max 9, so negligable runtime for loop O(9)
                for i in range(1, command + 1):
                    new_x, new_y = pos[0] + direction[0], pos[1] + direction[1]
                
                    if od[(new_x, new_y)]:
                        break

                    pos = [new_x, new_y]
                    res = max(res, pos[0] ** 2 + pos[1] ** 2)
        
        return res