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
    

# --- TEST CASE SECTION ---
if __name__ == "__main__":

    print("=" * 70)   
    print("{:^70}".format("DYNAMIC PROGRAMMING ALGORITHM PROBLEM 1 - TASK 3 TESTS -"))
    print("=" * 70)

    print("\n Sample test from Project PDF description")
    A = [
        [7, 1, 5, 3, 6],
        [2, 4, 3, 7, 9],
        [5, 8, 9, 1, 2],
        [9, 3, 14, 8, 7]
    ]
    result = MaxProfitDynamicProgramming(A, 4, 5)
    print(f"Expected: Stock 4, Buy Day 2 ($3), Sell Day 3 ($14), Profit $11 | Result: {result}")

    print("\n 1: Mixed stocks with profits (VALID)")
    matrix1 = [
        [7, 1, 5, 3, 6, 4],
        [2, 8, 3, 9, 1, 5],
        [10, 2, 6, 4, 8, 3]
    ]
    result = MaxProfitDynamicProgramming(matrix1, 3, 6)
    print(f"Expected: Stock 2, Buy Day 1 ($2), Sell Day 4 ($9), Profit $7| Result: {result}")    

    print("\n 2: No profit possible")
    matrix2 = [
        [10, 8, 6, 4, 2],
        [15, 12, 10, 5, 1]
    ]
    result = MaxProfitDynamicProgramming(matrix2, 2, 5)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 3: Minimum valid input (1 stock, 2 days)")
    matrix3 = [
        [1, 5]
    ]
    result = MaxProfitDynamicProgramming(matrix3, 1, 2)
    print(f"Expected: Stock 1, Buy Day 1 ($1), Sell Day 2 ($5), Profit $4 | Result: {result}")    

    #-------------------------------------------------------------------------

    print("\n" + "=" * 70)
    print("{:^70}".format("EDGE CASES"))
    print("=" * 70) 

    print("\n 1: Empty matrix")
    result = MaxProfitDynamicProgramming([], 0, 0)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

   
    print("\n 2: One stock One day (no transaction possible)")
    result = MaxProfitDynamicProgramming([[5]], 1, 1)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 3: Invalid Matrix dimensions")
    matrix_invalid = [
        [1, 2, 3],
        [4, 5]
    ]
    result = MaxProfitDynamicProgramming(matrix_invalid, 2, 3)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 4: Same price for all stocks")
    matrix_flat = [
        [3, 3, 3, 3],
        [3, 3, 3, 3]
    ]
    result = MaxProfitDynamicProgramming(matrix_flat, 2, 4)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    
