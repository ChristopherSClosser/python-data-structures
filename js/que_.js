'use strict'

let DLL = require('./dll')

class Queue{
  constructor(){
    this.dll = new DLL()
  }

  enqueue(val){
    this.dll.push(val)
  }

  dequeue(){
    try{
      return this.dll.shift()
    }catch(e){
      return 'List is empty'
    }
  }

  peek(){
    if(this.dll.len === 0){
      return 'List is empty'
    }
    return this.dll.tail.val
  }

  size(){
    return this.dll.len
  }
}

module.exports = Queue
