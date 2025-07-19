# COP4533 Final Project – Stock Profit Maximization

This repository contains the final project for COP4533, focusing on algorithmic solutions to maximize profit from stock trading under various constraints. The project is divided into multiple tasks, each targeting a specific variation of the stock trading problem using different algorithmic strategies.

---

## Problem Variants

### Problem 1: Single Transaction

- **Goal**: Find the best buy/sell pair for a single transaction to maximize profit.
- **Input**: A matrix `A[m][n]` representing stock prices of `m` stocks over `n` days.
- **Output**: A tuple `(stock, buyDay, sellDay, profit)` with the optimal trade.
- **Constraint**: Only one transaction allowed per stock.

### Problem 2: At Most K Transactions

- **Goal**: Maximize profit using up to `k` non-overlapping transactions.
- **Input**: Matrix `A[m][n]` and an integer `k`.
- **Output**: A list of at most `k` transactions `(stock, buyDay, sellDay)`.

### Problem 3: Cooldown Constraint

- **Goal**: Maximize profit with a cooldown period `c` after each sale.
- **Input**: Matrix `A[m][n]` and an integer `c` (cooldown days).
- **Output**: A sequence of transactions that respect the cooldown rule.

---

## Tasks Overview

| Task | Description                             | Time Complexity |
| ---- | --------------------------------------- | --------------- |
| 1    | Brute Force for Problem 1               | O(m·n²)         |
| 2    | Greedy for Problem 1                    | O(m·n)          |
| 3    | Dynamic Programming for Problem 1       | O(m·n)          |
| 4    | DP for Problem 2 (Inefficient)          | O(m·n²·k)       |
| 5    | Optimized DP for Problem 2              | O(m·n·k)        |
| 6    | DP for Problem 3 with cooldown tracking | O(m·n²)         |
| 7    | Optimized DP for Problem 3              | O(m·n)          |

---

## Project Milestones

**Milestone 1:** Understanding the Problems
Analyzed each variation of the stock trading problem.
Manually solved example cases to verify expected outcomes.

**Milestone 2:** Algorithm Design
Developed well-structured pseudocode for selected tasks.
Compare brute-force, greedy, and dynamic programming approaches.

**Milestone 3:** Algorithm Implementation
Translated pseudocode into working code using Python/C++/Java.

**Final Presentation**
Recorded walkthrough of pseudocode and design decisions.
Highlight the reasoning behind design choices
