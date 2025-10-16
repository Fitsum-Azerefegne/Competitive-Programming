class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        start, end = 0 , 0
        last_occurence = {}
        for i in range(len(s)):
            last_occurence[s[i]] = i
        for index, char in enumerate(s):
            end = max(end, last_occurence[char])
            if index == end:
                partitions.append(end - start + 1)
                start = index + 1
        return partitions
        