class Solution {
public:
    bool isPalindrome(int x) {
        vector<char>mydata;
        string data=to_string(x);
        for(int i=0;i<data.length();i++){
            mydata.push_back(data[i]);
        }
        for (int i=0,j=mydata.size()-1;i<mydata.size(),j>0;i++,j--){
            if (mydata[i]!=mydata[j])return false;
        }
        return true;
        
    }
};