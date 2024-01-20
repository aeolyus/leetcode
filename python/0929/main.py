from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            local = local.split('+')[0]
            local = local.replace('.', '')
            s.add(local+"@"+domain)
        return len(s)
