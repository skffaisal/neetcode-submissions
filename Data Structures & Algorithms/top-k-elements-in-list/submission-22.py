class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        count = {}
        res = []

        # Directly iterating over elements is faster than index loops in Python
        for num in n:
            count[num] = count.get(num, 0) + 1

        # Create buckets where index = frequency
        buckets = [[] for _ in range(len(n) + 1)]
        for value, frequency in count.items():
            buckets[frequency].append(value)

        # Iterate backwards from the highest frequency bucket
        for i in range(len(buckets) - 1, -1, -1):
            for value in buckets[i]:
                res.append(value)
                if len(res) == k:
                    return res  # Return immediately instead of using breaks
