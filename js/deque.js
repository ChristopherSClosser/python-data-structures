'use strict'

const DLL = require('./dll')

class Deque{
  constructor(){
    this.dll = new DLL()
  }

  append(val){
    this.dll.append(val)
  }

  appendleft(val){
    this.dll.push(val)
  }

  pop(){
    try{
      return this.dll.shift()
    }catch(e){
      throw new Error('Nothing in list')
    }
  }

  popleft(){
    try{
      return this.dll.pop()
    }catch(e){
      throw new Error('Nothing in the list')
    }
  }

  peek(){
    if(this.dll.len === 0){
      return 'Nothing in the list'
    }
    return this.dll.tail.val
  }

  peekleft(){
    if(this.dll.len === 0){
      return 'Nothing in the list'
    }
    return this.dll.head.val
  }

  size(){
    return this.dll.len
  }
}

module.exports = Deque
