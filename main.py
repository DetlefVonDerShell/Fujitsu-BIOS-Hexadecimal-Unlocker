import crcmod

crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0xFFFFFFFF, xorOut=0x00000000)

while True:
    # Prompt User for Input
    input_string = input("Please enter the code: ")
    # Exit Function
    if input_string.lower() == 'exit':
        print("Exiting..")
        break
        #

    # Divide Input in Blocks
    blocks = input_string.split('-')

    # Check input length
    if len(blocks) == 6 and len(blocks[0]) <= 4 and len(blocks[1]) <= 4 and len(blocks[2]) <= 4 and len(
            blocks[3]) <= 4 and len(blocks[4]) <= 4 and len(blocks[5]) <= 4:
                
        # Check first two blocks
        if blocks[0] == "203c" and blocks[1] == "d001":
            
            # Connect blocks
            result_string = "".join(blocks[2:])
            
            # Replace - Symbol
            result_string = result_string.replace("-", "")
            
            # Print Statement
            print("Input ok.")
            
            # Change Input to Hex and cut off '0x' to get result-string utf-8 representation
            hex_result = hex(int(result_string, 16))[2:].encode('utf-8')

            # CRC Function on hex_result
            crc_sum = hex(crc32_func(bytearray(hex_result)))

            print("The master password is: ", crc_sum[2:])
            print("Please note that the password is encoded for US QWERTY keyboard layouts.")
            break
        else:
            print("Wrong Input! The first two blocks must be '203c' and 'd001'.")
    else:
        print("Wrong Input! 6x4 blocks required.")
