#symmetric
def symmetric(p):
	n = len(p)
	for r in range(n):
		if len(p[r]) != n:
			return False
		for c in range(n):
			if p[r][c] != p[c][r]:
				return False
	return True
#symmetric-2nd solution
def symmetric(p):
	for i in range(len(p)):
    		for j in range(len(p)):
        		if p[i][j] != p[j][i]:
            		return False
	return True


#mean
def list_mean(p):
    total = 0 
    for i in p:
	    total = total + i
	    mean = total / float(len(p))
    return mean
    
#antisymmetric
def antisymmetric(A):
    for i in range(len(A)): # i starts to loop from 0 to 2
        for j in range(len(A)): # j starts to loop from 0 to 2
            if A[i][j] != -A[j][i]:
                return False
    return True
    
    
#identity_matrix
 # A[0][0] == 1 or A[0][-1] == 1
 # A[1][1] == 1 or A[1][-2] == 1
 # A[2][2] == 1 or A[2][-3] == 1
 # A[3][3] == 1 or A[3][0] == 1
 # index of any other element should be 0 
 
def is_identity_matrix(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
        if matrix[i][i] != 1: # do not include matrix[i][-i] != 1
            return False
        for j in range(len(matrix)):
            if matrix[i][j] != 0 and i != j:
                return False
    return True

#






