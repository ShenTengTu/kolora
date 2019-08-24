from kolora import color_256_xtrem

xtrem = color_256_xtrem('Silver')
assert xtrem == color_256_xtrem('#c0c0c0')
assert xtrem == 7
xtrem = color_256_xtrem('RoyalBlue1')
assert xtrem == color_256_xtrem('#5f5fff')
assert xtrem == 63
print('[✔] method color_256_xtrem()')