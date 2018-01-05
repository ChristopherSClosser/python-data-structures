'use strict'

let Stack = require('../stack')
const SLL = require('../sll')
let chai = require('chai')
let expect = chai.expect

describe('stack.js tests', function(){
  it('push adds new value', function(){
    let s = new Stack()
    s.push(2)
    expect(s.sll.head.val).to.equal(2)
  })

  it('push moves head along appropriately', function(){
    let s = new Stack()
    s.push(1)
    s.push(2)
    expect(s.sll.head.val).to.equal(2)
  })

  it('push moves old head to next of new head', function(){
    let s = new Stack()
    s.push(1)
    s.push(2)
    expect(s.sll.head.next.val).to.equal(1)
  })

  it('pop returns head value', function(){
    let s = new Stack()
    s.push('wow')
    expect(s.pop()).to.have.string('wow')
  })

  it('pop shifts head', function(){
    let s = new Stack()
    s.push('bill')
    s.push(1)
    s.pop()
    expect(s.sll.head.val).to.have.string('bill')
  })

  it('size returns Stack length', function(){
    let s = new Stack()
    expect(s.size()).to.equal(0)
  })

  it('stack takes an iterable', function(){
    let s = new Stack([1, 2, 3, 4])
    expect(s.size()).to.equal(4)
  })

  it('empty stack returns null', function(){
    let tl = new Stack()
    expect(tl.pop()).to.be.null
  })

  it('size returns stack length', function(){
    let tl = new Stack()
    expect(tl.size()).to.equal(0)
  })

  it('search returns "no such node" if not there', function(){
    let tl = new Stack()
    tl.push(1)
    expect(tl.sll.search(2)).to.have.string('No such Node')
  })

  it('search returns node', function(){
    let tl = new Stack()
    tl.push(1)
    tl.push(2)
    expect(tl.sll.search(1)).to.be.an.instanceof(SLL.Node).and.to.have.property('val').to.equal(1)
  })

  it('remove removes a single node', function(){
    let tl = new Stack()
    tl.push(1)
    tl.sll.remove(1)
    expect(tl.sll.head).to.be.null
  })

  it('remove works as expected', function(){
    let tl = new Stack()
    tl.push(2)
    tl.push(3)
    tl.push(4)
    tl.sll.remove(3)
    expect(tl.sll.head.next.val).to.equal(2)
  })

  it('display works as expected', function(){
    let tl = new Stack()
    for (var i = 0; i < 5; i++) {
      tl.push(i)
    }
    expect(tl.sll.display()).to.be.string('4, 3, 2, 1, 0')
  })

  it('linked stack iterable works as expected', function(){
    let tl = new Stack([1, 2, 3, 4])
    expect(tl.size()).to.equal(4)
  })

  it('remove on empty stack returns undefined', function(){
    let tl = new Stack()
    expect(tl.sll.remove()).to.be.undefined
  })

  it('remove returns string "no node with that value"', function(){
    let tl = new Stack([1, 2, 3, 4, 5])
    expect(tl.sll.remove(9)).to.be.string('No Node with that value.')
  })
})
