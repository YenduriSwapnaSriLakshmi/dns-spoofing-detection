from app.dns_resolver import get_local_dns, get_trusted_dns
from app.asn_lookup import get_asn
from app.trust_score import calculate_trust
from app.classifier import classify
from app.utils import print_result, save_log
from app.config import DNS_SERVERS


def main():
    domain = input("Enter domain: ")

    local_ip, local_ttl = get_local_dns(domain)

    trusted_ip, trusted_ttl = None, None
    for server in DNS_SERVERS:
        trusted_ip, trusted_ttl = get_trusted_dns(domain, server)
        if trusted_ip:
            break

    asn = get_asn(local_ip) if local_ip else None

    score = calculate_trust(local_ip, trusted_ip, local_ttl, trusted_ttl, asn)
    status = classify(score)

    result = {
        "Domain": domain,
        "Local IP": local_ip,
        "Trusted IP": trusted_ip,
        "TTL": local_ttl,
        "ASN": asn,
        "Trust Score": score,
        "Status": status
    }

    print_result(result)
    save_log(result)

def process_domain(domain):
    local_ip, local_ttl = get_local_dns(domain)

    trusted_ip, trusted_ttl = None, None
    for server in DNS_SERVERS:
        trusted_ip, trusted_ttl = get_trusted_dns(domain, server)
        if trusted_ip:
            break

    asn = get_asn(local_ip) if local_ip else None

    score = calculate_trust(local_ip, trusted_ip, local_ttl, trusted_ttl, asn)
    status = classify(score)

    print("\n--- DNS Analysis ---")
    print("Domain:", domain)
    print("Local IP:", local_ip)
    print("Trusted IP:", trusted_ip)
    print("TTL:", local_ttl)
    print("ASN:", asn)
    print("Trust Score:", score)
    print("Status:", status)
if __name__ == "__main__":
    main()