#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)#!/bin/bash
echo "enter three sides of the triangle"
read a
read b
read c

if [ $a == $b ]  && [ $b == $c ] && [ $c == $a ]
then
    echo "This is an equilateral triangle"
elif [ $a == $b ] || [ $b == $c ] || [ $c == $a ]
then 
    echo "This is a isosceles triangle"
else
echo "This is a scalene triangle"
fi
