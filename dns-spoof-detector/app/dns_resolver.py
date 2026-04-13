import dns.resolver

def get_local_dns(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ip = result[0].to_text()
        ttl = result.rrset.ttl
        return ip, ttl
    except Exception as e:
        return None, None


def get_trusted_dns(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    print(resolver)
    try:
        result = resolver.resolve(domain, 'A')
        ip = result[0].to_text()
        ttl = result.rrset.ttl
        return ip, ttl
    except Exception:
        return None, None