'use strict'

let Que = require('../que_')
let chai = require('chai')
let expect = chai.expect

describe('que_.js tests', function(){
  it('enqueue adds value', function(){
    let q = new Que()
    q.enqueue('this')
    expect(q.dll.head.val).to.be.string('this')
  })

  it('enqueue adds multiple values', function(){
    let q = new Que()
    q.enqueue('this')
    q.enqueue('is')
    q.enqueue('enqueued')
    expect(q.dll.tail.val).to.be.string('this')
  })

  it('dequeue removes first node inserted', function(){
    let q = new Que()
    q.enqueue('remove')
    expect(q.dequeue()).to.be.string('remove')
  })

  it('dequeue removes first node inserted after multiple', function(){
    let q = new Que()
    q.enqueue('this')
    q.enqueue('is')
    q.enqueue('enqueued')
    expect(q.dequeue()).to.be.string('this')
  })

  it('dequeue returns undefined on empty queue', function(){
    let q = new Que()
    expect(q.dequeue()).to.be.string('List is empty')
  })

  it('peek returns value of next node to be dequeued', function(){
    let q = new Que()
    q.enqueue('this')
    q.enqueue('is')
    q.enqueue('enqueued')
    expect(q.peek()).to.be.string('this')
  })

  it('peek returns undefined on empty queue', function(){
    let q = new Que()
    expect(q.peek()).to.be.string('List is empty')
  })

  it('size returns 0 on empty queue', function(){
    let q = new Que()
    expect(q.size()).to.equal(0)
  })

  it('size returns size of queue', function(){
    let q = new Que()
    q.enqueue('this')
    q.enqueue('is')
    q.enqueue('enqueued')
    expect(q.size()).to.equal(3)
  })
})
