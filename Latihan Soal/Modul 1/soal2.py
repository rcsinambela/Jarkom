from scapy.all import rdpcap

# Load the pcap file
pcap_file = "./soal2.pcapng"

# Read the pcapng file
packets = rdpcap(pcap_file)

# Extract the protocols from each packet
protocols = [packet.__class__.__name__ for packet in packets]

# Get unique protocols and count them
unique_protocols = set(protocols)
print(unique_protocols)
print(f"Total unique protocols: {len(unique_protocols)}")
