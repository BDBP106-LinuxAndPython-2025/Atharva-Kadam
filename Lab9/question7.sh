#!/bin/bash


echo "Energy = Mass * Speed"
energy=$(bc << EOF
scale =5
mass =1
speed =(3*(10^8))
mass*(speed)^2
EOF
)
echo "Thus the value is:"$energy
