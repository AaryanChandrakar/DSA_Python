"""
CASE STUDY 2: Real-Time Log Anomaly Detection
Problem Statement
You are given a string of system logs where:
• ( represents process start
• ) represents process end
Determine whether the log sequence is valid.
Input Format
logs

Sample Input
(()())

Sample Output
VALID
"""

logs = input("Enter the log sequence: ")

def is_valid_log(logs):
    stack = []
    for char in logs:
        if char == '(':   
            stack.append(char)
        elif char == ')':
            if not stack:
                return "INVALID"
            stack.pop()
        else:
            pass
    return "VALID" if not stack else "INVALID"

print(is_valid_log(logs))