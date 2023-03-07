/**
 * @param {number[][]} graph
 * @return {number[][]}
 */

/*

    principle: deapth first search 
    base case: node + 1 == graph.length 

*/

var allPathsSourceTarget = function(graph) {
    let paths = getPath(graph, 0, [], [])
    return paths
};

/*
    graph: the graph
    node: current node
    path: current path
    paths: all paths
 */

function getPath(graph, node, path, paths) {
    for (var j = 0; j < graph[node].length; j++) {
        getPath(graph, graph[node][j], [...path, node], paths)
    }

    if (node + 1 == graph.length) paths.push([...path, node])

    return paths;
}