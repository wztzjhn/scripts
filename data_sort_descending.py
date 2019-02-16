#!/usr/bin/python
import sys
import numpy as np
num_argv = len(sys.argv)

print_blank = 0
print '---------- mergesort data in descending order ----------'
if ( num_argv<3 ):
    sys.exit("Usage: data_sort filename key1 [key2] ...")
elif ( sys.argv[1]=='--help' ):
    sys.exit("Usage: data_sort filename key1 [key2] ...")
else:
    filename=sys.argv[1]
    keys=sys.argv[2:]
    num_keys=len(keys)
    print "keys used for sorting: ",keys

readfile = open(filename, "r")
data = [line.split() for line in readfile]
readfile.close()

if ( data[0][0][0]!='#' ):
    print 'data[0][0]:\t', data[0][0]
    sys.exit("Check if your 1st line starts with #?")

row_total = len(data)
row_begin = 2
row_end   = row_total-1
col_begin = 0
col_end   = len(data[row_begin])-1
col_keys  = []
for key in keys:
    col_keys.append(data[row_begin-1].index(key))
print 'col_keys-1:\t\t',col_keys
#if data[row_begin-1].count('ERROR(TBRMV)')>0:
#    col_error=data[row_begin-1].index('ERROR(TBRMV)')
#else:
#    col_error=-1

# function used to check if the argument string can be converted into float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# remove comment lines and blank lines
maxlen = len(data[1])
for row in range(row_end,row_begin-1,-1):
    if (len(data[row]) > maxlen):
        maxlen = len(data[row])
    if ( not(data[row]) ):
        del data[row]
    elif ( data[row][0][0]=='#' or not(is_number(data[row][col_keys[0]])) or not(is_number(data[row][col_keys[num_keys-1]])) ):
        del data[row]
#    elif ( col_error!=-1 and float(data[row][col_error])>1.0 ):
#        print "removing line with large errorbar in file "+filename+", error="+data[row][col_error]
#        del data[row]
row_total = len(data)
row_begin = 2
row_end   = row_total-1

dt = []
for term in data[1]:
    if term in keys:
        dt.append((term,float))
    else:
        dt.append((term,'S30'))
if maxlen > len(data[1]):
    dt.append(('__XleftXoverX__',np.str_,(maxlen-len(data[1]))*30))

data_tbs = []
for row in range(row_begin,row_end+1):
    val = []
    for col in range(0,len(data[row])):
        if col in col_keys:
            val.append(-float(data[row][col]))                                 # revert sign
        else:
            val.append(data[row][col])
    for col in range(len(data[row]),len(data[1])):
        val.append(" ")
    if len(data[row]) > len(data[1]):
        xleftxoverx = data[row][len(data[1])]
        for col in range(len(data[1])+1,len(data[row])):
            xleftxoverx = xleftxoverx + '\t' + data[row][col]
        val.append(xleftxoverx)
    elif maxlen > len(data[1]):
        val.append('')
    data_tbs.append(tuple(val))
data_tbs = np.array(data_tbs, dtype=dt)
data_tbs = data_tbs[np.argsort(data_tbs[keys], kind='mergesort')]


filename = filename+".Dsorted"
writefile = open(filename, "w")
for row in range(0,2):
    for word in data[row]:
        writefile.write(word + "\t")
    writefile.write("\n")
flag = data_tbs[0][col_keys[0]]
for term in data_tbs:
    if (term[col_keys[0]] != flag and print_blank == 1):
        writefile.write("\n")
    for col in range(0,len(term)):
        if col in col_keys:
            writefile.write(str(-term[col])+"\t")                              # revert sign
        else:
            writefile.write(str(term[col])+"\t")
    writefile.write("\n")
    flag = term[col_keys[0]]
writefile.close()
print '--------------------------------------------------------'
