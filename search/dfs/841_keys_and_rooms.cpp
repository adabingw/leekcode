class Solution {
public:
    void dfs(int node, vector<vector<int>>& rooms, vector<bool>& visited) {
        if (visited[node]) return;
        
        visited[node] = true;

        for (auto i : rooms[node]) {
            dfs(i, rooms, visited);
        }

        return;
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n);

        dfs(0, rooms, visited);

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                return false;
            }
        }
        return true;
    }
};