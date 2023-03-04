/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {

    let source = image[sr][sc]

    const dfs = (sr, sc) => {
        if (sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length || image[sr][sc] !== source)  {
            return
        }
        
        image[sr][sc] = color
        
        dfs(sr + 1, sc)   
        dfs(sr - 1, sc)   
        dfs(sr, sc + 1)   
        dfs(sr, sc - 1)      
    }

    if (source != color) dfs(sr, sc) 
    return image
};