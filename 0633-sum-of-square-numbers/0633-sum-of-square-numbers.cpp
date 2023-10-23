class Solution {
public:
    bool judgeSquareSum(int c) {
        long long i=0;
        long long j=int(sqrt(c));
        while(i<=j)
        {
            long long n=i*i + j*j;
            if (n ==c)
                return 1;
            else if (n>c)
                j-=1;
            else
                i+=1;
            
        }
        return 0;
        
    }
};