# ==============================================================================
# (Dennis)
# Cryptography & Data Security Assignment 2025/2026
# Task 3: DES Round Key Generation (Permuted Choice 2)
# ==============================================================================
# INPUT:  56-bit Key (Hex String) from Task 2 (Shifted Key)
# OUTPUT: 48-bit Round Key (Hex String) for Task 5 (Encryption)
# ==============================================================================

def hex_to_bin(hex_str, bits):
    """
    Convert a hex string to a binary string of a specific bit length.
    Includes error handling for empty inputs.
    """
    if not hex_str:
        return ""
    int_val = int(hex_str, 16)
    bin_str = bin(int_val)[2:].zfill(bits)
    return bin_str

def bin_to_hex(bin_str):
    """
    Convert a binary string back to a hex string.
    Ensures the output is uppercase and formatted with '0x'.
    """
    int_val = int(bin_str, 2)
    # Calculate how many hex digits we need (4 bits per hex digit)
    hex_len = len(bin_str) // 4
    hex_str = hex(int_val)[2:].upper().zfill(hex_len)
    return "0x" + hex_str

def pc2_permutation(key_56_bin):
    """
    Applies the PC-2 Permutation Table to compress 56 bits into 48 bits.
    """
    # Standard DES PC-2 Table (Compresses 56 bits -> 48 bits)
    # Indices are 1-based standard, so we subtract 1 during access.
    PC2_TABLE = [
        14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
        23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
    ]

    # Map the bits using the table
    # Note: key_56_bin is 0-indexed, so we use i-1
    key_48_bin = ''.join(key_56_bin[i-1] for i in PC2_TABLE)
    return key_48_bin

def main():
    print("=" * 60)
    print("DES Round Key Generation - Task 3 (PC-2)")
    print("Objective: Compress 56-bit Shifted Key -> 48-bit Round Key")
    print("=" * 60)

    # 1. Get Input from previous task (Output data from Task 2)
    # Note: A 56-bit key is represented by 14 Hex digits (14 * 4 = 56)
    hex_input = input("Enter 56-bit Key from Task 2 (e.g., 0x1B02EFFC7072): ").strip()

    # Clean the input (remove '0x' if present)
    if hex_input.lower().startswith("0x"):
        hex_input = hex_input[2:]

    # 2. Validate Input Length
    # We expect 14 hex chars for 56 bits.
    if len(hex_input) != 14:
        print(f"\n[ERROR] Invalid length! Expected 14 hex characters (56 bits).")
        print(f"You entered {len(hex_input)} characters.")
        print("Please check the output from Task 2 again.")
        return

    try:
        # 3. Convert to Binary (56 bits)
        key_56_bin = hex_to_bin(hex_input, 56)
        
        print(f"\n[INFO] Input Validated.")
        print(f"Binary (56-bit): {key_56_bin}")

        # 4. Perform PC-2 Permutation
        key_48_bin = pc2_permutation(key_56_bin)

        # 5. Convert to Hex Output (48 bits = 12 Hex digits)
        key_48_hex = bin_to_hex(key_48_bin)

        print("-" * 60)
        print(f"RESULT: 48-bit Round Key")
        print(f"Binary: {key_48_bin}")
        print(f"HEX   : {key_48_hex}")
        print("-" * 60)
        
        print("\n[NEXT STEP]")
        print(f"Pass this value ({key_48_hex}) to the member doing Task 5 (Expansion & XOR).")

    except ValueError:
        print("\n[ERROR] Input contains non-hexadecimal characters.")

if __name__ == "__main__":
    main()