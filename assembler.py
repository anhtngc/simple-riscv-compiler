import re
from binary_genarative import RType, IType_1, IType_2, IType_3, SType, UType, BType, JType
from assembly_parsing import parse_instruction, calculate_label_offsets, remove_comments

try:
    # Get input filename
    input_filename = input("Enter the assembly file name: ")
        
    # Read input file
    with open(input_filename, 'r') as fhand:
        lines = fhand.readlines()

    # Calculate label offsets first
    labels = calculate_label_offsets(lines)

    instructions = remove_comments(lines) 
        
    results = []
    line_number = 0

    # Process each line
    for line in lines:
        line = line.strip()
        if not line or line.endswith(':') or line.startswith('#'):
            continue

        current_address = line_number * 4 

        # Parse instruction with label information
        parsed_fields = parse_instruction(line, labels, current_address)
            
        if parsed_fields is None:
            continue

        # Convert to machine code based on instruction type
        binary_code = None
            
        if parsed_fields["type"] == "R":
            converter = RType(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["rs1"], parsed_fields["rs2"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "I1":
            converter = IType_1(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["rs1"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "I2":
            converter = IType_2(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["rs1"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "I3":
            converter = IType_3(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["rs1"], parsed_fields["shamt"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "S":
            converter = SType(parsed_fields["instruction"], parsed_fields["rs1"], parsed_fields["rs2"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "U":
            converter = UType(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "SB":
            converter = BType(parsed_fields["instruction"], parsed_fields["rs1"], parsed_fields["rs2"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()
                
        elif parsed_fields["type"] == "UJ":
            converter = JType(parsed_fields["instruction"], parsed_fields["rd"], parsed_fields["imm"])
            binary_code = converter.to_machine_code()

        if binary_code:
            results.append({
                "instruction": line.strip(),
                "address": current_address,
                "binary_code": binary_code
            })
            
        line_number += 1

    # Write results to output file
    with open("binary.bin", 'w') as file:
        for result in results:
            file.write(f"{result['binary_code']}\n")

    print("Successfully converted the instructions to machine codes, click 'binary.bin' to see the results!")

except FileNotFoundError:
    print(f"Error: Input file not found")
except Exception as e:
    print(f"Error: {str(e)}")