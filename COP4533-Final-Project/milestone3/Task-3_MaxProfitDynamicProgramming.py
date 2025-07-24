def MaxProfitDynamicProgramming(A, m, n):
    """
    DP approach to find the maximum profit from a single buy/sell transaction.

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks
        n (int): Number of days

    Returns:
        Tuple[int, int, int, int]: (bestStock, bestBuyDay, bestSellDay, maxProfit)
        All values use 1-based indexing. 
        Returns (0, 0, 0, 0) if no profit is possible.
    """

    # --- edge case: check if the input is empty or missing ---
    if m <= 0 or n <= 1 or not A:
        return (0, 0, 0, 0)
    
    # --- edge case: check if matrix has proper dimensions
    if len(A) != m or any(len(row) != n for row in A):
        return (0, 0, 0, 0)

    # --- initialize variables to store the best result ---
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    # --- loop through each stock ---
    for i in range(m):
        minPrice = A[i][0]  # lowest price seen so far for this stock
        minDay = 0          # day when the lowest price occurred

        # --- check each day starting from day 1 ---
        for j in range(1, n):
            currentProfit = A[i][j] - minPrice  # profit if we sell today

            # --- update result if we found a better profit ---
            if currentProfit > maxProfit:
                maxProfit = currentProfit
                bestStock = i + 1         # 1-based index
                bestBuyDay = minDay + 1
                bestSellDay = j + 1

            # --- update minPrice if today's price is lower ---
            if A[i][j] < minPrice:
                minPrice = A[i][j]
                minDay = j

    # --- return result  ---
    if maxProfit == 0:
        return (0, 0, 0, 0) # if no profitable transaction found
    else:
        return (bestStock, bestBuyDay, bestSellDay, maxProfit)
    
