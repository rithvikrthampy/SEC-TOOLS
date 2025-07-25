from scapy.all import sniff, ARP

def arp_display(packet):
    if packet.haslayer(ARP):
        arp = packet[ARP]
        if arp.op == 1:
            print(f"[+] ARP Request: {arp.psrc} is asking about {arp.pdst}")
        elif arp.op == 2:
            print(f"[+] ARP Reply: {arp.psrc} has MAC address {arp.hwsrc}")

print("Sniffing ARP packets.......")
sniff(filter="arp", prn=arp_display, store=0)
