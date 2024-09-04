# ARP Spoofing Tool

This Python script performs ARP spoofing attacks, which involve sending false ARP messages over a network. The script can be used for network testing, security research, and educational purposes.

## Features

- Perform ARP spoofing to redirect traffic between devices.
- Restore ARP tables to their original state.
- Display the number of spoofed packets sent in real-time.

## Prerequisites

- Python 3.x
- `scapy` library
- Root or administrative privileges

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NULLxDEF/arp_spoof.git
    cd arp-spoof
    ```

2. **Create and activate the virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required dependencies:**

    ```bash
    pip install scapy
    ```

## Usage

To perform ARP spoofing, run the script with root privileges:

1. Ensure you are in the virtual environment:

    ```bash
    source venv/bin/activate
    ```

2. **Enable port forwarding:**  
   Before running the script, ensure that port forwarding is enabled on your system to allow traffic to be forwarded through your machine:

    ```bash
    echo 1 > /proc/sys/net/ipv4/ip_forward
    ```

3. **Run the script with sudo:**

    ```bash
    sudo python3 arp_spoof.py
    ```

4. Follow the prompts to enter the IP addresses of the target and gateway.

## Example

```bash
sudo python3 arp_spoof.py
```
