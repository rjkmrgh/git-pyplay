
const functions = {
    isValid(s) {

        const mp = new Map();
        
        const strLetters = s.split('');
        strLetters.forEach(a => {
            if(mp.has(a)){
                mp.set(a, mp.get(a)+1);
            }
            else{
                mp.set(a, 1);
            }
        })
        let minVal = true;
        let mpValues = Array.from(mp.values()).sort();
        const len = mpValues.length;
        
        if (len === 1 ){
           return 'YES'
        }
        else if (len > 1 ){
            for(let i = 0; i <= len-1; i++) {
                const diff = mpValues[0] - mpValues[i];            
                if(diff === 0 ){
                    minVal = true;
                }
                else{
                    minVal = false;
                }
            }  
            if(!minVal){
                minVal = true;
                if(mpValues[0] === 1){
                    for(let i = 1; i < len-1; i++) {
                        const diff = mpValues[1] - mpValues[i];            
                        if(diff !== 0 ){
                            minVal = false;
                        }
                    }
                    if(len > 1 && mpValues[len-1] > 2 ){
                        const diff = mpValues[len -1] - mpValues[len -2];
                        if(diff === 0){
                            minVal = true;
                        }   
                        else{
                            minVal = false;
                        }
                    }
                }
                else{
                    for(let i = 0; i < len-2; i++) {
                        const diff = mpValues[0] - mpValues[i];            
                        if(diff !== 0 ){
                           minVal = false;
                        }
                    }  
                    if(minVal){
                        const diff = mpValues[len -1] - mpValues[len -2];
                        if(diff ===1){
                            minVal = true;
                        }   
                        else{
                            minVal = false;
                        }
                    }
                }
        
            }
        }
    
        
    
        if(minVal){        
            return 'YES';
        }
        else{
            return 'NO';
        }
    }
    
}

module.exports = functions;