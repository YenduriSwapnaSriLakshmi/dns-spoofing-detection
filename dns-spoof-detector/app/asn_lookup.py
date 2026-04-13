from ipwhois import IPWhois

def get_asn(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        return res.get('asn', None)
    except Exception:
        return None