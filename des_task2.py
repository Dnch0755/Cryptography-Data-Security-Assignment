def hex_to_bin(hex_str, bits=56):
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
    hex_str = hex(int_val)[2:].upper().zfill(14)
    return "0x" + hex_str


def left_circular_shift(key_half, shifts):
    """
    Perform left circular shift on 28-bit key half.
    """
    return key_half[shifts:] + key_half[:shifts]


def generate_round_keys(key_56bit):
    """
    Generate 16 round keys by performing left circular shifts.
    """
    # DES shift schedule: number of left shifts per round
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # Split into left 28 bits (C0) and right 28 bits (D0)
    left_half = key_56bit[:28]
    right_half = key_56bit[28:]
    
    round_keys = []
    
    # Generate keys for all 16 rounds
    for round_num in range(1, 17):
        # Perform left circular shift based on schedule
        shifts = shift_schedule[round_num - 1]
        left_half = left_circular_shift(left_half, shifts)
        right_half = left_circular_shift(right_half, shifts)
        
        # Combine left and right halves (Cn + Dn)
        combined_key = left_half + right_half
        round_keys.append((round_num, combined_key))
    
    return round_keys


def main():
    print("=" * 70)
    print("DES Round Key Generation - Task 2")
    print("Task: Split 56-bit key → Left Circular Shifts → 16 Round Keys")
    print("=" * 70)
    
    # Input: 56-bit key from Task 1 (after PC-1)
    hex_key = input("Enter 56-bit key after PC-1 (e.g., 0x11223344556677): ").strip()
    
    # Remove '0x' prefix if present
    if hex_key.startswith("0x") or hex_key.startswith("0X"):
        hex_key = hex_key[2:]
    
    # Pad to 14 hex digits if needed (for 56 bits)
    hex_key = hex_key.zfill(14)
    
    # Validate input length
    if len(hex_key) > 14:
        print("Error: Key must be at most 56 bits (14 hex digits).")
        return
    
    # Convert hex to binary (56 bits)
    key_bin = hex_to_bin(hex_key, bits=56)
    print(f"\n1. Input Key (Hex): 0x{hex_key.upper()}")
    print(f"   Binary: {key_bin}")
    print(f"   Length: {len(key_bin)} bits")
    
    # Split into left and right halves
    left_half = key_bin[:28]
    right_half = key_bin[28:]
    
    print(f"\n2. Initial Key Split (28-bit halves):")
    print(f"   Left  (C0): {left_half}")
    print(f"   Right (D0): {right_half}")
    
    # Generate all 16 round keys
    round_keys = generate_round_keys(key_bin)
    
    print(f"\n3. Round Keys (after Left Circular Shifts):")
    print("   " + "=" * 80)
    print("   Round | 56-bit Binary Key                                        | Hex")
    print("   " + "-" * 80)
    
    for round_num, key_binary in round_keys:
        key_hex = bin_to_hex(key_binary)
        print(f"   R{round_num:02d}   | {key_binary} | {key_hex}")
    
    print("   " + "=" * 80)
    
    # Display shift schedule for reference
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    print(f"\n4. DES Shift Schedule:")
    print(f"   Rounds 1-16: {shift_schedule}")
    print(f"   Total shifts: {sum(shift_schedule)} (28 shifts = full rotation)")
    
    # Verification
    print(f"\n5. Verification:")
    print(f"   ✓ R16 should equal input key: {round_keys[-1][1] == key_bin}")
    
    print("\n" + "=" * 70)
    print("Task 2 completed successfully.")
    print("Output: 16 round keys (56-bit each) → Input to Task 3 (PC-2)")
    print("=" * 70)


if __name__ == "__main__":
    main()
