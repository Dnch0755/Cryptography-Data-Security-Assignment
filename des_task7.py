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
    # Dictionary mapping for the P-Box
    # This maps output position to source bit position from the S-Box result
    P_MAP = {
        1: 16, 2: 7, 3: 20, 4: 21, 5: 29, 6: 12, 7: 28, 8: 17,
        9: 1, 10: 15, 11: 23, 12: 26, 13: 5, 14: 18, 15: 31, 16: 10,
        17: 2, 18: 8, 19: 24, 20: 14, 21: 32, 22: 27, 23: 3, 24: 9,
        25: 19, 26: 13, 27: 30, 28: 6, 29: 22, 30: 11, 31: 4, 32: 25
    }

    print("\n" + "="*50)
    print("  DES ENCRYPTION PROCESSOR - TASK 07  ")
    print("="*50)
    
    try:
        val_from_task6 = input(" [INPUT] S-Box Result (0x5C421307): ").strip()
        val_from_task4 = input(" [INPUT] Left Side L(i) (0x1A2B3C4D): ").strip()

        # Clean 0x prefix if present for interoperability
        h6 = val_from_task6[2:] if val_from_task6.lower().startswith("0x") else val_from_task6
        h4 = val_from_task4[2:] if val_from_task4.lower().startswith("0x") else val_from_task4

        # Validate 32-bit length (8 hex digits)
        if len(h6) != 8 or len(h4) != 8:
            print("\n [!] ERROR: Please enter exactly 8 hex characters.")
            return

        # Convert hex to binary strings with 32-bit padding
        bits6 = bin(int(h6, 16))[2:].zfill(32)
        bits4 = bin(int(h4, 16))[2:].zfill(32)

        # 1. Perform Permutation (P)
        # Iterate through our map to rearrange the bits
        permuted_bits = "".join(bits6[P_MAP[i] - 1] for i in range(1, 33))

        # 2. XOR with Left Side 32 bit
        # This produces the Right 32-bit for the next round
        res_int = int(permuted_bits, 2) ^ int(bits4, 2)
        
        # Format the final result for Task 8
        # Output must be a 32-bit hex string
        final_hex = hex(res_int)[2:].zfill(8).upper()
        
        # Simple Results Display
        print("\n" + "-"*50)
        print(f" >> CALCULATION SUCCESSFUL")
        print(f" >> Round (i+1) Right Side: 0x{final_hex}")
        print("-"*50)
        print(" STATUS: Ready for Task 8 input.")

    except Exception:
        print("\n [!] ERROR: Invalid Hexadecimal format detected.")

if __name__ == "__main__":
    execute_task_7()