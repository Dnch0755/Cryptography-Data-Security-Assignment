def hex_to_bin(hex_str, bits=56):
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


def left_circular_shift(key_half, shifts):
    """
    Perform left circular shift on 28-bit key half.
    """
    return key_half[shifts:] + key_half[:shifts]


def generate_round_keys(key_56bit):
    """
    Generate 16 round keys using left circular shifts.
    Returns list of (round_number, 56-bit_key) tuples.
    """
    # DES shift schedule
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # Split into C0 (left 28 bits) and D0 (right 28 bits)
    left_half = key_56bit[:28]
    right_half = key_56bit[28:]
    
    round_keys = []
    
    for round_num in range(1, 17):
        shifts = shift_schedule[round_num - 1]
        left_half = left_circular_shift(left_half, shifts)
        right_half = left_circular_shift(right_half, shifts)
        
        combined_key = left_half + right_half
        round_keys.append((round_num, combined_key))
    
    return round_keys


def main():
    output_lines = []
    output_lines.append("=" * 60)
    output_lines.append("DES Round Key Generation - Part 2")
    output_lines.append("Task: Input 56-bit key → Split C0/D0 → Shifts → 16 Round Keys")
    output_lines.append("=" * 60)
    
    hex_key = input(
        "Enter 56-bit key in hex (e.g., 0x1A54F265EDDE85): "
    ).strip()
    
    if hex_key.startswith("0x"):
        hex_key = hex_key[2:]
    
    if len(hex_key) != 14:
        print("❌ Error: Key must be exactly 56 bits (14 hex digits).")
        return
    
    key_bin = hex_to_bin(hex_key)
    
    output_lines.append(f"\n1. Input Key (Hex): 0x{hex_key.upper()}")
    output_lines.append(f"   Binary: {key_bin}")
    output_lines.append(f"   Length: {len(key_bin)} bits")
    
    # Split into C0 and D0
    left_half = key_bin[:28]
    right_half = key_bin[28:]
    
    output_lines.append("\n2. Initial Key Split (28-bit halves):")
    output_lines.append(f"   Left  (C0): {left_half}")
    output_lines.append(f"   Right (D0): {right_half}")
    
    # Generate round keys
    round_keys = generate_round_keys(key_bin)
    
    # Display shift schedule
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    output_lines.append("\n3. DES Shift Schedule:")
    output_lines.append(f"   Rounds 1-16: {shift_schedule}")
    output_lines.append(f"   Total shifts: {sum(shift_schedule)} (28 = full rotation)")
    
    # Display round keys
    output_lines.append("\n4. Round Keys (R1 to R16):")
    output_lines.append("   " + "=" * 56)
    output_lines.append("   Round | Hex                | Binary (56-bit)")
    output_lines.append("   " + "-" * 56)
    
    for round_num, key_binary in round_keys:
        key_hex = bin_to_hex(key_binary)
        output_lines.append(f"   R{round_num:02d}   | {key_hex:<18} | {key_binary}")
    
    output_lines.append("   " + "=" * 56)
    
    # Verification
    output_lines.append("\n5. Verification:")
    output_lines.append(f"   ✓ Total rounds generated: {len(round_keys)}")
    output_lines.append(f"   ✓ R16 returns to original: {round_keys[-1][1] == key_bin}")
    
    output_lines.append("\n" + "=" * 60)
    output_lines.append("Task 2 completed successfully.")
    output_lines.append("Output (16 round keys) is ready for next step.")
    output_lines.append("=" * 60)
    
    # Print to terminal
    print("\n".join(output_lines))
    
    # Write to text file
    with open("Des_Task2_Output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    
    print("\n✔ Output also saved to 'Des_Task2_Output.txt'")


if __name__ == "__main__":
    main()
