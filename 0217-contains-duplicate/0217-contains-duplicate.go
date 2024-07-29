func containsDuplicate(nums []int) bool {

    var maps = map[int]int{}
    for i, ind := range nums{
        maps[ind] = i
    }
    return len(nums) > len(maps)
    
}