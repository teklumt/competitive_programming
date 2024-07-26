class Solution {
  List<int> twoSum(List<int> nums, int target) {
    
    var seen = new Map();
    for(var i = 0; i <= nums.length; i++){
        if(seen.containsKey(target - nums[i])){
            return [i, seen[target - nums[i]]];
        }
        seen[nums[i]] = i;
    }
    return [];
    
  }
}