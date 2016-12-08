"""
Write a program to calculate the value of given arithmetic expression.
Take into account that arithmetic operations have different priorities.
Consider also processing brackets correctly. Handle the unary minus as well. Examples:

5 + 6
11

(2 + 3) * 4.5
22.5

2 + 3 * 1.5 - 1
5.5

-2 - -1
3

3 ++ 4
error

1.5 – 2.5 * 2 * (-3)
16.5

1/2
0.5
"""
from collections import deque
import re


output_queue = deque()
operator_stack = deque()

# fill the output queue with the expression in polish notation
split_input = re.split(r"\s*([-+/*])\s*", input().replace(" ", ""))

print(split_input)
for token in split_input:
    if re.match("[+-]?\d+\.?\d?", token) is not None:
        # If the token is a number, then push it to the output queue.
        output_queue.append(float(token))
    elif token in ["+", "-", "*", "/"]:
        if operator_stack:
            top_element = operator_stack[-1]
            while top_element in ["+", "-", "*", "/"]:
                if token in ["+", "-"]:  # o1 is left-associative and its precedence is less than or equal to that of o2
                    output_queue.append(operator_stack.pop())
                elif top_element in ["*", "/"] and token in ["*", "/"]:  # equal to that of 02
                    output_queue.append(operator_stack.pop())
                else:
                    break
                top_element = operator_stack[-1] if operator_stack else None

        operator_stack.append(token)
        pass
    elif token in ["(", ")"]:
        if token == "(":
            operator_stack.append(token)
        else:
            """
            If the token is a right parenthesis (i.e. ")"):
            Until the token at the top of the stack is a left parenthesis, pop operators off the stack onto the output queue.
            Pop the left parenthesis from the stack, but not onto the output queue.
            """
            top_stack =  operator_stack.pop()
            while top_stack != "(":
                output_queue.append(top_stack)
                top_stack = operator_stack.pop()


"""
When there are no more tokens to read:
While there are still operator tokens in the stack:
If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
Pop the operator onto the output queue.
"""
while operator_stack:
    output_queue.append(operator_stack.pop())
print(output_queue)

" Evaluate the Postfix Notation"
x = output_queue.popleft()
stack = deque()
while True:
    if x in ["+", "-", "*", "/"]:
        a = stack.pop()
        b = stack.pop()
        if x == "+":
            stack.append(a + b)
        elif x == "-":
            stack.append(b - a)
        elif x == "*":
            stack.append(a * b)
        elif x == "/":
            stack.append(b / a)
    else:
        stack.append(x)
    if not output_queue:
        break
    x = output_queue.popleft()

print(stack.pop())

