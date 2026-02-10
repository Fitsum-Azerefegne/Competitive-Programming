class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_hashmap = defaultdict(int)
        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                visit_hashmap[subdomain] += count

        result = []
        for domain, counts in visit_hashmap.items():
            result.append(f"{counts} {domain}")
        return result  
