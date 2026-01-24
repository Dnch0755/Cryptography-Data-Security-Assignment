# ==============================================================================
# Student Name : (Dennis)
# Cryptography & Data Security Assignment 2025/2026
# Task 3: DES Round Key Generation (Permuted Choice 2)
# ==============================================================================
# INPUT:  56-bit Key (Hex String) from Task 2 (Shifted Key)
# OUTPUT: 48-bit Round Key (Hex String) for Task 5 (Encryption)
# ==============================================================================

import os

def hex_to_bin(hex_str, bits=56):
    """Converts hex string to a binary string of a fixed length."""
    if not hex_str: return ""
    int_val = int(hex_str, 16)
    return bin(int_val)[2:].zfill(bits)

def bin_to_hex(bin_str):
    """Converts a binary string back to a hex string (formatted for rubric)."""
    int_val = int(bin_str, 2)
    hex_len = len(bin_str) // 4
    hex_str = hex(int_val)[2:].upper().zfill(hex_len)
    return "0x" + hex_str

def pc2_permutation(key_56_bin):
    """Applies the PC-2 Permutation Table (56-bit -> 48-bit)."""
    # Standard DES PC-2 Table
    PC2_TABLE = [
        14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
        23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
    ]
    # -1 because table starts with 1-based index, while python strings starts with 0-based
    return ''.join(key_56_bin[i-1] for i in PC2_TABLE)

def main():
    print("=" * 70)
    print("      DES ROUND KEY GENERATION - TASK 3 (PC-2)")
    print("=" * 70)

    # ---------------------------------------------------------
    # REQUIREMENT: Input from Keyboard OR File
    # ---------------------------------------------------------
    print("INPUT SOURCE SELECTION:")
    print("[1] Keyboard Input (Type manually)")
    print("[2] Read from File ('input_task3.txt')")
    choice = input("\nSelect an option (1 or 2): ").strip()

    hex_input = ""

    if choice == '2':
        filename = "input_task3.txt"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                hex_input = f.read().strip()
                print(f"\n[INFO] Read from file: {hex_input}")
        else:
            print(f"\n[ERROR] '{filename}' not found. Please create it first.")
            return
    else:
        # Default to keyboard
        hex_input = input("\nEnter 56-bit Key from Task 2 (e.g., 0x1B02EFFC707278): ").strip()

    # ---------------------------------------------------------
    # VALIDATION & CLEANING
    # ---------------------------------------------------------
    if hex_input.lower().startswith("0x"):
        hex_input = hex_input[2:]
    
    # Interoperability Fix: Handle 16-char padded input from Task 1/2
    if len(hex_input) == 16:
        hex_input = hex_input[-14:] 
    elif len(hex_input) != 14:
        print(f"\n[ERROR] Invalid length! Expected 14 hex chars (56 bits).")
        print(f"Received: {len(hex_input)} chars.")
        return

    try:
        # ---------------------------------------------------------
        # CORE PROCESSING
        # ---------------------------------------------------------
        # 1. Convert Hex -> Bin
        key_56_bin = hex_to_bin(hex_input, 56)
        
        # 2. Apply PC-2 Permutation
        key_48_bin = pc2_permutation(key_56_bin)
        
        # 3. Convert Bin -> Hex
        key_48_hex = bin_to_hex(key_48_bin)

        # ---------------------------------------------------------
        # REQUIREMENT: Output to Monitor
        # ---------------------------------------------------------
        print("\n" + "-" * 60)
        print(f"FINAL REPORT RESULTS")
        print("-" * 60)
        print(f"Input Key (56-bit)  : 0x{hex_input.upper()}")
        print(f"Round Key (48-bit)  : {key_48_hex}")
        print("-" * 60)

        # ---------------------------------------------------------
        # REQUIREMENT: Output to File
        # ---------------------------------------------------------
        output_filename = "output_task3.txt"
        with open(output_filename, "w") as f:
            f.write(key_48_hex)
        
        print(f"\n[SUCCESS] Result also saved to '{output_filename}'")
        print("[NEXT STEP] Pass this output to Member 5 (Encryption Task)")

    except ValueError:
        print("\n[ERROR] Input contains non-hexadecimal characters.")

if __name__ == "__main__":
    main()