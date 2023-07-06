from collections import deque

def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes  # Keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = deque([0])  # Start BFS from the first box

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]  # Get the keys in the current box

        for key in keys:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for further exploration

    # Check if all boxes can be visited starting from box 0
    return all(visited)


# Testing the code
boxes = [[1], [2], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [3], [], [4]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1], [2, 3], [4], [0], []]
print(canUnlockAll(boxes))  # Output: False
