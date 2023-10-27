class Solution {
public:
    int minMoves(vector<int>& nums) {
        long long leng=nums.size();
        long long minn=nums[0];
        long long summ=0;
        for (long long i=0;i<leng;i++){
            if (nums[i]<minn)
                minn=nums[i];
            summ+=nums[i];
        }
        return summ-minn*leng;    
    }
};
