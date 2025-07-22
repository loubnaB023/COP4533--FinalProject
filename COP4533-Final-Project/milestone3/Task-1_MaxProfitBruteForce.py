

def MaxProfitBruteForce(A, m, n):
    """
    Brute force algorithm to find the maximum profit from a single buy/sell transaction.

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks (rows)
        n (int): Number of days (columns)

    Returns:
        Tuple[int, int, int, int]: (bestStock, bestBuyDay, bestSellDay, maxProfit)
        All values are 1-based indices.
        Returns (0, 0, 0, 0) if no profit is possible.
    """

    # --- initialize variables to store the best result found ---
    maxProfit = 0
    bestStock = 0
    bestBuyDay = 0
    bestSellDay = 0

    # --- try every possible stock ---
    for i in range(m):  # stock index (0-based)
        # --- try every possible buy day ---
        for j1 in range(n - 1):  # buy day
            # --- try every possible sell day after the buy day ---
            for j2 in range(j1 + 1, n):  # sell day
                # --- calculate profit for the current transaction ---
                profit = A[i][j2] - A[i][j1]

                # --- if this transaction gives higher profit, update the result ---
                if profit > maxProfit:
                    maxProfit = profit
                    # 1-based index
                    bestStock = i + 1        
                    bestBuyDay = j1 + 1      
                    bestSellDay = j2 + 1     

    # --- return result depending on whether any profit was made ---
    if maxProfit == 0:
        return (0, 0, 0, 0)  # if no profitable transaction found
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

    result = MaxProfitBruteForce(A, m, n)
    print("BEST TRANSACTION:", result)  # Expected output: (4, 2, 3, 11)