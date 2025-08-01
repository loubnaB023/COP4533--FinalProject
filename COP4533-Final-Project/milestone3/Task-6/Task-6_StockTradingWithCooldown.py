def StockTradingWithCooldown(A, m, n, cooldown):
    """
        Time Complexity: O(m·n^2)

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks
        n (int): Number of days
        cooldown (int): period of cooldown after selling a stock

    Returns:
        Tuple[int, List[Tuple[int, int, int]]]: A tuple containing:
            - The maximum total profit (int),
            - A list of selected transactions, each represented as a tuple:
                (stock_index, buy_day, sell_day)
    """

    # --- edge case: check if the input is empty or missing ---
    if m <= 0 or n <= 1 or not A or cooldown <= 0:
        return 0, []
    
    # --- edge case: check if matrix has proper dimensions
    if len(A) != m or any(len(row) != n for row in A):
        return 0, []
    
    # --- 1: find all profitable transactions ---
    # transactions = [(stock_index, buy_day, sell_day, profit, next_day)]
    # where next_day = sell_day + cooldown + 1 (1-based index)
    transactions = []
    for stock_id in range(m):
        prices = A[stock_id]
        for buy_day in range(n - 1):
            for sell_day in range(buy_day + 1, n):
                profit = prices[sell_day] - prices[buy_day]
                if profit > 0:
                    buy = buy_day + 1
                    sell = sell_day + 1
                    next_day = sell + cooldown + 1
                    transactions.append((stock_id + 1, buy, sell, profit, next_day))

    # --- 2: Sort by buy_day ---    
    transactions.sort(key=lambda x: x[1])

    # --- 3: DP table where dp[day] = (max_profit, best_sequence) ---
    dp = [(0, []) for _ in range(n + 2)]  # allows access to sell + cooldown + 1 
    prefix_max = [(0, []) for _ in range(n + 2)]

    for t in transactions:
        stock, buy, sell, profit, next_day = t
        next_day = min(next_day, n)  # cap to make sute next_day does not exceed n

        # --- compute the best result before or on the buy day  ---
        '''
        this allows us to safely insert the current transaction without violating cooldown constraints.
        - we retrieve the max profit up to the buy day from prefix_max.
        - then we calculate the new total profit if we include this transaction.
        - if this new total profit is better than what we currently have for the 'next_day',
        - we update dp[next_day] with the new profit and sequence.'''
        best_profit_before = prefix_max[buy]
        total_profit = best_profit_before[0] + profit
        sequence = best_profit_before[1] + [(stock, buy, sell)]

        if total_profit > dp[next_day][0]:
            dp[next_day] = (total_profit, sequence)

        # --- update prefix max at next_day ---
        prefix_max[next_day] = max(prefix_max[next_day], dp[next_day], key=lambda x: x[0])

    #-- make sure each prefix_max[i] keeps the best result so far  ---
    '''
    this loop checks each day and makes sure that prefix_max[i] has
    the best profit we've seen up to that day.
    If it wasn't updated earlier, we copy the value from the previous day.'''
    for i in range(1, n + 2):
        prefix_max[i] = max(prefix_max[i], prefix_max[i - 1], key=lambda x: x[0])

    best_result = max(dp, key=lambda x: x[0])    

    return best_result  # (max_profit, sequence)






if __name__ == "__main__":
    A = [
        [2, 9, 8, 4, 5, 0, 7],
        [6, 7, 3, 9, 1, 0, 8],
        [1, 7, 9, 6, 4, 9, 11],
        [7, 8, 3, 1, 8, 5, 2],
        [1, 8, 4, 0, 9, 2, 1]
    ]
    m, n, c = 5, 7, 2

    profit, sequence = StockTradingWithCooldown(A, m, n, c)

    print(" Best Sequence for Max Profit:")
    for s in sequence:
        stock_id, buy_day, sell_day = s
        buy_price = A[stock_id - 1][buy_day - 1]
        sell_price = A[stock_id - 1][sell_day - 1]
        individual_profit = sell_price - buy_price
        print(f"Stock {stock_id}: Buy Day {buy_day}, Sell Day {sell_day}, Profit = {individual_profit}")
        
    print("\n Transaction Sequence [(stock_index, buy_day, sell_day)]:")
    print([(s[0], s[1], s[2]) for s in sequence])
    print(f"\n Total Profit: {profit}")

        # === Edge Case Tests ===
    print("\n\n ==== Edge case tests ===") # Expected: (0, [])

    edge_cases = [       
        ("1: Empty matrix", [], 0, 0, 2),
        ("2: m <= 0", [[1, 2, 3]], 0, 3, 1),
        ("3: n <= 1", [[1]], 1, 1, 1),
        ("4: cooldown < 0", [[1, 2, 3]], 1, 3, -1),
        ("5: Row count mismatch", [[1, 2], [3, 4]], 3, 2, 1),
        ("6: Column count mismatch", [[1, 2, 3], [4, 5]], 2, 3, 1),
    ]

    for name, test_A, test_m, test_n, test_k in edge_cases:
        result = StockTradingWithCooldown(test_A, test_m, test_n, test_k)
        print(f"{name}\nResult: {result}\n")  # Expected: []

   


