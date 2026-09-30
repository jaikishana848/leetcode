class Solution(object):
    def maxProfit(self, prices):
        a=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum=prices[i]
            else:
                profit=prices[i]-minimum
                if profit>a:
                    a=profit
        return a
