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

Binary trees can be categorized into various types based on their structure, properties, and usage. Here are some common types of binary trees:

<H2>Full Binary Tree:</H2>

In a full binary tree, every node has either 0 or 2 children.
There are no nodes with only one child.
Every level, except possibly the last, is fully filled.

<H2>Complete Binary Tree:</H2>

In a complete binary tree, all levels are completely filled except possibly for the last level.
In the last level, nodes are filled from left to right without any gaps.
Complete binary trees are typically used in heap data structures.

<H2>Perfect Binary Tree:</H2>

A perfect binary tree is both full and complete.
All internal nodes have exactly two children.
All leaf nodes are at the same level.

<H2>Balanced Binary Tree:</H2>

A balanced binary tree is a tree where the height of the two subtrees of any node never differs by more than one.
Balancing ensures that the height of the tree is logarithmic in terms of the number of nodes, leading to efficient operations.
Degenerate (or Pathological) Binary Tree:

In a degenerate binary tree, each parent node has only one associated child node.
It essentially becomes a linked list.
Degenerate trees have poor time complexities for operations like searching, insertion, and deletion.

<H2>Binary Search Tree (BST):</H2>

A binary search tree is a binary tree where the left child of a node has a value less than the parent node, and the right child has a value greater than the parent node.
BSTs allow for efficient searching, insertion, and deletion operations.
<H2>Threaded Binary Tree:</H2>

In a threaded binary tree, additional pointers called "threads" are added to the nodes to make traversal easier.
Threads link nodes according to their inorder successor or predecessor.
Threaded trees save space by eliminating the need for explicit null pointers.
These are some of the common types of binary trees. Each type has its unique characteristics and use cases, making them suitable for different scenarios and applications.

Binary trees can be categorized into various types based on their structure, properties, and usage. Here are some common types of binary trees:

<H2>Full Binary Tree:</H2>

In a full binary tree, every node has either 0 or 2 children.
There are no nodes with only one child.
Every level, except possibly the last, is fully filled.

<H2Complete Binary Tree:</H2>

In a complete binary tree, all levels are completely filled except possibly for the last level.
In the last level, nodes are filled from left to right without any gaps.
Complete binary trees are typically used in heap data structures.

<H2>Perfect Binary Tree:</H2>

A perfect binary tree is both full and complete.
All internal nodes have exactly two children.
All leaf nodes are at the same level.

<H2>Balanced Binary Tree:</H2>

A balanced binary tree is a tree where the height of the two subtrees of any node never differs by more than one.
Balancing ensures that the height of the tree is logarithmic in terms of the number of nodes, leading to efficient operations.

<H2>Degenerate (or Pathological) Binary Tree:</H2>

In a degenerate binary tree, each parent node has only one associated child node.
It essentially becomes a linked list.
Degenerate trees have poor time complexities for operations like searching, insertion, and deletion.

<H2>Binary Search Tree (BST):</H2>

A binary search tree is a binary tree where the left child of a node has a value less than the parent node, and the right child has a value greater than the parent node.
BSTs allow for efficient searching, insertion, and deletion operations.

<H2>Threaded Binary Tree:</H2>

In a threaded binary tree, additional pointers called "threads" are added to the nodes to make traversal easier.
Threads link nodes according to their inorder successor or predecessor.
Threaded trees save space by eliminating the need for explicit null pointers.
These are some of the common types of binary trees. Each type has its unique characteristics and use cases, making them suitable for different scenarios and applications.









