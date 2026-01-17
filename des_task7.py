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
    # Standard DES P-Box table 
    p_table = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    print("\n" + "="*50)
    print("  DES ENCRYPTION PROCESSOR - TASK 07  ")
    print("="*50)
    
    try:
        # User input with requested examples and original variable names
        val_from_task6 = input(" [INPUT] S-Box Result (0x5C421307): ").strip()
        val_from_task4 = input(" [INPUT] Left Side L(i) (0x1A2B3C4D): ").strip() 

        # Clean 0x prefix if present for interoperability 
        h6 = val_from_task6[2:] if val_from_task6.lower().startswith("0x") else val_from_task6
        h4 = val_from_task4[2:] if val_from_task4.lower().startswith("0x") else val_from_task4

        # Check for 32-bit length (8 hex digits)
        if len(h6) != 8 or len(h4) != 8:
            print("\n [!] ERROR: Please enter exactly 8 hex characters.")
            return

        # Convert hex to binary strings with padding to 32 bits
        bits6 = bin(int(h6, 16))[2:].zfill(32)
        bits4 = bin(int(h4, 16))[2:].zfill(32)

        # 1. Perform Permutation (P) 
        permuted_bits = ""
        for pos in p_table:
            permuted_bits += bits6[pos - 1]

        # 2. XOR with Left Side 
        res_int = int(permuted_bits, 2) ^ int(bits4, 2)
        
        # Format the final 32-bit Right result for Task 8 [cite: 43, 45]
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