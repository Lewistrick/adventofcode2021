def get_versions(packet, n_subs=1):
    print("------------------ Reading packet:", packet)
    # if n_subs == 0:
    #     print("No subs expected!")
    #     return []

    if not packet or all(ch == "0" for ch in packet):
        print("No packet left! Error?")
        return []

    ver = int(packet[:3], 2)
    typ = int(packet[3:6], 2)
    print(f"Version={ver}, Type={typ}")
    versions = [ver]
    if typ == 4:
        # read literal value
        tot = 0
        bytesread = 6 # version and type number also count
        print("- Reading literal:", packet[6:])
        for group in (packet[i:i+5] for i in range(6, len(packet), 5)):
            print(f"  - Group: '{group}'")
            tot = 16 * tot + int(group[1:], 2)
            bytesread += 5
            if group.startswith("0"):
                break
        print(f"  - Total: {tot}")
        restpacket = packet[bytesread:]
        versions += get_versions(restpacket, n_subs-1)
        return versions

    # if the next number is a 0, read 15 bytes, else read 11 bytes
    read_n = 15 if packet[6] == "0" else 11
    next_idx = 7 + read_n
    n_subs = int(packet[7:next_idx], 2)
    print(f"Number of subpackets: {n_subs}")
    subpacket = packet[next_idx:]
    versions += get_versions(subpacket, n_subs)
    return versions


# read input
with open("in16.txt") as line:
    inp = line.read()

packet = bin(int(inp, 16))[2:]
nmissing = (4 - len(packet) % 4) % 4
packet = "0" * nmissing + packet

versions = get_versions(packet)
print("Versions:", versions)
print("part 1:", sum(versions))