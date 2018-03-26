
N = int(input())

S=[]

S = [input() for _ in range(N)]

#print(S)

dt = {x:0 for x in range(1,30)}

for ss in S:
    if ss.startswith('G'):
        count = 2
    else:
        count = 1
    nlist = [int(s) for s in ss.split() if s.isdigit()]
    for x in nlist: 
        try:
            dt[x] +=count
        except:
            pass    

maxVal =dt[19]

if maxVal < dt[20]:
    maxVal = dt[20]
    
isDate = True

for k, x in dt.items():    
    if k != 19 and k !=20 and x >= maxVal:            
        isDate = False
           break
        
        
if isDate:
    print('Date')
else:
    print('No Date')
