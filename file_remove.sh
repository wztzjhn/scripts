#!/bin/bash
# sourcing environment.sh will not work in non-interactive bash,
# you have to specify the path of this script in these cases.

if [ $# == 0 ]; then
    echo "mv: missing file operand"
    exit -250
fi

declare -a inputs=( $@ )

trash_personal="${HOME}/Trash_Personal"
trash_system="${HOME}/.local/share/Trash/files"
if [ -d ${trash_personal} ]; then
    trash_folder=${trash_personal}
elif [ -d ${trash_system} ]; then
    trash_folder=${trash_system}
else
    echo "Trash folder not located correctly."
    echo "To unalias, use command: unalias rm"
    exit -250
fi
year=`date +%Y`
month=`date +%m`
day=`date +%d`
trash_sub1="${trash_folder}/${year}-${month}-${day}"
if [ ! -d ${trash_sub1} ]; then
    mkdir ${trash_sub1}
fi
hour=`date +%H`
trash_sub2="${trash_sub1}/H${hour}"
if [ ! -d ${trash_sub2} ]; then
    mkdir ${trash_sub2}
fi
min=`date +%M`
sec=`date +%S`
trash_sub3="${trash_sub2}/M${min}:S${sec}"
if [ ! -d ${trash_sub3} ]; then
    mkdir ${trash_sub3}
fi

i=0
while [ $i -lt $# ]; do
    if [ ${inputs[i]} != "-r" ]; then
        mv ${inputs[i]} ${trash_sub3}
    fi
    i=$[$i+1]
done
