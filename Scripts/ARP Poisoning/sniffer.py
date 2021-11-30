#!/usr/bin/python
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='eth1',filter='arp',prn=print_pkt)

