'use strict'

let DLL = require('../dll')
let chai = require('chai')
let expect = chai.expect

describe('dll.js tests', function() {
  it('dll have empty head on creation', function(){
    let dll = new DLL()
    expect(dll.head).to.be.null
  })

  it('push adds new node', function(){
    let dll = new DLL()
    dll.push('test')
    expect(dll.head.val).to.be.string('test')
  })

  it('push moves head along', function(){
    let dll = new DLL()
    dll.push(1)
    dll.push(2)
    expect(dll.head.val).to.equal(2)
  })

  it('old head points to new head', function(){
    let dll = new DLL()
    dll.push('test')
    dll.push('wow')
    expect(dll.head.next.prev.val).to.be.string('wow')
  })

  it('pop removes head', function(){
    let dll = new DLL()
    dll.push('val')
    let res = dll.pop()
    expect(res).to.be.string('val')
  })

  it('pop moves head along', function(){
    let dll = new DLL()
    dll.push('val')
    dll.push('wow')
    dll.pop()
    expect(dll.head.val).to.equal('val')
  })

  it('pop throws error on empty list', function(){
    let dll = new DLL()
    expect(dll.pop).to.throw(Error)
  })

  it('append adds tail', function(){
    let dll = new DLL()
    dll.append('dip')
    expect(dll.tail.val).to.be.string('dip')
  })

  it('append moves tail along appropriately', function(){
    let dll = new DLL()
    dll.append('jim')
    dll.append('jon')
    dll.append('bob')
    expect(dll.tail.val).to.be.string('bob')
  })

  it('shift removes tail node', function(){
    let dll = new DLL()
    dll.append('bob')
    dll.push('wow')
    dll.shift()
    expect(dll.tail.val).to.be.string('wow')
  })

  it('shift throws error on empty list', function(){
    let dll = new DLL()
    expect(dll.shift).to.throw(Error)
  })

  it('empty list remove returns string', function(){
    let dll = new DLL()
    expect(dll.remove()).to.be.string('List is empty.')
  })

  it('remove returns string if node not in list', function(){
    let dll = new DLL()
    dll.push(1)
    expect(dll.remove('jim')).to.be.string('Node not in list.')
 })

  it('remove pops head', function(){
    let dll = new DLL()
    dll.push(1)
    expect(dll.remove(1)).to.be.undefined
  })
})
