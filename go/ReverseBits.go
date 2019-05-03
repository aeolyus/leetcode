package main

func reverseBits(num uint32) uint32 {
	r := uint32(0)
	shift := uint32(32)
	for ; num > 0; shift-- {
		r <<= 1
		if num&1 == 1 {
			r ^= 1
		}
		num >>= 1
	}
	return r << shift
}
