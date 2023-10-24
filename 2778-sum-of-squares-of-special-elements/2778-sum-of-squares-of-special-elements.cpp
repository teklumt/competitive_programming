class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        long long res=0;
        long long n=nums.size();
        for(long long i=1;i<n+1;i++){
            if(n%i==0){
                res+=nums[i-1]*nums[i-1];
            }
        }
        return res;
        
        
    }
};