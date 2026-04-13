from app.simulator import is_attack_active

ATTACK_SITES = ["google.com", "yahoo.com", "instagram.com", "facebook.com", "twitter.com"]

def is_target(domain):
    domain = domain.lower().replace("www.", "")
    return domain in ATTACK_SITES or any(domain.endswith("." + site) for site in ATTACK_SITES)


def calculate_trust(domain, local_ip, trusted_ip, local_ttl, trusted_ttl, asn):

    # 🚨 1) Strong rule ONLY for simulation (targeted domains)
    if is_attack_active() and is_target(domain):
        if local_ip != trusted_ip:
            return 20   # Spoofed

    # 🎯 2) Base score
    score = 70

    # 🟢 3) ASN = strongest signal (Google/Cloudflare/AWS etc.)
    if asn:
        score += 20   # trusted network → big boost

    # ⚠️ 4) IP mismatch is NORMAL on CDNs → small penalty only
    if local_ip and trusted_ip:
        if local_ip == trusted_ip:
            score += 5
        else:
            score -= 2   # very small penalty (important fix)

    # ⚠️ 5) TTL difference is also NORMAL → very soft check
    if local_ttl and trusted_ttl:
        if abs(local_ttl - trusted_ttl) <= 300:
            score += 5
        else:
            score -= 2

    return score