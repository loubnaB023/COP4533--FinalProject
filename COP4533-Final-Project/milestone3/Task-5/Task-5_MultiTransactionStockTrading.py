def MultiTransactionStockTrading(A, m, n, k):
    """
        Time Complexity: O(m·n·k)

    Parameters:
        A (List[List[int]]): Matrix representing stock prices (m stocks * n days)
        m (int): Number of stocks
        n (int): Number of days
        k (int): max number of transactions

    Returns:
        List of selected (stock_index, buy_day, sell_day, profit)
    """

    # --- edge case: check if the input is empty or missing ---
    if m <= 0 or n <= 1 or not A or k <= 0:
        return []
    
    # --- edge case: check if matrix has proper dimensions
    if len(A) != m or any(len(row) != n for row in A):
        return []
    

    all_transactions = []

    for stock_index in range(m):
        prices = A[stock_index]

        # --- initialize DP tables ---
        # DP table to store the best profit at each day for up to t transactions
        max_profit = []
        for transaction_num in range(k + 1):
            day_profits = []
            for day in range(n):
                day_profits.append(0)  # start with 0 profit for each day
            max_profit.append(day_profits)

        # DP table to remember which (buy, sell) days gave us that profit
        best_days = []
        for transaction_num in range(k + 1):
            day_pairs = []
            for day in range(n):
                day_pairs.append(None)  # no transaction yet
            best_days.append(day_pairs)

        

        for t in range(1, k + 1):
            max_diff = -prices[0]        # best value of (max_profit[t-1][d] - prices[d])
            best_buy_day = 1             # start with day 1 (1-based)

            for day in range(1, n):
                current_profit = prices[day] + max_diff

                # ---  option 1: no new transaction today ---
                if max_profit[t][day - 1] >= current_profit:
                    max_profit[t][day] = max_profit[t][day - 1]
                    best_days[t][day] = best_days[t][day - 1]
                else:
                    # ---  option 2: sell today using the best past buy day ---
                    max_profit[t][day] = current_profit
                    best_days[t][day] = (best_buy_day, day + 1)  # store 1-based

                # --- update max_diff and corresponding buy day ---
                prev = max_profit[t - 1][day] - prices[day]
                if prev > max_diff:
                    max_diff = prev
                    best_buy_day = day + 1

        # --- reconstruct transactions for this stock ---
        t = k
        day = n - 1
        while t > 0 and day > 0:
            if best_days[t][day]:
                buy_day, sell_day = best_days[t][day]
                profit = prices[sell_day - 1] - prices[buy_day - 1]
                all_transactions.append((stock_index + 1, buy_day, sell_day, profit))
                day = buy_day - 2  # go to the day before the buy_day
                t -= 1
            else:
                day -= 1

    # --- sort all transactions by profit in descending order  ---
    all_transactions.sort(key=lambda x: x[3], reverse=True )
    

    # --- pick top-k non-overlapping transactions ---
    selected = []
    for stock, buy1, sell1, profit in all_transactions:
        overlaps = False
        for _, buy2, sell2, _ in selected:
            if not (sell1 <= buy2 or buy1 >= sell2):  # overlapping interval
                overlaps = True
                break
        if not overlaps:
            selected.append((stock, buy1, sell1, profit))
            if len(selected) == k:
                break

    return selected



# --- Task-5 TEST CASE SECTION ---
if __name__ == "__main__":
    # Sample from the project description
    A = [
        [7, 1, 5, 3, 6],   
        [2, 9, 3, 7, 9],   
        [5, 8, 9, 1, 6],    
        [9, 3, 4, 8, 7]     
    ]
    m, n, k = len(A), len(A[0]), 3
    result = MultiTransactionStockTrading(A, m, n, k)
    
    print("Selected Non-Overlapping Transactions:")
    print("ID    (Stock, Buy, Sell)    Profit")
    print("-------------------------------------")
    for idx, (stock, buy, sell, profit) in enumerate(result, 1):
        print(f"T{idx:<4}      ({stock}, {buy}, {sell})          {profit}")
    
    # calculate total profit
    transactions = [(stock, buy, sell) for stock, buy, sell, profit in result]
    total_profit = sum(profit for _, _, _, profit in result)
    print("-------------------------------------")
    print( f"{transactions} with total profit = {total_profit}")


    print("\n=== Edge case tests ===\n")
   
    edge_cases = [       
        ("1: Empty matrix", [], 0, 0, 2),
        ("2: m <= 0", [[1, 2, 3]], 0, 3, 1),
        ("3: n <= 1", [[1]], 1, 1, 1),
        ("4: k <= 0", [[1, 2, 3]], 1, 3, 0),
        ("5: Row count mismatch", [[1, 2], [3, 4]], 3, 2, 1),
        ("6: Column count mismatch", [[1, 2, 3], [4, 5]], 2, 3, 1),
    ]

    for name, test_A, test_m, test_n, test_k in edge_cases:
        result = MultiTransactionStockTrading(test_A, test_m, test_n, test_k)
        print(f"{name}\nResult: {result}\n")  # expected: []






