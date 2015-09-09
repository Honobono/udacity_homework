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
    






