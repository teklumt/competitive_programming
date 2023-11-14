/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
   let num=true;
	return function(...args){
        if (num){
            num=false;
            return fn(...args);
        }
        else{
            num=0;
            return undefined;
        }

        
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
