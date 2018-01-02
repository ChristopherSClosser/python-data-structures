'use strict'

class Node {
  constructor(val, next = null){
    this.val = val
    this.next = next
  }
}

class LinkedList {
  constructor(iterable = null) {
    this.head = null
    this._length = 0

    if(Array.isArray(iterable)){
      iterable.forEach(x => this.push(x))
    }
  }

  push(val){
    this.head = new Node(val, this.head)
    this._length ++
  }

  pop(){
    if(this.head === null){
      return null
    }

    let res = this.head
    this.head = this.head.next
    this._length --

    return res.val
  }

  search(val){
    let _search = this.head

    try{
      while(this.head){
        if(val === _search.val){
          return _search
        }else{
          _search = _search.next
        }
      }
    }catch(e){
      return 'No such Node'
    }
  }

  remove(val){
    let currNode = this.head
    let prevNode = null
    let found = false

    try{
      while(currNode && !found){
        if(val === currNode.val){
          found = true
        }else{
          prevNode = currNode
          currNode = currNode.next
        }
      }

      if(prevNode === null){
        this.pop()
      }else if(currNode.next === null){
        prevNode.next = null
      }else{
        prevNode.next = currNode.next
      }
    }catch(e){
      return 'No Node with that value.'
    }
    this._length --
  }

  display(){
    let node = this.head
    let res = []

    while(node){
      res.push(node.val)
      node = node.next
    }
    return res.join(', ')
  }

  size(){
    return this._length
  }
}

module.exports = {LinkedList, Node}
