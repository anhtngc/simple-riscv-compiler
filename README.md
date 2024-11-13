# Simple RISC-V Compiler
## 1️⃣ Overview:
This project is a lightweight, educational RISC-V compiler that translates RISC-V assembly instructions into machine code. Designed for learning and experimentation, this compiler helps beginners understand how RISC-V instructions are parsed, processed, and converted into binary format. It covers fundamental RISC-V instruction types, including R, I, S, B, U, and J, providing hands-on experience with compiler development.

## 2️⃣ Key Features:
- **Instruction Parsing**: Supports essential RISC-V instruction types, such as arithmetic, logic, branch, load/store, and jump instructions.
- **Label Handling**: Automatically calculates and resolves label addresses within the code for branch and jump instructions.
- **Error Handling**: Detects unsupported or invalid instructions with appropriate warnings for easy debugging.
- **Flexible Register Naming**: Allows use of conventional RISC-V register names (e.g., a0, t1) for user-friendly assembly code.

## 3️⃣ Getting Started:
Before using the my Siny RISC-V Compiler, ensure you have the following installed: `python 3.x`
### Installation
Clone the repository:
```bash
git clone https://github.com/anhtngc/simple-riscv-compiler.git
cd simple-riscv-compiler
```
### Usage
#### 1. Edit your RISC-V Assembly codes:
Modify the content of the `code.asm` file with your RISC-V Assembly instructions.
#### 2. Compile the file containing RISC-V Assembly codes:
Run the following command to compile your assembly code:
```bash
    python3 main.py
```
#### 3. Result:
The compiled binary machine codes output will be generated and saved (created) in the `output.txt` file (this file is stored in the same directory with `main.py`)

### 4️⃣ Supported Instructions:
The Simple RISC-V Compiler supports the full suite of standard RISC-V instructions, including:
- **Loads**: `lb`, `lh`, `lw`, `lbu`, `lhu`
- **Stores**: `sb`, `sw`, `sw`
- **Shifts**: `sll`, `slli`, `srl`, `srli`, `sra`, `srai`
- **Arithmetic**: `add`, `addi`, `sub`, `lui`, `auipc`
- **Logical**: `xor`, `xori`, `or`, `ori`, `and`, `andi`
- **Compare**: `slt`, `slti`, `sltu`, `sltiu`
- **Branches**: `beq`, `bne`, `blt`, `bge`, `bltu`, `bgeu`
- **Jump & Link**: `jal`

Note that the commands `nop`, `ret`, ect are being ignored and cannot be converted into binary machine code.

