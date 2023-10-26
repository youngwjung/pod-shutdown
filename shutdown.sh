#!/bin/sh

echo "prestop hook initiated"
for i in `seq 1 $1`
do
  echo "$i"
  sleep 1
done
echo "prestop hook completed"