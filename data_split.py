#!/usr/bin/python
import sys
import os
num_argv = len(sys.argv)

print '--------- split data into files according to key --------'
if ( num_argv<3 ):
    sys.exit("Usage: data_split filename key ...")
elif ( sys.argv[1]=='--help' ):
    sys.exit("Usage: data_split filename key ...")
else:
    filename=sys.argv[1]
    key=sys.argv[2]

if filename[-7:] != '.sorted':
    sys.exit("file has to be sorted by the key before entering!")
readfile = open(filename, "r")
data = [line.split() for line in readfile]
readfile.close()

if ( data[0][0][0]!='#' ):
    print 'data[0][0]:\t', data[0][0]
    sys.exit("Check if your 1st line starts with #?")

row_total    = len(data)
row_begin    = 2
row_end      = row_total-1
col_begin    = 0
col_end      = len(data[row_begin])-1
col_key      = data[row_begin-1].index(key)
vals         = []
row_bgn_vals = []
for row in range(row_begin,row_end+1):
    val = data[row][col_key]
    if (val not in vals):
        vals.append(val)
        row_bgn_vals.append(row)


for i in range(0,len(vals)):
    if i == len(vals)-1:
        row_end_val = row_end
    else:
        row_end_val = row_bgn_vals[i+1]-1
    if (not os.path.isdir(key+vals[i])):
        os.mkdir(key+vals[i])
    writefile = open(key+vals[i]+"/"+filename[:-7], "w")
    for word in data[0]:
        writefile.write(word + "\t")
    writefile.write("\n")
    for word in data[1]:
        writefile.write(word + "\t")
    writefile.write("\n")
    for row in range(row_bgn_vals[i],row_end_val+1):
        for word in data[row]:
            writefile.write(word + "\t")
        writefile.write("\n")
    writefile.close()

print '--------------------------------------------------------'