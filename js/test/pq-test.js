'use strict'

let Priority = require('../priorityq')
let chai = require('chai')
let expect = chai.expect

describe('priorityQ.js tests', function(){
  it('pop removes highest priority', function(){
    let pq = new Priority()
    for(var i = 0; i < 3; i++){
      pq.insert(i)
    }
    pq.insert(8, 2)
    pq.insert(10, 2)
    expect(pq.pop()).to.equal(8)
  })

  it('pop removes properly', function(){
    let pq = new Priority()
    for(var i = 0; i < 3; i++){
      pq.insert(i)
    }
    pq.insert(8, 2)
    pq.insert(10, 2)
    pq.pop()
    pq.pop()
    pq.pop()
    pq.pop()
    expect(pq.pop()).to.equal(2)
  })

  it('check highest priority', function(){
    let pq = new Priority()
    for(var i = 0; i < 3; i++){
      for(var ii = 0; ii < 10; ii++){
        pq.insert(ii, i)
      }
    }
    pq.insert(30, 10)
    expect(pq.peek()).to.equal(30)
  })

  it('check length of priority', function(){
    let pq = new Priority()
    for(var i = 0; i < 3; i++){
      pq.insert(i)
    }
    pq.insert(8, 2)
    pq.insert(10, 2)
    expect(pq.len).to.equal(5)
  })

  it('check length of priority after pop', function(){
    let pq = new Priority()
    for(var i = 0; i < 5; i++){
      pq.insert(i)
    }
    pq.pop()
    expect(pq.len).to.equal(4)
  })

  it('pop raises error on new priority queue', function(){
    let pq = new Priority()
    expect(pq.pop).to.throw(Error)
  })

  it('peek shows highest priority', function(){
    let pq = new Priority()
    for(var i = 0; i < 3; i++){
      pq.insert(i)
    }
    pq.insert(8, 2)
    pq.insert(10, 2)
    pq.insert(0, 33)
    expect(pq.peek()).to.equal(0)
  })

  it('peek returns undefined if priority queue is empty', function(){
    let pq = new Priority()
    expect(pq.peek()).to.be.undefined
  })
})
