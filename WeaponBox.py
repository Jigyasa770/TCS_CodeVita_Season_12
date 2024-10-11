import math
from collections import deque

# Function to check if a number is a triangular number
def is_triangular(x):
    n = (-1 + math.sqrt(1 + 8 * x)) / 2.0
    return n.is_integer()

# Function to calculate the labor cost
def calculate_labor_cost(weights, N, K):
    queue = deque(weights)
    consecutive_unshifted = 0
    current_max = None
    shifted = []

    while consecutive_unshifted < K:
        # Get the first N boxes for this cycle.
        cycle = [queue.popleft() for _ in range(min(N, len(queue)))]
        
        # Find the box that will remain after the cycle.
        while len(cycle) > 1:
            a = cycle.pop(0)
            b = cycle.pop(0)
            if a < b:
                shifted.append(a)
                queue.append(a)
                cycle.insert(0, b)  # Insert the larger one back into the front.
            else:
                shifted.append(b)
                queue.append(b)
                cycle.insert(0, a)  # Insert the larger one back into the front.

        # The remaining element is the max for this cycle.
        last_box = cycle[0]

        # If this is the same as the current max, increase consecutive_unshifted count.
        if current_max == last_box:
            consecutive_unshifted += 1
        else:
            consecutive_unshifted = 1  # Reset to 1 as this is the first time last_box remains.
            current_max = last_box

        # Add the last box back to the front of the queue.
        queue.appendleft(last_box)

    # Calculate the labor cost by summing the non-triangular weights of shifted boxes.
    labor_cost = sum(w for w in shifted if not is_triangular(w))
    return labor_cost

# Main function to handle input and output
if __name__ == "__main__":
    weights = list(map(int, input().split()))
    N, K = map(int, input().split())
    result = calculate_labor_cost(weights, N, K)
    print(result, end = '')
