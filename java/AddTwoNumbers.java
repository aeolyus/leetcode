public class AddTwoNumbers {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
                                                          return addLists(l1, l2, 0);
                                                                                      }

    static ListNode addLists(ListNode l1, ListNode l2, int carry) {
        ListNode head = new ListNode(0);
        ListNode res = head;
        while (l1 != null || l2 != null) {
            int sum = carry;
            sum += l1 == null ? 0 : l1.val;
            sum += l2 == null ? 0 : l2.val;
            res.next = new ListNode(sum % 10);
            carry = sum / 10;
            l1 = l1 == null ? l1 : l1.next;
            l2 = l2 == null ? l2 : l2.next;
            res = res.next;
        }
        if (carry > 0) {
            res.next = new ListNode(carry);
        }
        return head.next;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(9);
        l1.next = new ListNode(9);
        ListNode l2 = new ListNode(1);
        ListNode ans = addTwoNumbers(l1, l2);
        while (ans != null) {
            System.out.println(ans.val);
            ans = ans.next;
        }
    }
}
