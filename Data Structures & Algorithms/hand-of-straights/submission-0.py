class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()
        freq = defaultdict(int)
        n = len(hand)
        for i in range(n):
            freq[hand[i]] += 1

        for num in hand:
            if freq[num] > 0:
                for i in range(num, num + groupSize):
                    if not freq[i]:
                        return False
                    freq[i] -= 1

        return True