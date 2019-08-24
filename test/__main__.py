from kolora import color_256_xtrem

print('\n## Functions')
xtrem = color_256_xtrem('Silver')
assert xtrem == color_256_xtrem('#c0c0c0')
assert xtrem == 7
xtrem = color_256_xtrem('RoyalBlue1')
assert xtrem == color_256_xtrem('#5f5fff')
assert xtrem == 63
print('[✔] function color_256_xtrem()')

##---

from kolora.kolora import Kolora

print('\n## Kolora.validate_color_value()')
try:
    Kolora.validate_color_value(1)
except TypeError as err:
    assert err.args[0] == "`obj` must be color name string, hex color code string or tuple `(r, g, b)`"
    print('[✔] `obj` must be color name string, hex color code string or tuple `(r, g, b)`')

assert Kolora.validate_color_value('Silver') == 'Silver'
print('[✔] `obj` is color name')

try:
    Kolora.validate_color_value('#a1b2')
except ValueError as err:
    assert err.args[0] == "hex color code must be like `#f0f` or `#ff00ff`"
    print('[✔] hex color code must be like `#f0f` or `#ff00ff`')

assert Kolora.validate_color_value('#A2F') == '#aa22ff'
print('[✔] extend hex color code shorthand')
assert Kolora.validate_color_value('#A2F3D4') == '#a2f3d4'
print('[✔] normal hex color code')

try:
    Kolora.validate_color_value((1, 2))
except ValueError as err:
    assert err.args[0] == "tuple `(r, g, b)` must contain 3 element"
    print('[✔] tuple `(r, g, b)` must contain 3 element')

assert Kolora.validate_color_value(('123', '456', '789')) == (123, 200, 21)
print('[✔] tuple `(r, g, b)` 0~255 integers')