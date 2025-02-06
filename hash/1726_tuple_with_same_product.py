class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        products = []

        for i in range(n):
            for j in range(i + 1, n):
                products.append(nums[i] * nums[j])
        
        products.sort()

        product = -1
        cnt = 0
        res = 0

        for i in range(len(products)):
            if products[i] == product:
                cnt += 1
            else:

                pairs = ((cnt - 1) * cnt // 2)
                res += 8 * pairs

                product = products[i]
                cnt = 1
        
        pairs = ((cnt - 1) * cnt // 2)
        res += 8 * pairs

        return res