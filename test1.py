
def prcdnce(op):
	
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/':
		return 2
	return 0

def operations(a, b, op):
	
	if op == '+': return a + b
	if op == '-': return a - b
	if op == '*': return a * b
	if op == '/':
	    try:
	        n = a / b
	        return n
	    except ZeroDivisionError:
	        print ("you can not divide number by zero")


def calc(s):
    tokens=s
    values = []
	
    ops = []
    i = 0
	
    while i < len(tokens):
		
# For spacing
        if tokens[i] == ' ':
            i += 1
            continue
		
# append '(' in ops list
        elif tokens[i] == '(':
            ops.append(tokens[i])
		
#append value
        elif tokens[i].isdigit():
            val = 0
			
# check for consecutive digit
            while (i < len(tokens) and tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1
            values.append(val)
            i-=1
		
# calculate value within bracket
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(operations(val1, val2, op))
            ops.pop()
            
        else:
            while (len(ops) != 0 and prcdnce(ops[-1]) >= prcdnce(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(operations(val1, val2, op))
            ops.append(tokens[i])
            
        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(operations(val1, val2, op))
    return values[-1]

s=input()
print(calc(s))

