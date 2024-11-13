# main program
main:
add t0, t1, t2		# Cộng giá trị của t1 và t2, lưu vào t0
sub t1, t2, t3
and a0, a1, a2

# Các lệnh có immediate
xori a5, a6, -5
andi s7, s8, 20

beq s3, tp, end		# Nếu s3 == tp nhảy đến nhãn end
bne s10, s9, loop	# Nếu s10 != s9 thì nhảy đến nhãn loop

# Một số lệnh khác để test
lui t0, 1000
auipc s11, 100
slli t0, gp, 10
srai tp, a1, 10

jal t0, end

loop: 
	lw t6, 32(t1)
end: nop
func: sh t1, 100(t4)