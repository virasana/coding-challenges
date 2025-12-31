# Coding Challenge: Optimal Task Scheduling

## Problem Statement

You are given a list of tasks. Each task has:
- a **duration** (positive integer)
- a **deadline** (positive integer)

Each task must be completed **on or before its deadline**.  
You may complete **only one task at a time** (no parallel execution).

Your goal is to determine the **maximum number of tasks** that can be completed without missing any deadlines.

---

## Input

A list of tasks, where each task is represented as a pair:

(duration, deadline)

### Example
[(3, 7), (1, 2), (2, 5), (4, 6)]

---

## Output

Return a single integer representing the **maximum number of tasks** that can be completed on time.

### Example Output
3

---

## Explanation

One valid schedule is:
- Task (1, 2) → finishes at time 1
- Task (2, 5) → finishes at time 3
- Task (3, 7) → finishes at time 6

All deadlines are met. Adding the task (4, 6) would cause a deadline to be missed.

---

## Constraints

- Number of tasks: 1 ≤ n ≤ 100,000
- Task duration: 1 ≤ duration ≤ 100,000
- Deadline: 1 ≤ deadline ≤ 1,000,000,000

---

## Requirements

- Solve the problem **algorithmically**
- Target time complexity: **O(n log n)**
- Use appropriate data structures
- Be prepared to explain **why your solution is correct**

---

## Follow-Up Questions (Interview Style)

- Why does your approach produce an optimal result?
- What data structure did you choose and why?
- How does your solution scale with large inputs?
- Can you describe a case where a greedy choice fails if implemented incorrectly?

---

## Optional Extension

Modify your solution to return the **actual set of tasks** that are completed, not just the count.
