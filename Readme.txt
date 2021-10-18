***Run dsa file in any IDE.


Documentation. (ALSO PROVIDED IN dsa.py)

The program is giving certain erroneous results.
Linear Results are coming for Exponential and Polynonmial run time while 
Logarithmic is returning a step function graph.
I have double and triple checked the test case programs which seem to be correct. 

The problem seems to be arising while clocking the program start time, which Ii have 
started before the loop. Since the loop will close only after running through the 
program, the value of start is not being stored thus the error.

I have tried but failed to correct this.

Parameters for memory fail-
1. Running 10 million elements for exponential and quadratic time complexities.
2. Spyder crashed while I tried to verify program results by printing fns. for these two cases. 
Rationale - Exponential growth in temporary storage (RAM) requirement for such calculations.
3. Jump argument required while covering large input samples.



