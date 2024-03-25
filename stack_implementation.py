# Implement a stack that has the following methods:
# - push(val), which pushes an element onto the stack
# - pop(), which pops off and returns the topmost element of the stack.
# If there are no elements in the stack, then it should throw an error or return null.
# - max(), which returns the maximum value in the stack currently.
# If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.


# Implement linked list to run methods in constant time
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.max_val = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        # Insert a new ele to the top of stack
        new_node = Node(data)
        if self.top is None:  # Add an ele to the top if a stack is empty
            self.top = new_node
            return print(f'Added {new_node.data} to the top of the stack!')
        else:  # Else link a new ele with a top, then update a new top value
            new_node.next = self.top
            new_node.max_val = max(data, self.top.max_val)  # Compare and update a new max value if needed
            self.top = new_node
            return print(f'Added {new_node.data} to the top of the stack!')

    def pop(self):
        # Remove a top ele of the stack
        if self.top is None:  # Print error if the stack is empty
            return print('Cannot pop an empty stack!')
        else:  # Else assign previous ele's value to the top
            print(f'Popped {self.top.data} out of the stack!')
            self.top = self.top.next

    def max_val(self):
        if self.top is None:
            return print('Cannot find a max value in an empty stack!')
        else:
            return print(f'{self.top.max_val} is a max value of the stack!')

    def print_ele(self):
        cur_node = self.top
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next


# Testing
imp_stack = Stack()

imp_stack.push(0)
imp_stack.push(80)
imp_stack.push(35)
imp_stack.push(100)
print('----------')

imp_stack.pop()
imp_stack.max_val()
imp_stack.print_ele()
print('----------')

imp_stack.pop()
imp_stack.max_val()
imp_stack.print_ele()
