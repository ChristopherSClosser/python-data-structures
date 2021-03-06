[![Build Status](https://travis-ci.org/ChristopherSClosser/python-data-structures.svg?branch=master)](https://travis-ci.org/ChristopherSClosser/python-data-structures)[![Coverage Status](https://coveralls.io/repos/github/ChristopherSClosser/python-data-structures/badge.svg?branch=master)](https://coveralls.io/github/ChristopherSClosser/python-data-structures?branch=master)

# Implement Data Structures In Python

- **Max Wolff & Chris Closser**
- **Version**: 1.0.6

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
- Implementing data structures
  - Single linked list (+JavaScript)
    - push() O(1)
    - pop() O(1)
    - search() O(n)
    - remove() O(n)
    - size() O(1)
    - display() O(n)
    - len() O(1)
  - Stack (+JavaScript)
    - push() O(1)
    - pop() O(1)
    - len() O(1)
  - Doubly linked list (inherits from SLL) (+JavaScript)
    - push() O(1)
    - pop() O(1)
    - search() O(n)
    - remove() O(n)
    - size() O(1)
    - display() O(n)
    - len() O(1)
    - append() O(1)
    - shift() O(1)  
  - Graph
    - nodes() O(n)
    - edges() O(1)
    - add_node() O(n)
    - add_edge() O(n)
    - del_node() O(n^2)
    - del_edge() O(n^2)
    - has_node() O(n)
    - neighbors() O(n)
    - adjacent() O(n)
    - traversals O(n)
    - dijkstra() O(n^2)
    - bellman() O(n^2)
  - Queue (inherits from DLL) (+JavaScript)
    - enqueue() O(1)
    - dequeue() O(1)
    - peek() O(1)
  - Dequeue (inherits from DLL) (+JavaScript)
    - popleft() O(1)
    - appendleft() O(1)
    - peekleft() O(1)
  - Priority queue (inherits from DLL) (+JavaScript)
    - pop() O(1)
    - peek() O(1)
    - insert O(n)
  - Binary min heap
    - push() O(1)
    - pop() O(1)
    - _shiftup() O(log-n)
    - _shiftdown() O(log-n)
    - _parent() O(log-n)
    - _leftchild() O(log-n)
    - _rightchild() O(log-n)
  - Binary search tree
    - insert() O(log-n)
    - search(), contains() O(log-n)
    - size() O(1)
    - depth() O(n)
    - balance() O(n)
    - traversals O(n)
      - breadth_first_traversal
      - in_order
      - pre_order
      - post_order
    - delete() O(n)
  - HashTable
    - hash() O(1)
    - set() O(n)
    - extend() O(n)
    - get() O(n)
  - Quick Sort
    - O(nlog(n))
  - Radix Sort
    - O(nk) - where k is the number of digits in the longest number

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
  You can fork or clone the repository [here](https://github.com/ChristopherSClosser/python-data-structures)  
  Python setup virtual environment and pytest  
  For JavaScript navigate to `js/` then `npm i`, run tests by entering `npm test`

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Python 2 and 3 packages:
  - pytest

JavaScript packages:
  - chai
  - mocha

## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Added functionality to add and delete some things.
-->
<pre>Oct 22 17 1300hrs&ensp;&ensp;-&ensp;&ensp;Init&ensp;&ensp;-  

Oct 22 17 1330hrs linked_list.py
                  test_linked_list.py
                  README

Oct 22 17 1430hrs linked_list.py
                  node - push
                  Testing
                  README

Oct 23 17 1600hrs pop - display
                  Testing
                  README

Oct 23 17 1630hrs size - remove
                  Testing
                  README

Oct 24 17 1500hrs search - __len__
                  Testing
                  README

Oct 24 17 1530hrs stack.py
                  Testing
                  README

Oct 25 17 1600hrs dll.py
                  Testing
                  README

Oct 25 17 1620hrs node prev pointer
                  Testing
                  README

Oct 25 17 1640hrs dll.pop
                  Testing
                  README

Oct 25 17 1700hrs dll.pop, dll.shift, dll.append, dll.remove
                  Testing
                  README

Oct 25 17 1800hrs que_ enqueue() dequeue() peek()
                  Testing
                  README

Oct 30 17 1300hrs deque
                  Testing
                  README
</pre>
