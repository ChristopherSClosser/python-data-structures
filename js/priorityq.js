'use strict'

class PriorityQ{
  constructor(){
    this.priorityDict = {}
    this.len = 0
  }

  insert(value, priority = 0){
    if(this.priorityDict[priority] !== undefined){
      this.priorityDict[priority].push(value)
    }else{
      this.priorityDict[priority] = priority
      this.priorityDict[priority] = []
      this.priorityDict[priority].push(value)
    }
    this.len ++
  }

  pop(){
    if (this.len === 0){
      throw new Error('There is nothing to pop')
    }
    let highestPriority = Math.max.apply(Math, Object.keys(this.priorityDict).map(Number))
    if(this.priorityDict[highestPriority].length === 0){
      delete this.priorityDict[highestPriority]
      highestPriority = Math.max.apply(Math, Object.keys(this.priorityDict).map(Number))
    }
    let popped = this.priorityDict[highestPriority].shift()
    this.len --
    return popped
  }

  peek(){
    if(this.len === 0){
      return
    }
    let highestPriority = Math.max.apply(Math, Object.keys(this.priorityDict).map(Number))
    return this.priorityDict[highestPriority][0]
  }
}

function isEmptyObject(obj){
  for(var name in obj){
    return false
  }
  return true
}

module.exports = PriorityQ
