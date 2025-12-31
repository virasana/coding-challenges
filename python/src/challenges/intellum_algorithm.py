import heapq

def max_tasks(tasks):
    # sort tasks by deadline, as the earliest deadline is most urgent
    tasks = sorted(tasks, key=lambda task: task[1])

    total_time = 0
    max_heap = []

    for duration, deadline in tasks:
        total_time += duration
        # push the current task
        heapq.heappush(max_heap, -duration)

        # did we break the deadline of the current task?
        if total_time > deadline:
            # yes, we broke it! now bosh the current task into the heap
            # we need to replace the longest duration task with the current one
            # remember, duration is not our goal - we want to free up the max room
            # so therefore removing the task with longest duration makes sense
            # intuition: getting max number of customers to fill tables at a restaurant
            # we would want to remove a family of three from a four-table place
            # and replace that with a four-family sitting
            longest = -heapq.heappop(max_heap)
            total_time -= longest

    return len(max_heap)

if __name__ == '__main__':
    tasks = [(3, 7), (1, 2), (2, 5), (4, 6)]
    print(max_tasks(tasks))  # Output: 3


# import heapq

# def max_tasks(tasks):
#     # Sort tasks by deadline (earliest first)
#     tasks.sort(key=lambda task: task[1])

#     total_time = 0
#     max_heap = []  # store negative durations to simulate a max-heap

#     for duration, deadline in tasks:
#         total_time += duration
#         heapq.heappush(max_heap, -duration)

#         # If we exceed the deadline, remove the longest task so far
#         if total_time > deadline:
#             longest = -heapq.heappop(max_heap)
#             total_time -= longest

#     # Number of tasks successfully scheduled
#     return len(max_heap)


# # Example usage [(duration, deadline)]
# tasks = [(3, 7), (1, 2), (2, 5), (4, 6)]
# print(max_tasks(tasks))  # Output: 3
