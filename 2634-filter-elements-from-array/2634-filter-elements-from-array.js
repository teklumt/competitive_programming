/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res=[];
    for (let i=0;i<arr.length;i++){
        const num=fn(arr[i],i);
        if(num){
            res.push(arr[i]);
        }
        
    }
    return res;
};