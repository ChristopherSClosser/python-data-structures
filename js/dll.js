'use strict'

class Node{
  constructor(val, next = null, prev = null){
    this.val = val
    this.next = next
    this.prev = prev
  }
}

class DLL{
  constructor(){
    this.head = null
    this.tail = null
    this._counter = 0
  }

  push(val){
    let oldHead = this.head
    this.head = new Node(val, this.next = this.head)
    this._counter ++
    if(oldHead){
      oldHead.prev = this.head
    }else{
      this.tail = this.head
    }
  }

  append(val){
    let oldTail = this.tail
    this.tail = new Node(val, this.prev = this.tail)
    this._counter ++
    if(oldTail){
      oldTail.next = this.tail
    }else{
      this.head = this.tail
    }
  }

  pop(){
    if(this._counter === 0){
      this.head = null
      this.tail = null
    }
    if(!this.head){
      throw new Error('Node not in list.')
    }
    let output = this.head.val
    this.head = this.head.next
    if(this.head){
      this.head.prev = null
    }else{
      this.tail = null
    }
    this._counter --
    return output
  }

  shift(){
    if(this._counter === 0){
      this.head = null
      this.tail = null
    }
    if(!this.tail){
      throw new Error('Node not in list.')
    }
    let output = this.tail.val
    this.tail = this.tail.prev
    if(this.tail){
      this.tail.next = null
    }else{
      this.head = null
    }
    this._counter --
    return output
  }

  remove(val){
    if(!this.head){
      return 'List is empty.'
    }
    if(this.head.val === val){
      this.pop()
      return
    }
    let curr = this.head
    while(curr.next){
      if(curr.val === val){
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        this._counter --
        return
      }
      curr = curr.next
    }
    if(val === this.tail.val){
      this.shift()
      return
    }
    return 'Node not in list.'
  }
}

module.exports = DLL
