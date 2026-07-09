class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        val = self.stack[-1]
        del self.stack[-1]
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minim = self.stack[0]
        for i in range(1, len(self.stack)):
            minim = min(minim, self.stack[i])

        return minim
        
