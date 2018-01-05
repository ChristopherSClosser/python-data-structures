'use strict'

const SLL = require('./sll')

class Stack {
  constructor(isIterable = null){
    this.sll = new SLL.LinkedList()
    if(Array.isArray(isIterable)){
      isIterable.map(x => this.push(x))
    }
  }

  push(val){
    this.sll.push(val)
  }

  pop(){
    return this.sll.pop()
  }

  size(){
    return this.sll.size()
  }
}

module.exports = Stack
