#Longest Increasing sequences using Dynamic programming

def LongestIncreasingSequence():

    P = [10, 8, 12, 33, 60, 8, 72, 80, 88, 9]
    M= [1]
    M = M * len(P)
    print (P)

    for i in range(1, len(P)):
        for j in range (0, i):
            while j < i:
                if P[i] > P[j] and M[i] < M[j] + 1:
                    M[i] =  M[j] + 1
                j +=1

            
    mx = max(M)
    return mx

if __name__ == '__main__':
    print(LongestIncreasingSequence())
