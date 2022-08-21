/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    
    
    let a = s.length -1;
    let b = 0;
    
    while (a != b ){
        
        if(b>a){
            break;
        }
        
        let c = s[b];
        s[b] = s[a];
        s[a] = c;
        
        b++;
        a--;
        
        
        
    }
   
    
    
    
    
    
};