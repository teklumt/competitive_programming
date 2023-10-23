class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n<=0)return 0;
        else
            return log2(n)==int(log2(n));
    }
};