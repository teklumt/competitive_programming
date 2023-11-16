class Solution {
public:
    bool isThree(int n) {
        int count=0;
        for (int i=1;i<n+1;i++){
            if( n%i==0){
                if (count<3)
                    count+=1;
                else
                    return false;
            }
            
        }
        if(count==3)
                return true;
            else 
                return false;
        
    }
};
