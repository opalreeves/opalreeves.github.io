#Opal Reeves Assignment 10a (extra credit)
def file_sum(filename):
    total = 0.0
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:                
                total += float(line)
    
    with open('sum.txt', 'w') as out:
        out.write(str(total))