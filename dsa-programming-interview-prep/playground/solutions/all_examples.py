from collections import Counter, OrderedDict, defaultdict, deque
import heapq


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


def is_valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def length_of_longest_substring(s):
    left = 0
    seen = {}
    best = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        best = max(best, right - left + 1)
    return best


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


def max_subarray(nums):
    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] != 1 or (r, c) in visited:
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
                dfs(r, c)
    return count


def top_k_frequent(nums, k):
    return [num for num, _ in Counter(nums).most_common(k)]


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1


def can_finish_courses(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque(i for i, degree in enumerate(indegree) if degree == 0)
    completed = 0
    while queue:
        node = queue.popleft()
        completed += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return completed == num_courses


def lru_cache_results(capacity, operations):
    cache = OrderedDict()
    output = []
    for operation in operations:
        if operation[0] == "get":
            key = operation[1]
            if key not in cache:
                output.append(-1)
            else:
                cache.move_to_end(key)
                output.append(cache[key])
        else:
            _, key, value = operation
            if key in cache:
                cache.move_to_end(key)
            cache[key] = value
            if len(cache) > capacity:
                cache.popitem(last=False)
    return output


def dedupe_latest(records):
    latest = {}
    for record in records:
        key = record["id"]
        if key not in latest or record["updated_at"] > latest[key]["updated_at"]:
            latest[key] = record
    return [latest[key] for key in sorted(latest)]


def merge_event_streams(streams):
    heap = []
    for stream_index, stream in enumerate(streams):
        if stream:
            heapq.heappush(heap, (stream[0]["ts"], stream_index, 0, stream[0]))
    result = []
    while heap:
        _, stream_index, event_index, event = heapq.heappop(heap)
        result.append(event)
        next_index = event_index + 1
        if next_index < len(streams[stream_index]):
            next_event = streams[stream_index][next_index]
            heapq.heappush(heap, (next_event["ts"], stream_index, next_index, next_event))
    return result


def find_scd2_errors(records):
    by_id = defaultdict(list)
    for record in records:
        by_id[record["id"]].append(record)
    errors = []
    for key, rows in by_id.items():
        current_count = sum(1 for row in rows if row["current"])
        rows = sorted(rows, key=lambda row: row["start"])
        has_overlap = False
        for prev, curr in zip(rows, rows[1:]):
            prev_end = prev["end"] or "9999-12-31"
            if curr["start"] < prev_end:
                has_overlap = True
                break
        if current_count != 1 or has_overlap:
            errors.append(key)
    return sorted(errors)

