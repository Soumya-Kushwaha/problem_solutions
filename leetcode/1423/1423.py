class Solution(object):
    def maxScore(self, cardPoints, k):
        frontSum, backSum = [0], [0]
        frontSum.extend(frontSum[-1] + n for n in cardPoints)
        backSum.extend(backSum[-1] + n for n in cardPoints[::-1])
        allCombinations = [frontSum[i] + backSum[k - i] for i in range(k + 1)]
        return max(allCombinations)
