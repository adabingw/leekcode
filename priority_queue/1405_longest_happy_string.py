class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> pq;
        if (a > 0) pq.push({ a, 'a' });
        if (b > 0) pq.push({ b, 'b' });
        if (c > 0) pq.push({ c, 'c' });

        string res = "";

        while (!pq.empty()) {
            pair<int, char> p = pq.top();
            pq.pop();
            int count = p.first;
            char character = p.second;

            if (res.length() >= 2 && res[res.length() - 1] == character && res[res.length() - 2] == character) {
                if (pq.empty()) break;

                pair<int, char> temp = pq.top();
                pq.pop();

                res += temp.second;
                if (temp.first - 1 > 0) {
                    pq.push({ temp.first - 1, temp.second });
                }
            } else {
                count--;
                res += character;
            }

            if (count) pq.push({ count, character });
        }

        return res;

    }
};