#!/usr/bin/python
import sys
num_argv = len(sys.argv)

print '----------- remove data with repeated keys ----------'
print '-------- (data appeared later being deleted) --------'
if ( num_argv<3 ):
    sys.exit("Usage: data_rmdulp filename key1 key2 ...")
elif ( sys.argv[1]=='--help' ):
    sys.exit("Usage: data_rmdulp filename key1 key2 ...")
else:
    filename=sys.argv[1]
    keys=sys.argv[2:]
    num_keys=len(keys)
    print "keys used for removing dulplicates: ",keys

readfile = open(filename, "r")
data = [line.split() for line in readfile]
readfile.close()

if ( data[0][0][0]!='#' ):
    print 'data[0][0]:\t', data[0][0]
    sys.exit("Check if your 1st line starts with #?")

row_total=len(data)
row_begin = 2
row_end   = row_total-1
col_begin  = 0
col_end    = len(data[row_begin])-1
col_keys   = []
for key in keys:
    col_keys.append(data[row_begin-1].index(key))
print 'col_keys-1:\t\t',col_keys

# remove dulplicated lines
for row in range(row_end,row_begin,-1):
    flag=1
    for col in col_keys:
        if data[row][col]!=data[row-1][col]:
            flag=0
            break
    if flag==1:
        del data[row]
row_total=len(data)
row_begin = 2
row_end   = row_total-1

filename = filename+".rmdulpLT"
writefile = open(filename, "w")
for row in range(0,len(data)):
    for word in data[row]:
        writefile.write(word + "\t")
    writefile.write("\n")
writefile.close()
print '------------------------------------------------------'


