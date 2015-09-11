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

#numbers_in_lists
def numbers_in_lists(string):
    i = 0 #positioining of the integer in the string
    y = int(string[i]) #the first int
    result_list = [y] 
    sub_list = []
    
    for i in range(len(string)-1): #indexing range(len(string)) would be out of range.
        x = int(string[i+1]) #the int after the preceding int
        if x <= y:  
            sub_list.append(x)
        elif x > y: 
            y = x
            if len(sub_list) > 0: #list is not empty
                result_list.append(sub_list)
                sub_list = []
            result_list.append(x)
    if len(sub_list) > 0:
         result_list.append(sub_list)     

    return result_list
    
    
#frequency_analysis
def freq_analysis(message):
    n = len(message) #total number of chars in the msg
    i = 0 #occurence of each letter
    my_letters = "abcdefghijklmnopqrstuvwxyz"
    freq_list = [0.0] * 26 #create an empty list of [0.0,0.0,0.0,0.0...]
    for j in range(len(message)):
        char = message[j:j+1]
        freq_char = message.count(char) / float(n)
        freq_list[my_letters.find(char)] = freq_char #replace item in empty list with char frequency. 
    return freq_list






