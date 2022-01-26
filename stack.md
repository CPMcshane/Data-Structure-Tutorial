# Stacks
## Introduction

Stacks are a type of ordered list and very similar to stacks we use in our everyday lives. If you have a stack of papers on your desk, you can only add to the top of the stack and you can only take from the top of the stack. Stacks are stored sequentially in memory. 

## Push/pop

Items can be added to a stack by using .append

```python 
plate = []
plate.append('pancake1')
plate.append('pancake2')
plate.append('pancake3')

print('plate') # ['pancake1', 'pancake2', 'pancake3']
```
Items can be removed by using .pop

```python
plate.pop()
plate.pop()

print('plate') # ['pancake1']
```

## Performance

Due to the stack only ever taking and adding items to the end of the list, the performance will always be O(1). There is no looping that has to be done to find a specific placement because nothing will be inserted in the middle of the stack.

## Uses

Stacks can be used for many different things, for example an undo button. A stack can be used to house a list of the users actions. Stacks will keep the first actions at the front of the list and the most recent actions at the back. The last action would be at the very end of the stack and can be accessed with a single .pop()

Anytime order matters, and you want the most recent item first, it helps to use a stack.

## Examples

[practice](stack_example.py)

[solution](stack_solution.py)


## Return link
[Back to welcome page](welcome.md)