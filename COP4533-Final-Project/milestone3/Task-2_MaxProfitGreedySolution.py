
def MaxProfitGreedySolution(A, m, n):
    """
    Greedy algorithm to find the maximum profit from a single buy/sell transaction.

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks
        n (int): Number of days

    Returns:
        Tuple[int, int, int, int]: (bestStock, bestBuyDay, bestSellDay, maxProfit)
        All values use 1-based indexing. 
        Returns (0, 0, 0, 0) if no profit is possible.
    """

    # --- initialize variables to store the best result ---
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    # --- iterate over each stock ---
    for i in range(m):
        # --- assume the first day's price is the lowest seen so far ---
        minPrice = A[i][0]      # track minimum price for current stock
        minDay = 0              # track the day of the minimum price

        # --- iterate through the rest of the days ---
        for j in range(1, n):   # start from day 1 (second day)
            profit = A[i][j] - minPrice  # potential profit if sold today

            # --- if this transaction gives better profit, update result ---
            if profit > maxProfit:
                maxProfit = profit
                # 1-based index for stock, buy day, and sell day
                bestStock = i + 1        
                bestBuyDay = minDay + 1   
                bestSellDay = j + 1   

            # --- update minPrice if a new lower price is found ---
            if A[i][j] < minPrice:
                minPrice = A[i][j]
                minDay = j

    # --- return result ---
    if maxProfit == 0:
        return (0, 0, 0, 0)     # if no profitable transaction found
    else:
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
    


# --- TEST CASE SECTION ---
if __name__ == "__main__":
    
    # test matrix from the project description
    A = [
        [7, 1, 5, 3, 6],
        [2, 4, 3, 7, 9],
        [5, 8, 9, 1, 2],
        [9, 3, 14, 8, 7]
    ]
    m = len(A)
    n = len(A[0])

    result = MaxProfitGreedySolution(A, m, n)
    print("BEST TRANSACTION USING THE GREEDY SOLUTION:", result)
    # Expected Output: (4, 2, 3, 11)