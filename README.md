# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Overview

This project explored the implementation and application of two fundamental linear data structures: the Stack, which operates on a Last-In, First-Out (LIFO) basis, and the Queue, which operates on a First-In, First-Out (FIFO) basis.

## Implementation Summary

The following requirements were successfully implemented in unit2_discussion.py:

- Stack Operations: Implemented push, pop, and peek operations to manage a "Bottle Rack" simulation.
- Queue Operations: Implemented enqueue, dequeue, and front operations using collections.deque to simulate a "Tasting Line."
- Behavioral Demonstrations: Demonstrated LIFO behavior by popping spirits in reverse order of addition and FIFO behavior by serving spirits in the exact order they were ordered.
- Edge Case Handling: Developed and tested checks for operations performed on empty structures, ensuring the program provides informative error messages rather than crashing.
- Real-World Scenario: Created a "Spirit Cellar Management" simulation, utilizing a stack for deep-storage piling and a queue for processing shipping orders.

## My Reflection

While completing this assignment, I deepened my understanding of linear data structures and their specific access patterns. I learned how to utilize Python's list for a stack and the more efficient collections.deque for a queue to ensure that removals from the front of the line occurred in O(1) (constant) time.

One of the primary challenges I encountered was ensuring that the program remained robust when handling edge cases, such as attempting to pop from an empty stack. I overcame this by implementing is_empty() helper methods to validate the state of the data structure before attempting any removal or peek operation.

The fundamental difference between stacks and queues is the order of retrieval. In a real-world application like my spirit cellar, a stack is ideal for "Last-In, First-Out" scenarios—such as piling crates in a narrow storage area where only the top item is accessible. Conversely, a queue is essential for "First-In, First-Out" scenarios, such as a shipping line, where the first order placed must be the first order fulfilled to ensure freshness, fairness and efficiency.

