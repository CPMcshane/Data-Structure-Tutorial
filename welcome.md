# Welcome page

## This tutorial will cover stacks, sets, and trees

Each tutorial will hava an explaination, diagrams and practice problems to help you learn about these data structures and how to use them.

[stacks](stack.md)

[sets](sets.md)

[trees](trees.md)

## A quick note about Big O notation.

Big O notation is how we measure the performance of a program. It is how much
the workload changes as our data set gets larger or smaller.

### O(1)
The code ```x = 10``` is an example of O(1) because no matter how large or small our data set is, the performance to run that line of code does not change.

### O(n)
The code
```python
for i in data:
    print(i)
```
is O(n) because the amount of work needed is directly proportional to the data size.
As the data set gets larger there is more work to be done.

### O(n^2)
The code
```python
for i in data:
    for j in data:
        print(i+j)
```
is O(n^2) because as the data increases in size, the amount of work needed increases by a factor of 2 because there are two loops.

### O(log n)
O(log n) performance can occur when the data we are searching through is cut in half every time. If we have a list of numbers and check to see if the value we are looking for is greater or less than the number we checked, we can know which half of the data we need to look at next. If we keep checking greater than or less than of the middle number in the remaining data, our performance is O(log n).

Essentially it means as the data size increases, the work is increased by log(n). The data set would have to about double in size before we would have to increase the amount of work done.