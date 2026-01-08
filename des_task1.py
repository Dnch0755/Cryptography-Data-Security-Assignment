def hex_to_bin(hex_str, bits=64):
    """
    Convert a hex string to a binary string of fixed length.
    """
    int_val = int(hex_str, 16)
    bin_str = bin(int_val)[2:].zfill(bits)
    return bin_str

def bin_to_hex(bin_str):
    """
    Convert a binary string to a hex string.
    """
    int_val = int(bin_str, 2)
    hex_str = hex(int_val)[2:].upper().zfill(16)
    return "0x" + hex_str

def validate_parity(key_bin):
    """
    Validate odd parity for each 8-bit block (DES parity bits).
    Returns True if valid, False otherwise.
    """
    for i in range(0, 64, 8):
        byte = key_bin[i:i+8]
        if byte.count('1') % 2 == 0:
            return False
    return True

def pc1_permutation(key_bin):
    """
    Perform Permuted Choice 1 (PC-1) on 64-bit binary string.
    Returns 56-bit binary string after permutation.
    """
    # PC-1 table (8x7) — ignoring parity bits
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    # Convert to 1-based index for clarity
    pc1_result = ''.join(key_bin[i-1] for i in pc1_table)
    return pc1_result

def main():
    print("=" * 60)
    print("DES Round Key Generation - Part 1")
    print("Task: Input 64-bit key → Validate parity → PC-1 → 56-bit key")
    print("=" * 60)

    # Input hex key (example: 0x1122334455667788)
    hex_key = input("Enter 64-bit key in hex (e.g., 0x1122334455667788): ").strip()

    # Remove '0x' prefix if present
    if hex_key.startswith("0x"):
        hex_key = hex_key[2:]

    # Ensure length is 16 hex digits (64 bits)
    if len(hex_key) != 16:
        print("Error: Key must be exactly 64 bits (16 hex digits).")
        return

    # Convert hex to binary (64 bits)
    key_bin = hex_to_bin(hex_key, bits=64)

    print(f"\n1. Input Key (Hex): 0x{hex_key.upper()}")
    print(f"   Binary: {key_bin}")
    print(f"   Length: {len(key_bin)} bits")

    # Validate parity bits
    if not validate_parity(key_bin):
        print("Warning: Parity bits are invalid (odd parity expected).")
        proceed = input("Continue anyway? (y/n): ").strip().lower()
        if proceed != 'y':
            print("Exiting.")
            return
    else:
        print("✓ Parity bits are valid (odd parity).")

    # Apply PC-1 permutation
    pc1_output = pc1_permutation(key_bin)

    print(f"\n2. After PC-1 Permutation:")
    print(f"   Binary: {pc1_output}")
    print(f"   Length: {len(pc1_output)} bits")

    # Convert 56-bit result to hex
    pc1_hex = bin_to_hex(pc1_output).replace("0x", "")
    # Pad to 14 hex digits for 56 bits
    pc1_hex = pc1_hex.zfill(14)
    print(f"   Hex: 0x{pc1_hex.upper()}")

    print("\n" + "=" * 60)
    print("Task 1 completed successfully.")
    print("Output (56-bit key after PC-1) is ready for next step.")
    print("=" * 60)

if __name__ == "__main__":
    main()