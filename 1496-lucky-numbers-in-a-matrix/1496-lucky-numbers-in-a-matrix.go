func min(arr []int) int {
    minVal := arr[0]
    for _, v := range arr {
        if v < minVal {
            minVal = v
        }
    }
    return minVal
}

func max(arr []int) int {
    maxVal := arr[0]
    for _, v := range arr {
        if v > maxVal {
            maxVal = v
        }
    }
    return maxVal
}
func luckyNumbers (matrix [][]int) []int {

    m, n := len(matrix), len(matrix[0])

    // var res = []int{}
    var transponse [][]int = make([][]int, n)
    for i := range transponse {
        transponse[i] = make([]int, m)
    }

    for  i := 0; i < m; i++ {
        for j := 0; j < n; j++{
            transponse[j][i] = matrix[i][j]

        }
    }

    for  i := 0; i < m; i++ {
        for j := 0; j < n; j++{
            if matrix[i][j] == min(matrix[i]) && matrix[i][j] == max(transponse[j]){
                // res = append(res, matrix[i][j])
                return  []int{matrix[i][j]}
            }

        }
    }
    return []int{}




    
}