
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


    # --- edge case: check if the input is empty or missing ---
    if m <= 0 or n <= 1 or not A or n < 2:    
        return (0, 0, 0, 0)
    
    # --- edge case: check if matrix has proper dimensions
    if len(A) != m or any(len(row) != n for row in A):
        return (0, 0, 0, 0)

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

    print("=" * 70)
    print("{:^70}".format("GREEDY ALGORITHM PROBLEM 1 - TASK 2 TESTS"))
    print("=" * 70)

    print("\n Sample test from Project PDF description")
    A = [
        [7, 1, 5, 3, 6],
        [2, 4, 3, 7, 9],
        [5, 8, 9, 1, 2],
        [9, 3, 14, 8, 7]
    ]
    result = MaxProfitGreedySolution(A, 4, 5)
    print(f"Expected: (4, 2, 3, 11) | Result: {result}")
    
    print("\n 1: Mixed stocks with profits (VALID)")
    matrix1 = [
        [7, 1, 5, 3, 6, 4],
        [2, 8, 3, 9, 1, 5],
        [10, 2, 6, 4, 8, 3]
    ]
    result = MaxProfitGreedySolution(matrix1, 3, 6)
    print(f"Expected: (2, 1, 4, 7) | Result: {result}")
    
    print("\n 2: No profit possible")
    matrix2 = [
        [10, 8, 6, 4, 2],
        [15, 12, 10, 5, 1]
    ]
    result = MaxProfitGreedySolution(matrix2, 2, 5)
    print(f"Expected: (0, 0, 0, 0)| Result: {result}")

    print("\n 3: Minimum valid input (1 stock, 2 days)")
    matrix3 = [
        [1, 5]
    ]
    result = MaxProfitGreedySolution(matrix3, 1, 2)
    print(f"Expected: (1, 1, 2, 4) | Result: {result}")
    
    print("\n" + "=" * 70)
    print("{:^70}".format("EDGE CASES"))
    print("=" * 70)

    print("\n 1: Empty matrix")
    result = MaxProfitGreedySolution([], 0, 0)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 2: One stock One day (no transaction possible)")
    result = MaxProfitGreedySolution([[5]], 1, 1)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 3: Invalid Matrix dimensions")
    matrix_invalid = [
        [1, 2, 3],
        [4, 5]
    ]
    result = MaxProfitGreedySolution(matrix_invalid, 2, 3)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 4: Same price for all stocks")
    matrix_flat = [
        [3, 3, 3, 3],
        [3, 3, 3, 3]
    ]
    result = MaxProfitGreedySolution(matrix_flat, 2, 4)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")
    

   