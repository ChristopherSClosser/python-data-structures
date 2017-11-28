'use strict';

const SLL = require('../sll');
const expect = require('chai').expect;

describe('SLL.prototypes', function() {

  describe('.reverse()', function() {
    let list = new SLL();
    list.append(1); list.append(2); list.append(3);
    list.append(4); list.append(5);
    let newList = list.reverse();

    it('should return a new list', () => {
      expect(newList).to.exist;
    });

    it('should reverse the order of the list', () => {
      expect(newList.head.val).to.equal(5);
    });

    it('should make the previous head.next null', () => {
      expect(newList.head.next.next.next.next.val).to.deep.equal(1);
      expect(newList.head.next.next.next.next.next).to.deep.equal(null);
    });
  });

  describe('.findMiddle()', function() {
    let list = new SLL();
    list.append(1); list.append(2); list.append(3);
    list.append(4); list.append(5);

    it('should return the middle node in an odd list', () => {
      let middle = list.findMiddle();
      let mid = middle[0];
      // if list is odd it will return the middle
      expect(mid.val).to.equal(3);
    });

    it('should return the greater middle node in an even list', () => {
      list.append(6);
      let middle = list.findMiddle();
      let mid = middle[0];

      expect(mid.val).to.equal(4);
    });

    it('should return the index of the last node', () => {
      let middle = list.findMiddle();
      let midIndex = middle[1];

      expect(midIndex).to.equal(5);
    });
  });

  describe('.nthNode()', function() {
    let list = new SLL();
    list.append(1); list.append(2); list.append(3);
    list.append(4); list.append(5);

    it('should return the last node', () => {
      let findLast = list.nthNode(1);

      expect(findLast.next).to.equal(null);
    });

    it('should return the second to the last node', () => {
      let find = list.nthNode(2);

      expect(find.next.next).to.equal(null);
    });

    it('should return list head node', () => {
      let find = list.nthNode(5);

      expect(find).to.equal(list.head);
    });
  });

  describe('.remove()', function() {
    let list = new SLL();
    list.append(1); list.append(2); list.append(3);
    list.append(4); list.append(5);

    it('should remove the head', () => {
      list.remove(0);

      expect(list.head.val).to.deep.equal(2);
    });

    it('should remove the last node', () => {
      list.remove(3);

      expect(list.head.next.next.next).to.deep.equal(null);
    });

    it('should have only two nodes left', () => {
      list.remove(1);

      expect(list.head.next.next).to.deep.equal(null);
    });
  });
});
