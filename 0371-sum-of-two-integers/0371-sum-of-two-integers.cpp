class Solution {
public:
    int getSum(int a, int b) {
        int carry = 0;
        while (b  != 0){
            carry = (a & b) << 1;
            a ^= b;
            b = carry;
                
        }
        return a;
        
    }
};