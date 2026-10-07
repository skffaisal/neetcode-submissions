class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        # using sorting 
        freq = {}

        # 1. Count frequencies
        for value in n:
            freq[value] = freq.get(value, 0) + 1

        # 2. Convert dict → (value, frequency)
        freq = list(freq.items())

        # 3. Sort by frequency, highest first
        sorted_by_freq = sorted(
            freq,
            key=lambda item: item[1],
            reverse=True
        )

        # 4. Take first k values
        result = []

        for value, frequency in sorted_by_freq[:k]:
            result.append(value)

        return result