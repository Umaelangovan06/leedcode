class Solution(object):
    def maxProfit(self, prices):
        min_price=float('inf')
        max_profit=0
        for price in prices:
            min_price=min(price,min_price)
            max_profit=max(max_profit,price-min_price)
        return max_profit
    
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy=0
#         sell=1
#         profit=0
#         count=0
#         for i in prices:
#             count+=1
#         while sell<count:
#             if prices[sell]>prices[buy]:
#                 cur_profit=prices[sell]-prices[buy]
#                 if cur_profit>profit:
#                     profit=cur_profit
#             else:
#                 buy=sell
#             sell+=1
#         return profit