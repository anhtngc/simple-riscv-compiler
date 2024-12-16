# Convert register operation to binary
conventions = {
    "zero": 0,
    "ra": 1,
    "sp": 2,
    "gp": 3,
    "tp": 4,
    "t0": 5,
    "t1": 6,
    "t2": 7,
    "s0": 8,
    "fp": 8,
    "s1": 9,
    "a0": 10,
    "a1": 11,
    "a2": 12,
    "a3": 13,
    "a4": 14,
    "a5": 15,
    "a6": 16,
    "a7": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "s8": 24,
    "s9": 25,
    "s10": 26,
    "s11": 27,
    "t3": 28,
    "t4": 29,
    "t5": 30,
    "t6": 31
}

# Define opcodes and funct3, funct7 values ​​for R-type instructions
class RType:
    opcode = '0110011'  # General opcode for R-type instructions

    funct3 = {
        'ADD': '000', 
        'SUB': '000', 
        'SLL': '001', 
        'SLT': '010', 
        'SLTU': '011',
        'XOR': '100', 
        'SRL': '101', 
        'SRA': '101', 
        'OR': '110', 
        'AND': '111'
    }

    funct7 = {
        'ADD': '0000000', 
        'SUB': '0100000', 
        'SLL': '0000000', 
        'SLT': '0000000',
        'SLTU': '0000000', 
        'XOR': '0000000', 
        'SRL': '0000000', 
        'SRA': '0100000',
        'OR': '0000000', 
        'AND': '0000000'
    }

    def __init__(self, instruction, rd, rs1, rs2):
        self.instruction = instruction
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2

    # Convert registers x1 to x32 to 5-bit binary code
    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    # Convert R-type instructions to 32-bit binary machine code
    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        rs1_bin = self.reg_to_bin(self.rs1)
        rs2_bin = self.reg_to_bin(self.rs2)
        funct3_bin = self.funct3[self.instruction]
        funct7_bin = self.funct7[self.instruction]
        
        # Build machine code from fields
        machine_code = (
            funct7_bin +
            rs2_bin +
            rs1_bin +
            funct3_bin +
            rd_bin +
            self.opcode
        )
        return machine_code
'''
    # Convert binary machine code to hexadecimal with format 0x (optional)
    def to_hex(self):
        binary_code = self.to_machine_code()
        hex_code = "0x" + hex(int(binary_code, 2))[2:].zfill(8).upper()
        return hex_code
'''

class IType_1: 
    opcode = '0010011'  # General opcode for ADDI, XORI, ORI, ANDI, SLTI, SLTIU instructions

    funct3 = {
        'ADDI': '000',
        'XORI': '100',
        'ORI': '110',
        'ANDI': '111',
        'SLTI': '010',
        'SLTIU': '011'
    }

    def __init__(self, instruction, rd, rs1, imm):
        self.instruction = instruction
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def imm_to_bin(self, imm):
        # Convert immediate to 12-bit signed binary in two's complement
        imm_int = int(imm)
        if imm_int < 0:
            imm_bin = format((1 << 12) + imm_int, '012b')  # Two's complement for negative numbers
        else:
            imm_bin = format(imm_int, '012b')
        return imm_bin

    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        rs1_bin = self.reg_to_bin(self.rs1)
        imm_bin = self.imm_to_bin(self.imm)
        funct3_bin = self.funct3[self.instruction]

        machine_code = (
            imm_bin +
            rs1_bin +
            funct3_bin +
            rd_bin +
            self.opcode
        )

        return machine_code

class IType_2:
    opcode = '0000011'  # General opcode for LB, LH, LW, LBU, LHU instructions

    funct3 = {
        'LB': '000',
        'LH': '001', 
        'LW': '010',
        'LBU': '100',
        'LHU': '101',
    }

    def __init__(self, instruction, rd, rs1, imm):
        self.instruction = instruction
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def imm_to_bin(self, imm):
        # Convert immediate to 12-bit signed binary in two's complement
        imm_int = int(imm)
        if imm_int < 0:
            imm_bin = format((1 << 12) + imm_int, '012b')  # Two's complement for negative numbers
        else:
            imm_bin = format(imm_int, '012b')
        return imm_bin

    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        rs1_bin = self.reg_to_bin(self.rs1)
        imm_bin = self.imm_to_bin(self.imm)
        funct3_bin = self.funct3[self.instruction]

        machine_code = (
            imm_bin +
            rs1_bin +
            funct3_bin +
            rd_bin +
            self.opcode
        )

        return machine_code

class IType_3:
    opcode = '0010011'  # General opcode for SLLI, SRLI, SRAI instructions

    funct3 = {
        'SLLI': '001',
        'SRLI': '101',
        'SRAI': '101'
    }

    funct7 = {
        'SLLI': '0000000',
        'SRLI': '0000000',
        'SRAI': '0100000'
    }

    def __init__(self, instruction, rd, rs1, shamt):
        self.instruction = instruction
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt

    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def shamt_to_bin(self, shamt):
        return format(int(shamt), '05b')

    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        rs1_bin = self.reg_to_bin(self.rs1)
        funct3_bin = self.funct3[self.instruction]
        shamt_bin = self.shamt_to_bin(self.shamt)
        funct7_bin = self.funct7[self.instruction]
        
        machine_code = (
            funct7_bin +
            shamt_bin +
            rs1_bin +
            funct3_bin +
            rd_bin +
            self.opcode
        )

        return machine_code

class SType:
    opcode = '0100011'  # General opcode for S-Type instructions

    funct3 = {
        'SB': '000', 
        'SH': '001', 
        'SW': '010'
    }

    def __init__(self, instruction, rs1, rs2, imm):
        self.instruction = instruction.upper()
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm

    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def imm_to_bin(self, imm):
        # Convert immediate to 12-bit signed binary in two's complement
        imm_int = int(imm)
        if imm_int < 0:
            imm_bin = format((1 << 12) + imm_int, '012b')  # Two's complement for negative numbers
        else:
            imm_bin = format(imm_int, '012b')

        # Split into imm[11:5] and imm[4:0] for S-type format
        return imm_bin[:7], imm_bin[7:]

    def to_machine_code(self):
        rs1_bin = self.reg_to_bin(self.rs1)
        rs2_bin = self.reg_to_bin(self.rs2)
        imm_bin_hi, imm_bin_lo = self.imm_to_bin(self.imm)
        funct3_bin = self.funct3[self.instruction]

        machine_code = (
            imm_bin_hi +
            rs2_bin +
            rs1_bin +
            funct3_bin +
            imm_bin_lo +
            self.opcode
        )
        return machine_code
    

class BType:
    opcode = '1100011'  # General opcode for B-type instructions

    funct3 = {
        'BEQ': '000',
        'BNE': '001',
        'BLT': '100',
        'BGE': '101',
        'BLTU': '110',
        'BGEU': '111'
    }

    def __init__(self, instruction, rs1, rs2, imm_offset):
        self.instruction = instruction.upper()
        self.rs1 = rs1
        self.rs2 = rs2
        # Convert negative numbers to 13-bit two's complement
        if imm_offset < 0:
            imm_offset = (1 << 13) + imm_offset
        self.imm_offset = imm_offset & 0x1FFF  # Ensure 13-bit value

    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def imm_to_bin(self, imm):
        # Separate imm bits according to B-type convention
        imm12 = (imm >> 12) & 0x1
        imm10_5 = (imm >> 5) & 0x3F
        imm4_1 = (imm >> 1) & 0xF
        imm11 = (imm >> 11) & 0x1
        
        return (format(imm12, '01b'),       # bit [12]
                format(imm10_5, '06b'),     # bits [10:5]
                format(imm4_1, '04b'),      # bits [4:1]
                format(imm11, '01b'))       # bit [11]

    def to_machine_code(self):
        rs1_bin = self.reg_to_bin(self.rs1)
        rs2_bin = self.reg_to_bin(self.rs2)
        imm12, imm10_5, imm4_1, imm11 = self.imm_to_bin(self.imm_offset)

        # Combine fields to create full binary code
        machine_code = (
            imm12 +                          
            imm10_5 +        
            rs2_bin +        
            rs1_bin +        
            self.funct3[self.instruction] +  
            imm4_1 +         
            imm11 +          
            self.opcode      
        )
        
        return machine_code
    
class UType:
    opcode = {
        'LUI': '0110111', 
        'AUIPC': '0010111'
    }

    def __init__(self, instruction, rd, imm):
        self.instruction = instruction.upper()
        self.rd = rd
        self.imm = imm

    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')

    def imm_to_bin(self, imm):
        return format(int(imm), '020b')

    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        imm_bin = self.imm_to_bin(self.imm)
        opcode = self.opcode[self.instruction]

        machine_code = (
            imm_bin +
            rd_bin +
            opcode
        )
        return machine_code

class JType:   # only support JAL instruction
    opcode = '1101111'   

    def __init__(self, instruction, rd, imm_offset):
        self.instruction = instruction.upper()
        self.rd = rd
        self.imm_offset = imm_offset    # Offset to the label in bytes

    def reg_to_bin(self, reg):
        if reg in conventions:
            reg = f"x{conventions[reg]}"
        return format(int(reg[1:]), '05b')
    
    def imm_to_bin(self, imm_offset):
        # Convert the immediate offset to a signed 21-bit binary format
        imm_bin = format(imm_offset, '021b') if imm_offset >= 0 else format((1 << 21) + imm_offset, '021b')
    
        # Split bits according to UJ-type format
        imm_20 = imm_bin[0]             # imm[20]
        imm_10_1 = imm_bin[10:20]       # imm[10:1]
        imm_11 = imm_bin[9]             # imm[11]
        imm_19_12 = imm_bin[1:9]        # imm[19:12]
    
        return imm_20, imm_10_1, imm_11, imm_19_12

    def to_machine_code(self):
        rd_bin = self.reg_to_bin(self.rd)
        imm_20, imm_10_1, imm_11, imm_19_12 = self.imm_to_bin(self.imm_offset)

        machine_code = (
            imm_20 +          
            imm_10_1 +        
            imm_11 +          
            imm_19_12 +       
            rd_bin +          
            self.opcode       
        )

        return machine_code