func twoSum(nums []int, target int) []int {
    var seen = make(map[int]int)
    for i, val := range nums{
        var dif = target - nums[i]
        if posi, okey1 := seen[dif];okey1{
            return []int{i,posi }
        }
        seen[val] = i
    }
    return []int{}
    
}