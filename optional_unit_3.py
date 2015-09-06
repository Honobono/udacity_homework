#symmetric
def symmetric(p):
	n = len(p)
	for r in range(n):
		if len(p[r]) != n:
			return False
		for c in range(n):
			if p[r][c] == p[c][r]:
				pass
			else:
				return False

	return True


#mean
def list_mean(p):
    total = 0 
    for i in p:
	    total = total + i
	    mean = total / float(len(p))
    return mean
    






