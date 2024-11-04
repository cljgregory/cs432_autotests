# cs432_autotests

Python script for automating test creation.
To start, create a new file "test.decaf" inside of your project folder for the current project (i.e. p4 or p3).
now download auto.py and add it to the same spot inside the project folder. 

THIS AUTOMATION WILL ONLY CHECK AGAINST THE PRINTED OUTPUT OF THE REFERENCE COMPILER AND NOT THE ILOC CODE USING --fdump-iloc

The script will create an input, expected, and output file and edit the itests.include file. It works by piping the output of the compiler to the 
appropriate file. Then the given test suite should handle the rest. 




