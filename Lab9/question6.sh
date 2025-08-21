#!/bin/bash

echo "The value of Home variable is:" $HOME


x=23934
y=44343
z=$(bc << EOF
scale=5
a=($x/$y)
a*1
EOF
)
echo "The answer is-" $z

echo ` ls /home/ibab |grep D`

echo `grep ibab /etc/passwd`
