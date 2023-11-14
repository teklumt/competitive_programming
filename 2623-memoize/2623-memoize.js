/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const store={};
    return function(...args) {
        const key=JSON.stringify(args);
        if (store[key]!==undefined){
            return store[key];
        }
        const res=fn(...args);
        store[key]=res;
        return res;
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */