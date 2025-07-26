

def MaxProfitBruteForce(A, m, n):
    """
    Brute force algorithm to find the maximum profit from a single buy/sell trans.

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks (rows)
        n (int): Number of days (columns)

    Returns:
        Tuple[int, int, int, int]: (bestStock, bestBuyDay, bestSellDay, maxProfit)
        All values are 1-based indices.
        Returns (0, 0, 0, 0) if no profit is possible.
    """

    # --- edge case: check if the input is empty or missing ---
    if m <= 0 or n <= 1 or not A or n < 2:    
        return (0, 0, 0, 0)
    
    # --- edge case: check if matrix has proper dimensions
    if len(A) != m or any(len(row) != n for row in A):
        return (0, 0, 0, 0)

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
    
    print("=" * 70)
    print("{:^70}".format("BRUTE FORCE ALGORITHM PROBLEM 1 - TASK 1 TESTS"))
    print("=" * 70)

    print("\n Sample test from Project PDF description")
    A = [
        [7, 1, 5, 3, 6],
        [2, 4, 3, 7, 9],
        [5, 8, 9, 1, 2],
        [9, 3, 14, 8, 7]
    ]
    result = MaxProfitBruteForce(A, 4, 5) 
    print(f"Expected: (4, 2, 3, 11) | Result: {result}")

    print("\n 1: Mixed stocks with profits")
    matrix1 = [
        [7, 1, 5, 3, 6, 4],
        [2, 8, 3, 9, 1, 5],
        [10, 2, 6, 4, 8, 3]
    ]
    result = MaxProfitBruteForce(matrix1, 3, 6)
    print(f"Expected: (2, 1, 4, 7) | Result: {result}")

    print("\n 2: No profit possible")
    matrix2 = [
        [10, 8, 6, 4, 2],
        [15, 12, 10, 5, 1]
    ]
    result = MaxProfitBruteForce(matrix2, 2, 5)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 3: Minimum valid input (1 stock, 2 days)")
    matrix3 = [
        [1, 5]
    ]
    result = MaxProfitBruteForce(matrix3, 1, 2)
    print(f"Expected: (1, 1, 2, 4) | Result: {result}")

    print("\n" + "=" * 70)
    print("{:^70}".format("EDGE CASES"))
    print("=" * 70)

    print("\n 1: Empty matrix")
    result = MaxProfitBruteForce([], 0, 0)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 2: One stock One day (no transaction possible)")
    result = MaxProfitBruteForce([[5]], 1, 1)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")


    print("\n 3: Invalid Matrix dimensions")
    matrix_invalid = [
        [1, 2, 3],
        [4, 5]
    ]
    result = MaxProfitBruteForce(matrix_invalid, 2, 3)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")

    print("\n 4: All stocks with the same price")
    matrix_flat = [
        [3, 3, 3, 3],
        [3, 3, 3, 3]
    ]
    result = MaxProfitBruteForce(matrix_flat, 2, 4)
    print(f"Expected: (0, 0, 0, 0) | Result: {result}")
