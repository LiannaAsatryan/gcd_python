#description of the main program
this program finds the greatest common dividor of two numbers written in the input file like this:
 num1 num2
 num1 num2
 ...
after the execution the answers will be store in the output file like this:
 answer1
 answer2
 ... 

#gcd_test.py description
this test_file performs the following operations for every line in the input file:
reads two input numbers from the input file, finds their greatest common dividor, writes in the output file, 
compares the result value with the corresponding value in golden file and writes the appropriate message in the result file
If the current values of the input file aren't integer numbers, the answer is "mistake"

#files
 in this directory there are following files
* input.txt __ it is the file where our input values are written
* golden.txt __ it is the file where our correct answers are written
* gcd_functions.py __it is the file where the problem_solver function and other related functions are written
* gcd_test.py __ this .py file contains the operations of reading from the input file, solving and writing in output file and the result file(testing)
* main.py __ this file contains the program which solves our main problem (without testing)

the files that will be generated are 
*output.txt__here the result-values are written
*result.txt__here the test results are written(test passed or not)
*__pycache__(this directory is generated because I import the functions from a file into another)


#to run the main program type in command line
 python3 main.py
to clean the generated files type 
 rm output.txt
 rm -r __pycache__


#to run the test type in command line
 python3 gcd_test.py
to clean the generated files type 
 rm output.txt result.txt
 rm -r __pycache__
