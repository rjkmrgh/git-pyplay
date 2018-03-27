## Subset Sum Problem

def SubSetSum(A, S, N):

    M = [[False for _ in range(S+1)] for _ in range(N)]

    for i in range(len(A)):
        for j in range(0,S+1):
            if j == A[i]:    
                M[i][j] = True
            elif j == 0:    
                M[i][j] = True
            elif j - A[0] < 0:    
                M[i][j] = False
                
            else:
                if j < A[i]:
                    M[i][j] = M[i-1][j]
                elif j == A[i]:
                    M[i][j] = True                
                else:
                    M[i][j] = M[i-1][j-A[i]] or M[i-1][j]

    return M[-1][-1]


#Sum
S= 11

#Numbers Subset
A = [2, 3, 7, 8, 10]

N = len(A)

if __name__ == '__main__':
    if SubSetSum(A, S, N):
        print('There is a subset of the given set with sum {} equal to given sum.'.format(S))
    else:
        print('There is no subset of the given set with sum {} equal to given sum.'.format(S))
    
