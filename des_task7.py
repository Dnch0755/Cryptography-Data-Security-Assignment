# ==============================================================================
# (Ammar Hakimi bin Adnan)
# Cryptography & Data Security Assignment 2025/2026
# Task 7: DES Encryption - Permutation (P) and XOR with Left Side
# ==============================================================================
# INPUT:  32-bit S-Box Result (Task 6) and 32-bit Left Side (Task 4)
# PROCESS: Perform P-Box Permutation and XOR with Left Side
# OUTPUT: Round (i+1) Right 32-bit (Ready for Task 8)
# ==============================================================================
import sys

def execute_task_7():
    # Define the DES P-Box using a dictionary
    # This maps the output position (1-32) to the source bit position from the S-Box
    P_MAP = {
        1: 16, 2: 7, 3: 20, 4: 21, 5: 29, 6: 12, 7: 28, 8: 17,
        9: 1, 10: 15, 11: 23, 12: 26, 13: 5, 14: 18, 15: 31, 16: 10,
        17: 2, 18: 8, 19: 24, 20: 14, 21: 32, 22: 27, 23: 3, 24: 9,
        25: 19, 26: 13, 27: 30, 28: 6, 29: 22, 30: 11, 31: 4, 32: 25
    }

    print("--- DES Project: Task 7 Module ---")
    
    # 1. Get Input from previous tasks
    input_from_6 = input("Enter 32-bit S-Box Result (in hex (0x5C421307)): ").strip()
    input_from_4 = input("Enter 32-bit Left Side (in hex (0x1A2B3C4D)): ").strip()

    # Clean the input (remove '0x' if present)
    if input_from_6.lower().startswith("0x"):
        input_from_6 = input_from_6[2:]
    if input_from_4.lower().startswith("0x"):
        input_from_4 = input_from_4[2:]

    # 2. Validate Input Length
    # We expect 8 hex chars for 32 bits (8 * 4 = 32)
    if len(input_from_6) != 8 or len(input_from_4) != 8:
        print(f"\n[ERROR] Invalid length! Expected 8 hex characters (32 bits).")
        print(f"S-Box Input: {len(input_from_6)} chars | Left Side Input: {len(input_from_4)} chars")
        return

    try:
        # 3. Conversion to Binary Strings
        # Use zfill(32) to ensure leading zeros are preserved [cite: 41]
        sbox_bits = bin(int(input_from_6, 16))[2:].zfill(32)
        left_bits = bin(int(input_from_4, 16))[2:].zfill(32)

        print(f"\n[INFO] Input Validated.")

        # PROCESS 1: P-Box Permutation
        # Iterate through our map to rearrange the bits [cite: 43]
        permuted_string = "".join(sbox_bits[P_MAP[i] - 1] for i in range(1, 33))

        # PROCESS 2: Bitwise XOR with the Left Side
        # This produces the Right 32-bit for the next round [cite: 43]
        result_int = int(permuted_string, 2) ^ int(left_bits, 2)
        
        # OUTPUT SECTION
        # Formatted for Task 8: Inverse Initial Permutation [cite: 45]
        output_hex = hex(result_int)[2:].zfill(8).upper()
        
        print("-" * 60)
        print(f"RESULT: Round (i+1) Right 32-bit")
        print(f"Hex Output: 0x{output_hex}")
        print("-" * 60)
        print("\n[NEXT STEP]")
        print(f"Pass this value (0x{output_hex}) to the member doing Task 8.")

    except ValueError:
        print("\n[ERROR] Input contains non-hexadecimal characters.")

if __name__ == "__main__":
    execute_task_7()