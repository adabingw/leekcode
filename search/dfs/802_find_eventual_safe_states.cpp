class Solution {
public:

    bool safe(vector<vector<int>>& graph, vector<bool>& visit, vector<bool>& inStack, int node) {
        if (inStack[node]) return true;
        if (visit[node]) return false;

        visit[node] = true;
        inStack[node] = true;

        for (auto neigh: graph[node]) {
            if (safe(graph, visit, inStack, neigh)) return true;
        }

        inStack[node] = false;
        return false;
    }

    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<bool> visit(n), inStack(n);
        vector<int> res;

        for (int i = 0; i < n; i++) {
            safe(graph, visit, inStack, i);
        }

        for (int i = 0; i < n; i++) {
            if (!inStack[i]) res.push_back(i);
        }

        return res;
    }
};