<h1>DSA Implemention Using Python</h1>
<h1>What is really Meant by Data Structure</h1>
A data structure, in the realm of computer science, is a specific way of organizing and storing data in a computer system. It defines not only how data is arranged but also the operations that can be performed on it efficiently. Imagine it like organizing items in your home - different structures (shelves, boxes, drawers) suit different objects and tasks (finding a specific book, storing clothes).

Here are some key aspects of data structures:

<h2>Purpose:</h2>

Efficient access: The main goal is to enable efficient retrieval, manipulation, and update of data. Different structures provide varying levels of access speed depending on the type of operations needed.
Memory management: Efficient storage utilization is crucial, especially for large data sets. Some structures use memory contiguously, while others link elements dynamically.

<h2>Types:</h2>

Linear: Elements are arranged in a sequence, like arrays, linked lists, stacks, and queues. Efficient for insertions and deletions at specific points but might be slow for random access.
Non-linear: Elements are linked in more complex relationships, like trees, graphs, and hash tables. Offer efficient searching and retrieval based on key values but might be slower for sequential access.

<h2>Choosing the right one:</h2>

The optimal data structure depends on the specific needs of your program or application. Consider factors like:

Type of data: Numbers, text, objects, etc.
Operations required: Frequent insertions, deletions, searches, sorting?
Performance requirements: Speed, memory usage, scalability.

<h2>Benefits:</h2>

Efficient algorithms: Choosing the right data structure often leads to more efficient algorithms and faster program execution.
Organized code: Well-defined data structures improve code readability and maintainability.
Modular design: Complex systems can be built by combining simpler data structures.
<h1>Binary Search Tree</h1>
Algorithm to search for a key in a given Binary Search Tree:
Let’s say we want to search for the number X, We start at the root. Then:

We compare the value to be searched with the value of the root. 
If it’s equal we are done with the search if it’s smaller we know that we need to go to the left subtree because in a binary search tree all the elements in the left subtree are smaller and all the elements in the right subtree are larger. 
Repeat the above step till no more traversal is possible
If at any iteration, key is found, return True. Else False.
