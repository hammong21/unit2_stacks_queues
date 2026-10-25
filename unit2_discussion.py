"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================  
OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).  
You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque

class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        self.stack = []

    def push(self, value):
        # TODO (Student): Implement the push operation.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.stack.append(value) # LIFO: Most recent item is added to the top/end
        print(f"Adding {value} to the bottle rack...")

    def pop(self):
        # TODO (Student): Implement the pop operation.
        # Add a short comment explaining why this operation supports LIFO behavior.
        if not self.is_empty():
            removed = self.stack.pop() # LIFO: Remove the item from the top/end
            print(f"Removing {removed} from the rack (LIFO).")
            return removed
        else:
            print("Error: The bottle rack is empty!")
            return None

    def peek(self):
        # TODO (Student): Implement the peek operation.
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Error: Cannot peek; the rack is empty!")
            return None

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.queue.append(value) # FIFO: New items wait at the back of the line
        print(f"Ordering {value}... adding to the tasting line.")

    def dequeue(self):
        # TODO (Student): Implement the dequeue operation.
        # Add a short comment explaining why this operation supports FIFO behavior.
        if not self.is_empty():
            removed = self.queue.popleft() # FIFO: Serve the item that arrived first
            print(f"Serving {removed} (FIFO).")
            return removed
        else:
            print("Error: No orders in the queue!")
            return None

    def front(self):
        # TODO (Student): Implement the front operation.
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Error: No order at the front of the line!")
            return None

    def is_empty(self):
        # TODO (Student): Implement the is_empty operation.
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0

def main():
    # 3. Improve the print statements so they clearly explain what is happening.
    print("=== UNIT 2: STACKS AND QUEUES ===")
    
    # Test data: Spirits
    spirits = ["Bourbon", "Gin", "Tequila", "Vodka"]

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")
    
    my_stack = Stack()
    for s in spirits:
        my_stack.push(s)
    
    print("\n--- Demonstrating LIFO sequence ---")
    while not my_stack.is_empty():
        my_stack.pop()
    
    print("\n--- Testing Edge Cases ---")
    print("Testing pop() on empty stack:")
    my_stack.pop()
    
    print("Testing peek() on empty stack:")
    my_stack.peek()
    
    print("\nTesting single-item stack persistence:")
    my_stack.push("Single Malt")
    my_stack.pop()
    print(f"Is stack empty now? {my_stack.is_empty()}")

    print("\n" + "="*30 + "\n")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")
    
    my_queue = Queue()
    for s in spirits:
        my_queue.enqueue(s)
    
    print("\n--- Demonstrating FIFO sequence ---")
    while not my_queue.is_empty():
        my_queue.dequeue()
    
    print("\n--- Testing Edge Cases ---")
    print("Testing dequeue() on empty queue:")
    my_queue.dequeue()
    
    print("Testing front() on empty queue:")
    my_queue.front()
    
    print("\nTesting single-item queue persistence:")
    my_queue.enqueue("Single Gin")
    my_queue.dequeue()
    print(f"Is queue empty now? {my_queue.is_empty()}")

    print("\n" + "="*30 + "\n")

    print("--- Real-World Scenario: Spirit Cellar Management ---")
    # TODO (Student): Real-world scenario application
    cellar_stock = Stack()
    shipping_line = Queue()

    cellar_stock.push("Aged Bourbon")
    cellar_stock.push("Reserve Vodka")
    
    shipping_line.enqueue("Gin shipment #1")
    shipping_line.enqueue("Tequila shipment #2")

    print("\nExecuting FIFO: Shipping the oldest order first...")
    shipping_line.dequeue()
    
    print("\nExecuting LIFO: Retrieving the last crate added to storage...")
    cellar_stock.pop()

if __name__ == "__main__":
    main()