'use strict'

const DEQUE = require('../deque')
const CHAI = require('chai')
const expect = CHAI.expect

describe('deque.js tests', function(){
  it('append adds a value', function(){
    let deq =  new DEQUE()
    deq.append('wow')
    expect(deq.size()).to.equal(1)
  })

  it('append adds multiple values', function(){
    let deq =  new DEQUE()
    deq.append(1)
    deq.append(2)
    expect(deq.size()).to.equal(2)
  })

  it('popleft removes first node added', function(){
    let deq =  new DEQUE()
    deq.append('first')
    deq.append('second')
    expect(deq.popleft()).to.be.string('first')
  })

  it('popleft throws error on empty deque', function(){
    let deq =  new DEQUE()
    expect(deq.popleft).to.throw(Error)
  })

  it('peek returns next node to be dequed', function(){
    let deq =  new DEQUE()
    deq.appendleft('bill')
    expect(deq.peek()).to.be.string('bill')
  })

  it('peek returns null on empty deque', function(){
    let deq =  new DEQUE()
    expect(deq.peek()).to.equal('Nothing in the list')
  })

  it('size returns zero on empty deque', function(){
    let deq =  new DEQUE()
    expect(deq.size()).to.equal(0)
  })

  it('appendleft adds node to front', function(){
    let deq =  new DEQUE()
    deq.appendleft(1)
    deq.appendleft(2)
    deq.appendleft('left')
    expect(deq.dll.head.val).to.be.string('left')
  })

  it('appendleft adds multiple nodes', function(){
    let deq =  new DEQUE()
    deq.appendleft('one')
    deq.appendleft('two')
    expect(deq.size()).to.equal(2)
  })

  it('pop removes node', function(){
    let deq =  new DEQUE()
    deq.append('bob')
    deq.append('tom')
    expect(deq.pop()).to.be.string('tom')
  })

  it('pop throws error on empty deque', function(){
    let deq =  new DEQUE()
    expect(deq.pop).to.throw(Error)
  })

  it('peekleft show head node value', function(){
    let deq =  new DEQUE()
    deq.append('1')
    deq.appendleft(1)
    expect(deq.peekleft()).to.equal(1)
  })

  it('peekleft returns null on empty deque', function(){
    let deq =  new DEQUE()
    expect(deq.peekleft()).to.equal('Nothing in the list')
  })
})
