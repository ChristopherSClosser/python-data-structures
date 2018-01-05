'use strict'

const SLL = require('../sll')
const expect = require('chai').expect

describe('SLL class', function() {

  it('push adds node with value and assigns head.', function(){
    let tl = new SLL.LinkedList()
    tl.push(2)
    expect(tl.head.val).to.equal(2)
  })

  it('head.next should be null.', function(){
    let tl = new SLL.LinkedList()
    tl.push(2)
    expect(tl.head.next).to.be.null
  })

  it('push reassigns head correctly.', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    tl.push(2)
    expect(tl.head.val).to.equal(2)
  })

  it('push moves original head to next of new head', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    tl.push(2)
    expect(tl.head.next.val).to.equal(1)
  })

  it('pop returns head value', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    expect(tl.pop()).to.equal(1)
  })

  it('pop shifts head', function(){
    let tl = new SLL.LinkedList()
    tl.push('bob')
    tl.push(1)
    tl.pop()
    expect(tl.head.val).to.have.string('bob')
  })

  it('empty list returns null', function(){
    let tl = new SLL.LinkedList()
    expect(tl.pop()).to.be.null
  })

  it('size returns list length', function(){
    let tl = new SLL.LinkedList()
    expect(tl.size()).to.equal(0)
  })

  it('search returns "no such node" if not there', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    expect(tl.search(2)).to.have.string('No such Node')
  })

  it('search returns node', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    tl.push(2)
    expect(tl.search(1)).to.be.an.instanceof(SLL.Node).and.to.have.property('val').to.equal(1)
  })

  it('remove removes a single node', function(){
    let tl = new SLL.LinkedList()
    tl.push(1)
    tl.remove(1)
    expect(tl.head).to.be.null
  })

  it('remove works as expected', function(){
    let tl = new SLL.LinkedList()
    tl.push(2)
    tl.push(3)
    tl.push(4)
    tl.remove(3)
    expect(tl.head.next.val).to.equal(2)
  })

  it('display works as expected', function(){
    let tl = new SLL.LinkedList()
    for (var i = 0; i < 5; i++) {
      tl.push(i)
    }
    expect(tl.display()).to.be.string('4, 3, 2, 1, 0')
  })

  it('linked list iterable works as expected', function(){
    let tl = new SLL.LinkedList([1, 2, 3, 4])
    expect(tl.size()).to.equal(4)
  })

  it('remove on empty list returns undefined', function(){
    let tl = new SLL.LinkedList()
    expect(tl.remove()).to.be.undefined
  })

  it('remove returns string "no node with that value"', function(){
    let tl = new SLL.LinkedList([1, 2, 3, 4, 5])
    expect(tl.remove(9)).to.be.string('No Node with that value.')
  })
})
