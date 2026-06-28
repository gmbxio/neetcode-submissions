class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int>mp;
        for (int num: nums){
            mp[num]++;
        }
        for (int num: nums){
            if (mp[num] > 1) return 1;
        }
        return 0;
    }
};