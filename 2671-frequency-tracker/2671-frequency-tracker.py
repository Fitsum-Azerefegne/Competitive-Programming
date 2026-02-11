class FrequencyTracker:

    def __init__(self):
        self.firstfreq = defaultdict(int)
        self.secondfreq = defaultdict(int)
        # first {number: occurance}
        # second {frequency: number with that frequency}

    def add(self, number: int) -> None:
        old = self.firstfreq[number]
        if old > 0:
            self.secondfreq[old] -= 1
        self.firstfreq[number] += 1
        new = self.firstfreq[number]
        self.secondfreq[new] += 1

    def deleteOne(self, number: int) -> None:
        old = self.firstfreq[number]
        if old == 0:
            return
        self.firstfreq[number] -= 1
        self.secondfreq[old] -= 1
        new = self.firstfreq[number]
        self.secondfreq[new] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        if self.secondfreq[frequency] > 0:
            return True
        return False



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)