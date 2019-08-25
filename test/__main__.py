from kolora import color_256_xtrem, hex_to_rgb, rgb_to_hex

print('\n## Functions')
xtrem = color_256_xtrem('Silver')
assert xtrem == color_256_xtrem('#c0c0c0')
assert xtrem == 7
xtrem = color_256_xtrem('RoyalBlue1')
assert xtrem == color_256_xtrem('#5f5fff')
assert xtrem == 63
print('[✔] function color_256_xtrem()')

assert hex_to_rgb('#89abcd') == (137, 171, 205)
print('[✔] function hex_to_rgb()')
assert rgb_to_hex((137, 171, 205)) == '#89abcd'
print('[✔] function rgb_to_hex()')

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

##--

print('\n## Kolora.sgr_escape()')
# 8 bit frontground color #ff0000
assert Kolora.sgr_escape(38, 5, 9) == "\x1b[38;5;9m"
print('[✔] 8 bit frontground color')
# ISO-8613-3 24 bit background color #89abcd rgb(137, 171, 205)
assert Kolora.sgr_escape(48, 2, *(137, 171, 205)) == "\x1b[48;2;137;171;205m"
print('[✔] ISO-8613-3 24 bit background color')

##--

print('\n## callable Kolora instance (make colored text)')
assert Kolora()('normal').text == 'normal\x1b[0m'
print('[✔] No specify color at first')

s = "fg='Aqua',bg='Violet'"
txt = Kolora()(s, fg='Aqua', bg='Violet').text
assert txt == ('\x1b[38;5;14m\x1b[48;5;177m' + s + '\x1b[0m')
print('[✔] 8bit color name (in mapping)')

s = "fg='#00ffff',bg='#d787ff'"
txt = Kolora()(s, fg='#00ffff', bg='#d787ff').text
assert txt == ('\x1b[38;5;14m\x1b[48;5;177m' + s + '\x1b[0m')
print('[✔] 8bit hex code (in mapping)')

s = "fg=(0, 255, 255), bg=(215, 135, 255)"
txt = Kolora()(s, fg=(0, 255, 255), bg=(215, 135, 255)).text
assert txt == ('\x1b[38;5;14m\x1b[48;5;177m' + s + '\x1b[0m')
print('[✔] 8bit rgb tuple (in mapping)')

s = "fg='Aquaaa', bg='Violettt'"
txt = Kolora()(s, fg='Aquaaa', bg='Violettt').text
# temp return white xtrem code if not found
assert txt == ('\x1b[38;5;15m\x1b[48;5;15m' + s + '\x1b[0m')
print('[✔] 8bit color name (not in mapping)')

s = "fg='#00fffe', bg='#d787fe'"
txt = Kolora()(s, fg='#00fffe', bg='#d787fe').text
# temp return white xtrem code if not found
assert txt == ('\x1b[38;5;15m\x1b[48;5;15m' + s + '\x1b[0m')
print('[✔] 8bit hex code (not in mapping)')

s = "fg=(1, 255, 255), bg=(216, 135, 255)"
txt = Kolora()(s, fg=(1, 255, 255), bg=(216, 135, 255)).text
# temp return white xtrem code if not found
assert txt == ('\x1b[38;5;15m\x1b[48;5;15m' + s + '\x1b[0m')
print('[✔] 8bit rgb tuple (in mapping)')

s = "deep=24, fg='Aqua', bg='Violet'"
txt = Kolora()(s, deep=24, fg='Aqua', bg='Violet').text
assert txt == (s + '\x1b[0m')
print('[✔] 24bit color name (not support)')

s = "deep=24, fg='#00ffff',bg='#d787ff'"
txt = Kolora()(s, deep=24, fg='#00ffff',bg='#d787ff').text
assert txt == ('\x1b[38;2;0;255;255m\x1b[48;2;215;135;255m' + s + '\x1b[0m')
print('[✔] 24bit hex code')

s = "deep=24, fg=(0, 255, 255), bg=(215, 135, 255)"
txt = Kolora()(s, deep=24, fg=(0, 255, 255), bg=(215, 135, 255)).text
assert txt == ('\x1b[38;2;0;255;255m\x1b[48;2;215;135;255m' + s + '\x1b[0m')
print('[✔] 24bit rgb tuple')

s = 'Chain'
txt = Kolora()(
    s[0],
    bg='Maroon'
    )(
        s[1],
        bg='Green'
    )(
        s[2], # still Green
    )(
        s[3],
        reset= True # reset in chain
    )(
        s[4],
        bg='Olive'
    ).text
assert txt == ('\x1b[48;5;1m' + s[0] + '\x1b[48;5;2m' + s[1:3] + '\x1b[0m' + s[3] + '\x1b[48;5;3m'+ s[4] + '\x1b[0m')
print('[✔] invoke chaining & reset color in chain')