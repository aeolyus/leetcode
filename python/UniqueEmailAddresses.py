class Solution:
    def numUniqueEmails(self, emails) -> int:
        res = set()
        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            local = local.split('+')[0]
            local = local.replace('.', '')
            res.add(local + '@' + domain)
        return len(res)
