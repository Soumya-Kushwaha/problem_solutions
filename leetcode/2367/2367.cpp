class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int visited[201] = {}, res = 0;
        for (int n : nums) {
            if (n >= 2 * diff)
                res += visited[n - diff] && visited[n - 2 * diff];
            visited[n] = true;
        }
        return res;
}
};
