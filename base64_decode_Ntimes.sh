#!/bin/bash

old = "you base64 is here"

for i in {0..100} #nums of decode
do
  new=$(echo $old | base64 -d)
    old = $new
    echo $new
done
