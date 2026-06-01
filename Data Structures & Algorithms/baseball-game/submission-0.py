class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for val in operations:
            match val:
                case "+":
                    record.append(sum(record[-2:]))
                case "D":
                    record.append(record[-1]*2)
                case "C":
                    record.pop()
                case _:
                    record.append(int(val))            
        return sum(record)                    
