class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        global rows, cols, og
        rows = len(image) 
        cols = len(image[0])
        og = image[sr][sc]

        def fill(sr, sc): 
            global rows, cols, og
            if sr < 0 or sr >= rows or sc < 0 or sc >= cols or image[sr][sc] != og: 
                return 
            
            image[sr][sc] = color 

            fill(sr + 1, sc) 
            fill(sr - 1, sc) 
            fill(sr, sc + 1) 
            fill(sr, sc - 1)

        if image[sr][sc] != color: 
            fill(sr, sc) 
            
        return image 