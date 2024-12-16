import re
from binary_genarative import conventions

# Remove comments from each line
def remove_comments(lines):
        instructions = []
        for line in lines:
            line = re.sub(r'#.*', '', line)
            line = line.strip()
            if line:
                instructions.append(line)
        return instructions


def calculate_label_offsets(lines):
    labels = {}
    line_number = 0
    for line in lines:
        line = line.strip()
        # Ignore blank lines and comments
        if not line or line.startswith('#'):
            continue
            
        if ':' in line:
            label_part, *instruction_part = line.split(':')
            label = label_part.strip()
            labels[label] = line_number * 4  # address = number of lines * 4
            
            # If there is an adjacent command after the label, treat this as a line command
            if instruction_part:
                line_number += 1
        else:
            line_number += 1
    return labels

def parse_instruction(instruction_line, labels=None, current_address=None):
    # Remove comments and clean up the line
    if '#' in instruction_line:
        instruction_line = instruction_line.split('#')[0]
    instruction_line = instruction_line.strip()
    
    if not instruction_line or instruction_line.endswith(':'):
        return None
    
    if instruction_line.startswith('.data'):
        return None
        
    if ':' in instruction_line:
        parts = instruction_line.split(':', 1)
        label = parts[0].strip()
        instruction_line = parts[1].strip()
        
    parts = re.split(r'[,\s()]+', instruction_line)
    parts = [p for p in parts if p]  # Remove empty strings
    if not parts:
        return None

    instruction = parts[0].upper()

    # Check and ignore commands that do not need conversion
    if instruction.lower() in ["nop"]:
        return None
    
    # Convert register name to numeric format
    if len(parts) > 1 and parts[1] in conventions:
        parts[1] = f"x{conventions[parts[1]]}"
    if len(parts) > 2 and parts[2] in conventions:
        parts[2] = f"x{conventions[parts[2]]}"
    if len(parts) > 3 and parts[3] in conventions:
        parts[3] = f"x{conventions[parts[3]]}"

    r_type_instructions = {"ADD", "SUB", "AND", "OR", "XOR", "SLL", "SRL", "SRA", "SLT", "SLTU"}
    i_type1_instructions = {"ADDI", "ORI", "XORI", "ANDI", "SLTI", "SLTIU"}
    i_type2_instructions = {"LB", "LH", "LW", "LBU", "LHU"}
    i_type3_instructions = {"SLLI", "SRLI", "SRAI"}
    s_type_instructions = {"SB", "SH", "SW"}
    sb_type_instructions = {"BEQ", "BNE", "BLT", "BGE", "BLTU", "BGEU"}
    u_type_instructions = {"LUI", "AUIPC"}
    uj_type_instructions = {"JAL"}

    try:
        if instruction in r_type_instructions:
            return {"type": "R", "instruction": instruction, "rd": parts[1], "rs1": parts[2], "rs2": parts[3]}

        elif instruction in i_type3_instructions:
            return {"type": "I3", "instruction": instruction, "rd": parts[1], "rs1": parts[2], "shamt": parts[3]}

        elif instruction in i_type1_instructions:
            return {"type": "I1", "instruction": instruction, "rd": parts[1], "rs1": parts[2], "imm": parts[3]}
        
        elif instruction in i_type2_instructions:
            return {"type": "I2", "instruction": instruction, "rd": parts[1], "rs1": parts[3], "imm": parts[2]}

        elif instruction in s_type_instructions:
            return {"type": "S", "instruction": instruction, "imm": parts[2], "rs1": parts[3], "rs2": parts[1]}
        
        elif instruction in sb_type_instructions and labels and current_address is not None:
            target_label = parts[3]
            if target_label in labels:
                imm_offset = (labels[target_label] - current_address) 
                return {"type": "SB", "instruction": instruction, "rs1": parts[1], "rs2": parts[2], "imm": imm_offset}

        elif instruction in u_type_instructions:
            return {"type": "U", "instruction": instruction, "rd": parts[1], "imm": parts[2]}
        
        elif instruction in uj_type_instructions and labels and current_address is not None:
            target_label = parts[2]
            if target_label in labels:
                # Calculate offset as the difference between the label address and the current address, then shift by 1 for JAL
                imm_offset = (labels[target_label] - current_address)
                return {"type": "UJ", "instruction": instruction, "rd": parts[1], "imm": imm_offset}

    except IndexError:
        print(f"Warning: Invalid instruction format: {instruction_line}")
        return None

    return None