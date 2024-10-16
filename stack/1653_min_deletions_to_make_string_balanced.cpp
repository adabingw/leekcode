class Solution {
public:

    // focus on removing 'ba' pairs
    // count and remove pairs with stack
    
    int minimumDeletions(string s) {
        int n = s.length();
        stack<char> st;
        int res = 0;

        for (int i = 0; i < n; i++) {
            if (!st.empty() && st.top() == 'b' && s[i] == 'a') {
                st.pop();
                res++;
            } else {
                st.push(s[i]);
            }
        }

        return res;
    }
};