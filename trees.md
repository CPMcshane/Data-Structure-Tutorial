# Trees

## Introduction
Trees are a form of linked list. Linked lists can only point to one node as the 'next node' in the list. Trees can point to multiple nodes as being the 'next' node.

## Binary Search Trees
A binary tree is a tree in which each node points to no more than two other nodes. A binary search tree uses certain organization methods to decide where each node is placed. 

A simple example is using a greater than/less than criteria for where to place the new node. If the number value of the new node is less than the current node we move down the left pointer. If the value is greater than the value of the current node then we move down the right pointer. We repeat until we find an empty spot for the new node.

![tree diagram 1](diagrams/tree_diagram1.jpeg)

## Balancing
The order we add nodes to the tree can be very important. If we consistantly add values in a descending order, the tree will only add pointers to the left side. This effects us when we have to search for certain values in the tree. An unbalanced tree is the difference between a O(n) performance and a O(log n) performance.

![tree diagram 2](diagrams/tree_diagram2.jpeg)

## Searching
If we follow a specific order when creating the binary search tree, we can use that same logic when looking for a specific value. If the value we are looking for is 3, as we search the tree we can make a comparison at each node we visit. If three is less than the current node's value we move to the left, otherwise we move to the right.

Once we find where the number three should be, we can check to see if it is there or not. If we have reached our destination and the value of three is there, we know it is in our tree. If we arrive where three should have been placed and there is no three value, we know the number three is not in our search tree.

Because we are using a greater than, less than search, we have a performance of O(log n). 

## Recursion
Recursion is how we move through our search tree. Recursion is a method of programming where the function we write calls itself within the function. Recursion is broken into two sections in our functions, a smaller problem and a base case.

### Smaller problem
With recurion we want to break up our problem at hand into a smaller problem. For example if we are trying to write a function to perform n factorial, our smaller problem is multiplying two numbers rather than all the numbers as once.

Once we multiply two numbers, we can call the our function again to multiply the next two numbers.

```python
def factorial(n):
    number = n * factorial(n-1)
```
### Base case
The base case is how we get the recurion to stop and the returning to begin. For our factorial example, we only want to go until we get to when n is euqal to 1.

```Python
def factorial(n):

    # Base case
    if n == 1:
        return 1

    # Smaller problem
    number = n * factorial(n-1)
    return number
```
# diagram

## Example/Solution

[practice](trees_example.py)

[solution](trees_solution.py)

## Return to welcome page
[Back to welcome page](welcome.md)