# Task 7: DES Permutation (P) and XOR with Left Side
import sys

def execute_task_7():
    # We define the DES P-Box using a dictionary
    # This maps the output position (1-32) to the source bit position from the S-Box
    P_MAP = {
        1: 16, 2: 7, 3: 20, 4: 21, 5: 29, 6: 12, 7: 28, 8: 17,
        9: 1, 10: 15, 11: 23, 12: 26, 13: 5, 14: 18, 15: 31, 16: 10,
        17: 2, 18: 8, 19: 24, 20: 14, 21: 32, 22: 27, 23: 3, 24: 9,
        25: 19, 26: 13, 27: 30, 28: 6, 29: 22, 30: 11, 31: 4, 32: 25
    }

    print("--- DES Project: Task 7 Module ---")
    
    try:
        # INPUT SECTION
        # 32-bit input from S-Box (Task 6) and 32-bit Left Side (Task 4)
        input_from_6 = input("Enter 32-bit S-Box Result (in hex (0x5C421307)): ").strip()
        input_from_4 = input("Enter 32-bit Left Side (in hex (0x1A2B3C4D)): ").strip()

        # Conversion to Binary Strings
        sbox_bits = bin(int(input_from_6, 16))[2:].zfill(32)
        left_bits = bin(int(input_from_4, 16))[2:].zfill(32)

        # PROCESS 1: P-Box Permutation
        # Iterate through our map to rearrange the bits
        permuted_string = "".join(sbox_bits[P_MAP[i] - 1] for i in range(1, 33))

        # PROCESS 2: Bitwise XOR with the Left Side
        # This produces the Right 32-bit for the next round
        result_int = int(permuted_string, 2) ^ int(left_bits, 2)
        
        # OUTPUT SECTION
        # Formatted for Task 8: Inverse Initial Permutation
        output_hex = hex(result_int)[2:].zfill(8).upper()
        
        print("\n" + "="*40)
        print(f"Round (i+1) Right 32-bit: 0x{output_hex}")
        print("="*40)
        print("Ready for Task 8 input.")

    except (ValueError, IndexError) as e:
        print(f"Format Error: Please ensure you enter valid 32-bit hex values. {e}")

if __name__ == "__main__":
    execute_task_7()