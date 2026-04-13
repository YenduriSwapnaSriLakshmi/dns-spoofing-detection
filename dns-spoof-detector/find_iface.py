 
from scapy.all import get_if_list, get_if_addr

for iface in get_if_list():
    try:
        ip = get_if_addr(iface)
        if ip != "0.0.0.0":
            print(iface, "→", ip)
    except:
        pass