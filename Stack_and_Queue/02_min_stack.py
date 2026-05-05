class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append([val, val])
        else:
            current_min = self.stack[-1][1]
            new_min = min(current_min, val)
            self.stack.append([val, new_min])
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]


    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]


if __name__ == "__main__":
    min_stack = MinStack()

    values_to_push = [5, 3, 7, 2]

    print("Pushing elements into MinStack:")
    for value in values_to_push:
        min_stack.push(value)
        print(f"push({value}) -> top: {min_stack.top()}, min: {min_stack.getMin()}")

    print("\nPopping one element:")
    min_stack.pop()
    print(f"top: {min_stack.top()}, min: {min_stack.getMin()}")

    print("\nCurrent stack state:")
    print(min_stack.stack)
