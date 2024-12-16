# Khởi tạo giá trị với các lệnh khác nhau
    addi x1, x0, 5          # x1 = 5
    add x2, x1, x1          # x2 = x1 + x1 = 10
    lw x1, 8(x3)
    or x3, x1, x2           # x3 = x1 | x2 = 15 (OR logic)
    xor x4, x3, x1          # x4 = x3 ^ x1 = 10 (XOR logic)
    lui x5, 10000           # x5 = 0x10000
    addi x6, x5, 1          # x6 = 0x10000 - 1 = 0xFFFF
    and x7, x5, x6          # x7 = x5 & x6 = 0x10000
    sll x8, x1, x2          # x8 = x1 << x2 (shift left logical)
    srl x9, x8, x2          # x9 = x8 >> x2 (shift right logical)
    slt x10, x1, x2         # x10 = (x1 < x2) = 1 (set less than)
    add x11, x6, x7         # x11 = x6 + x7
    xor x12, x11, x8        # x12 = x11 ^ x8
    and x13, x4, x6         # x13 = x4 & x6
    or x14, x8, x9          # x14 = x8 | x9
    sub x15, x14, x11       # x15 = x14 - x11
    beq x5, x6, end
    jal x1, target
end: auipc x17, 10000
target: add x1, x2, x5
	    sub x5, x4, x7	

    # Lưu các giá trị từ x1 đến x15 vào vùng nhớ array
    la x31, array           # Lấy địa chỉ vùng nhớ array vào x31

    sw x1, 0(x31)           # Lưu x1 vào array[0]
    sw x2, 4(x31)           # Lưu x2 vào array[1]
    sw x3, 8(x31)           # Lưu x3 vào array[2]
    sw x4, 12(x31)          # Lưu x4 vào array[3]
    sw x5, 16(x31)          # Lưu x5 vào array[4]
    sw x6, 20(x31)          # Lưu x6 vào array[5]
    sw x7, 24(x31)          # Lưu x7 vào array[6]
    sw x8, 28(x31)          # Lưu x8 vào array[7]
    sw x9, 32(x31)          # Lưu x9 vào array[8]
    sw x10, 36(x31)         # Lưu x10 vào array[9]
    sw x11, 40(x31)         # Lưu x11 vào array[10]
    sw x12, 44(x31)         # Lưu x12 vào array[11]
    sw x13, 48(x31)         # Lưu x13 vào array[12]
    sw x14, 52(x31)         # Lưu x14 vào array[13]
    sw x15, 56(x31)         # Lưu x15 vào array[14]
    sw x16, 60(x31)         # Lưu x16 vào array[15]
    sw x17, 64(x31)         # Lưu x17 vào array[16]
    sw x18, 68(x31)         # Lưu x18 vào array[17]
    sw x19, 72(x31)         # Lưu x19 vào array[18]
    sw x20, 76(x31)         # Lưu x20 vào array[19]
    sw x21, 80(x31)         # Lưu x21 vào array[20]
    sw x22, 84(x31)         # Lưu x22 vào array[21]
    sw x23, 88(x31)         # Lưu x23 vào array[22]
    sw x24, 92(x31)         # Lưu x24 vào array[23]
    sw x25, 96(x31)         # Lưu x25 vào array[24]
    sw x26, 100(x31)        # Lưu x26 vào array[25]
    sw x27, 104(x31)        # Lưu x27 vào array[26]
    sw x28, 108(x31)        # Lưu x28 vào array[27]
    sw x29, 112(x31)        # Lưu x29 vào array[28]
    sw x30, 116(x31)        # Lưu x30 vào array[29]

    # Kết thúc chương trình