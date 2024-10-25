class Solution(object):
    def removeSubfolders(self, folders):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folders.sort()
        result = [ folders[0] ]

        for i in range(1, len(folders)):
            last_folder = result[-1]
            last_folder += '/'

            if not folders[i].startswith(last_folder):
                result.append(folders[i])
        
        return result