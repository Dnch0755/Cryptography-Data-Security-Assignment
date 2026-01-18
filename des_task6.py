# DES S-Box Tables
S_BOX = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

def get_48bit_input():
    """Get 48-bit input from user"""
    print("\n" + "="*50)
    print("DES S-BOX TRANSFORMATION (48-bit → 32-bit)")
    print("="*50)
    
    while True:
        print("\nEnter 48-bit input (choose format):")
        # print("1. Binary (48 bits like: 011000010001011110111010100001100110010100100111)")
        print("1. Hexadecimal (12 hex digits like: 6117BA866527)")
        print("2n. Use example: 0x123456789ABC")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        # if choice == "1":
    
        #     binary_input = input("\nEnter 48-bit binary string: ").strip()
            
   
        #     binary_input = binary_input.replace(" ", "")
            
        #     if len(binary_input) != 48:
        #         print(f"ERROR: Must be 48 bits. You entered {len(binary_input)} bits.")
        #         continue
            
        #     if not all(c in "01" for c in binary_input):
        #         print("ERROR: Binary string must contain only 0s and 1s.")
        #         continue
            
        #     return binary_input
            
        if choice == "1":
           
            hex_input = input("\nEnter 48-bit hex string (12 hex digits): ").strip()
            
            hex_input = hex_input.replace("0x", "").replace("0X", "").replace(" ", "")
            
       
            if len(hex_input) != 12:
                print(f"ERROR: Must be 12 hex digits. You entered {len(hex_input)} digits.")
                continue
            
            try:
             
                binary_input = bin(int(hex_input, 16))[2:].zfill(48)
                return binary_input
            except ValueError:
                print("ERROR: Invalid hexadecimal string.")
                continue
                
        elif choice == "2":
          
            print("\nUsing example input: 0x123456789ABC")
            hex_input = "123456789ABC"
            binary_input = bin(int(hex_input, 16))[2:].zfill(48)
            return binary_input
            
        else:
            print("ERROR: Invalid choice. Please enter 1, 2, or 3.")

def sbox_substitution(input_48bit):
    """Perform S-BOX substitution (48-bit to 32-bit)"""
    # Split 48-bit input into 8 groups of 6 bits
    six_bit_groups = []
    for i in range(0, 48, 6):
        six_bit_groups.append(input_48bit[i:i+6])
    

    output_32bit = ""
    
    for i, six_bits in enumerate(six_bit_groups):
        row_bits = six_bits[0] + six_bits[5]  # First and last bit
        row = int(row_bits, 2)
        
        col_bits = six_bits[1:5]  # Middle 4 bits
        col = int(col_bits, 2)
        
        sbox_value = S_BOX[i][row][col]
        
  
        output_32bit += bin(sbox_value)[2:].zfill(4)
    
    return output_32bit

def display_output(input_bin, output_bin):
    """Display the S-BOX output"""

    input_hex = hex(int(input_bin, 2))[2:].upper().zfill(12)
    output_hex = hex(int(output_bin, 2))[2:].upper().zfill(8)
    
    print("\n" + "="*50)
    print("S-BOX TRANSFORMATION RESULT")
    print("="*50)
    
    print(f"\nInput (48-bit):")
    print(f"Binary: {input_bin}")
    print(f"Hex:    0x{input_hex}")
    
    print(f"\nOutput (32-bit):")
    print(f"Binary: {output_bin}")
    print(f"Hex:    0x{output_hex}")
    

    print(f"\nTransformation: 48 bits → 32 bits")
    print(f"Each of 8 S-boxes: 6 bits → 4 bits")
    
    print("\n" + "="*50)

def main():
    """Main function"""
    print("DES S-BOX Converter")
    print("Converts 48-bit input to 32-bit output using DES S-boxes")
    

    input_binary = get_48bit_input()
    

    output_binary = sbox_substitution(input_binary)
    

    display_output(input_binary, output_binary)
    
 
    while True:
        again = input("\nRun again? (y/n): ").strip().lower()
        if again == 'y':
            input_binary = get_48bit_input()
            output_binary = sbox_substitution(input_binary)
            display_output(input_binary, output_binary)
        elif again == 'n':
            print("\nProgram ended. Goodbye!")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()