def hex_to_bin(hex_str, bits=64):
    """
    Convert a hex string to a binary string of fixed length.
    """
    int_val = int(hex_str, 16)
    bin_str = bin(int_val)[2:].zfill(bits)
    return bin_str


def bin_to_hex(bin_str):
    """
    Convert a binary string to a hex string with correct length.
    (56 bits → 14 hex characters)
    """
    int_val = int(bin_str, 2)
    hex_len = len(bin_str) // 4
    hex_str = hex(int_val)[2:].upper().zfill(hex_len)
    return "0x" + hex_str


def validate_parity(key_bin):
    """
    Validate odd parity for each 8-bit block (DES parity bits).
    Returns True if valid, False otherwise.
    """
    for i in range(0, 64, 8):
        byte = key_bin[i:i + 8]
        if byte.count('1') % 2 == 0:
            return False
    return True


def pc1_permutation(key_bin):
    """
    Perform Permuted Choice 1 (PC-1).
    """
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
    return ''.join(key_bin[i - 1] for i in pc1_table)


def main():
    output_lines = []

    output_lines.append("=" * 60)
    output_lines.append("DES Round Key Generation - Part 1")
    output_lines.append("Task: Input 64-bit key → Validate parity → PC-1 → 56-bit key")
    output_lines.append("=" * 60)

    hex_key = input(
        "Enter 64-bit key in hex (e.g., 0x133457799BBCDFF1): "
    ).strip()

    if hex_key.startswith("0x"):
        hex_key = hex_key[2:]

    if len(hex_key) != 16:
        print("❌ Error: Key must be exactly 64 bits (16 hex digits).")
        return

    key_bin = hex_to_bin(hex_key)

    output_lines.append(f"\n1. Input Key (Hex): 0x{hex_key.upper()}")
    output_lines.append(f"   Binary: {key_bin}")
    output_lines.append(f"   Length: {len(key_bin)} bits")

    # STRICT PARITY CHECK (STOP IF INVALID)
    if not validate_parity(key_bin):
        output_lines.append("✗ Parity bits are INVALID (odd parity required).")
        output_lines.append("\n❌ Program terminated due to invalid parity.")
        print("\n".join(output_lines))

        # Save output before exiting
        with open("Des_Task1_Output.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))

        print("\n✔ Output saved to 'Des_Task1_Output.txt'")
        return
    else:
        output_lines.append("✓ Parity bits are valid (odd parity).")

    # PC-1 Permutation
    pc1_output = pc1_permutation(key_bin)
    pc1_hex = bin_to_hex(pc1_output)

    output_lines.append("\n2. After PC-1 Permutation:")
    output_lines.append(f"   Binary: {pc1_output}")
    output_lines.append(f"   Length: {len(pc1_output)} bits")
    output_lines.append(f"   Hex: {pc1_hex}")

    output_lines.append("\n" + "=" * 60)
    output_lines.append("Task 1 completed successfully.")
    output_lines.append("Output (56-bit key after PC-1) is ready for next step.")
    output_lines.append("=" * 60)

    # Print to terminal
    print("\n".join(output_lines))

    # Write to text file
    with open("Des_Task1_Output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("\n✔ Output also saved to 'Des_Task1_Output.txt'")


if __name__ == "__main__":
    main()
