def topKFrequent(nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1,2,3,3,3,6,4,5,6,6], 2))
