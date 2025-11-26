class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = [0] * len(boxes)
        for i in range(len(moves)):
            for j in range(len(moves)):
                if boxes[j] == "1":
                    moves[i] += abs(i-j)
                
        return moves

        