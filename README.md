# version_control

## File Description

The math_lib.py file contains a 2 functions: 

1. div - performs division and correctly handles division by zero, the arguments are positional where the first number is the numerator and the second is the denominator

2. add    performs addition

The calculate.py file uses the functions from math_lib.py depending on which is specified by the user.

The file run.sh runs the calculate.py file.

## Usage

The user must specify a mathematical operation and then the two numbers they want the operation to be performed on 

Example: 

```
./run.sh add 1 2
```

which gives the result

```
3
```

If the second specified number is 0 in the division operation, the program with indicate an error caused by the division of zero.