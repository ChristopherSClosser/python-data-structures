
const Node = require('./list-node');

const SLL = module.exports = function() {
  this.head = null;
};

// O(1)
SLL.prototype.prepend = function(value) {
  let node = new Node(value);

  if(!this.head) {
    this.head = node;
    return this;
  }

  node.next = this.head;
  this.head = node;
  return this;
};

// O(n)
SLL.prototype.append = function(value) {
  let node = new Node(value);
  let lastNode = null;

  if(!this.head) {
    this.head = node;
    return this;
  }

  _setLastNode(this.head);
  lastNode.next = node;
  return this;

  function _setLastNode(node) {
    if(!node) return;
    lastNode = node;
    _setLastNode(node.next);
  }
};

// O(n)
SLL.prototype.reverse = function() {

  if(!this.head || !this.head.next) return this;

  let nodes = [],
    currentNode = this.head,
    node,
    reverseList = new SLL();

  while(currentNode) {
    nodes.push(currentNode);
    currentNode = currentNode.next;
  }

  reverseList.head = nodes.pop();
  currentNode = reverseList.head;

  node = nodes.pop();

  while(node) {
    node.next = null;
    currentNode.next = node;
    currentNode = currentNode.next;
    node = nodes.pop();
  }

  return reverseList;
};

// O(n)
SLL.prototype.remove = function(index) {
  let currentNode = this.head,
    i = 0, previous;

  //if list is empty, exit out
  if(!currentNode) return;

  //Check if first node
  if(index === 0){
    this.head = currentNode.next;
  }else{

    while(i < index){
      previous = currentNode;
      currentNode = currentNode.next;
      i++;
    }

    previous.next = currentNode.next;

    return previous;
  }
  /*
  // pass in the index you want to remove
  let list = a list with many nodes
  list.remove(some index)
  */
};

// O(n) this counts from the end
SLL.prototype.nthNode = function(n) {
  let currentNode = this.head,
    i = 1,
    nthNode;

  if(n <= 0) return;

  while(currentNode) {
    if(i === n) {
      nthNode = this.head;
    } else if (i - n > 0) {
      nthNode = nthNode.next;
    }
    i++;

    currentNode = currentNode.next;
  }
  return nthNode;
};

// O(n)
SLL.prototype.findMiddle = function(err) {
  if(err) console.error(err);
  let middleEnd = [];

  let i = 0,
    currentNode = this.head,
    middleNode = this.head;

  while(currentNode.next != null){
    i++;
    if(i % 2 == 0){
      middleNode = middleNode.next;
    }
    currentNode = currentNode.next;
  }

  if(i % 2 == 1){
    middleNode = middleNode.next;
  }
  middleEnd.push(middleNode, i);
  return middleEnd;
};
