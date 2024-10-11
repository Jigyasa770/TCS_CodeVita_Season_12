def count_valid_combinations(trees):
    n = len(trees)
    count = 0
    
    # Count the occurrences of each tree type in the current selection
    count_M_before = 0  # Count of 'M' before the current index
    count_L_before = 0  # Count of 'L' before the current index
    
    # First pass from left to right
    for i in range(n):
        if trees[i] == 'M':
            # If we choose 'M', count how many 'L's we can choose after
            count += count_L_before * (count_L_before - 1) // 2
            count_M_before += 1
        elif trees[i] == 'L':
            # If we choose 'L', count how many 'M's we can choose after
            count += count_M_before * (count_M_before - 1) // 2
            count_L_before += 1
            
    # Reset counters for the second pass
    count_M_after = 0  # Count of 'M' after the current index
    count_L_after = 0  # Count of 'L' after the current index
    
    # Second pass from right to left
    for i in range(n - 1, -1, -1):
        if trees[i] == 'M':
            count += count_L_after * (count_L_after - 1) // 2
            count_M_after += 1
        elif trees[i] == 'L':
            count += count_M_after * (count_M_after - 1) // 2
            count_L_after += 1
            
    return count

def find_winner(row_ashok, row_anand):
    # Input validation
    if not all(c in 'ML' for c in row_ashok) or not all(c in 'ML' for c in row_anand):
        return "Invalid input"
    
    # Count combinations
    count_ashok = count_valid_combinations(row_ashok)
    count_anand = count_valid_combinations(row_anand)
    
    # Determine winner
    if count_ashok > count_anand:
        return "Ashok"
    elif count_anand > count_ashok:
        return "Anand"
    else:
        return "Draw"

# Input
ashok_row = input().strip()
anand_row = input().strip()

# Output the result
print(find_winner(ashok_row, anand_row), end = '')
