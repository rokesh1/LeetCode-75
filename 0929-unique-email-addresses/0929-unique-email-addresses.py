class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent = set()
        for email in emails:
            local,domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            cleaned_email = local +"@"+ domain
            sent.add(cleaned_email)
        return len(sent)

        