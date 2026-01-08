import socket
import time

UDP_IP = "192.168.1.241"
UDP_PORT = 13900
data_length = 1350

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 262144)  # CRITICAL!
sock.bind((UDP_IP, UDP_PORT))

print("Listening for EEG data...")
print(f"Packet size: {data_length} bytes")
print(f"Samples per packet: {data_length // 27}")
print(f"Expected: 5 packets/sec, 250 samples/sec")
print("-" * 50)

packet_count = 0
sample_count = 0
start_time = time.time()
last_report_time = start_time

try:
    while True:
        data, addr = sock.recvfrom(2048)
        
        packet_count += 1
        samples_in_packet = len(data) // 27
        sample_count += samples_in_packet
        
        current_time = time.time()
        elapsed = current_time - last_report_time
        
        # Report every second
        if elapsed >= 1.0:
            packets_per_sec = packet_count / elapsed
            samples_per_sec = sample_count / elapsed
            total_elapsed = current_time - start_time
            
            print(f"Time: {total_elapsed:.1f}s | "
                  f"Packets/sec: {packets_per_sec:.1f} | "
                  f"Samples/sec: {samples_per_sec:.1f} | "
                  f"Packet size: {len(data)} bytes")
            
            packet_count = 0
            sample_count = 0
            last_report_time = current_time
            
except KeyboardInterrupt:
    print("\nStopped")
