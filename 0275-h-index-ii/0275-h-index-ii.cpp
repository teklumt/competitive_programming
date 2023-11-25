class Solution {
public:
    int hIndex(vector<int>& citations) {
        int res=0;
        int count=1;
        for (int i=citations.size()-1;i>=0;i--){
            if(citations[i]>=count){
                res++;
                count++;
            }
            else{
                break;
            }
        }
        return res;
        
    }
};