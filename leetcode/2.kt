/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var l1 = l1
        var l2 = l2
        val l3 = ListNode(-1);
        var node3  = l3;
        var ex = 0;

        while (l1 != null || l2 != null){
            val nodeNext = ListNode(-1);
            node3.next = nodeNext;
            var a = 0;
            if (l1 != null) a = l1.`val`;
            var b = 0;
            if (l2 != null) b = l2.`val`;
            var c = a + b + ex;
            if (c < 10 )  ex = 0;
            if (c >= 10){
                c -= 10;
                ex = 1;
            }
            nodeNext.`val` = c;
            node3 = node3.next!!;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        if (ex == 1){
            var cur = ListNode(1);
            node3.next = cur;
        }

        return l3.next;
        
    }
}