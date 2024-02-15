from collections import deque

def solve(integers):
    # Convert the input string to a list of integers
    integers_list = [int(x) for x in integers.split(' ')]

    # Create a sorted version of the list for later comparison
    sorted_integers = sorted(integers_list)

    # Create a deque from the list to allow efficient popping from both ends
    stack = deque(integers_list)

    # Initialize an empty deque to hold the final pile of cubes
    pile = deque()

    # Loop until there are less than two cubes left in the stack
    while len(stack) >= 2:
        # Remove and append the larger of the first and last cube to the pile
        pile.appendleft(stack.popleft() if stack[0] >= stack[-1] else stack.pop())

    # Append the remaining cube in the stack to the pile
    pile.appendleft(stack.pop())

    # Check if the pile of cubes is sorted in decreasing order 
    # (this is the actual requirement)
    return pile == deque(sorted_integers)

if __name__ == '__main__':
    integers = '4 3 2 1 3 4'
    print(solve(integers))  # True

    integers = '1 3 2'
    print(solve(integers))  # False