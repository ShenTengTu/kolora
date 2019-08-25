__all__ = ['color_256_xtrem', 'hex_to_rgb', 'rgb_to_hex']

import re

class _Color_Map():
    def __init__(self):
        self.__kv = []
    
    def __call__(self, **kwargs):
        i = 0
        for k in kwargs:
            v = kwargs[k]
            self.__kv.append((i, k, v))
            i += 1
        return self
    
    def name(self, v, default=None):
        for i, k, _v in self.__kv:
            if v == _v:
                return (i, k)
        return default

    def hex(self, k, default=None):
        for i, _k, v in self.__kv:
            if k == _k:
                return (i, v)
        return default

# referance : https://jonasjacek.github.io/colors/
# use `_n` suffix (n is digit) to separate duplicate color name
_COLOR256 = _Color_Map()(
    Black='#000000', Maroon='#800000', Green='#008000', Olive='#808000', 
    Navy='#000080', Purple='#800080', Teal='#008080', Silver='#c0c0c0', 
    Grey='#808080', Red='#ff0000', Lime='#00ff00', Yellow='#ffff00', 
    Blue='#0000ff', Fuchsia='#ff00ff', Aqua='#00ffff', White='#ffffff', 
    Grey0='#000000', NavyBlue='#00005f', DarkBlue='#000087', Blue3_0='#0000af', 
    Blue3_1='#0000d7', Blue1='#0000ff', DarkGreen='#005f00', DeepSkyBlue4_0='#005f5f', 
    DeepSkyBlue4_1='#005f87', DeepSkyBlue4_2='#005faf', DodgerBlue3='#005fd7', DodgerBlue2='#005fff', 
    Green4='#008700', SpringGreen4='#00875f', Turquoise4='#008787', DeepSkyBlue3_0='#0087af', 
    DeepSkyBlue3_1='#0087d7', DodgerBlue1='#0087ff', Green3_0='#00af00', SpringGreen3_0='#00af5f', 
    DarkCyan='#00af87', LightSeaGreen='#00afaf', DeepSkyBlue2='#00afd7', DeepSkyBlue1='#00afff', 
    Green3_1='#00d700', SpringGreen3_1='#00d75f', SpringGreen2_0='#00d787', Cyan3='#00d7af', 
    DarkTurquoise='#00d7d7', Turquoise2='#00d7ff', Green1='#00ff00', SpringGreen2_1='#00ff5f', 
    SpringGreen1='#00ff87', MediumSpringGreen='#00ffaf', Cyan2='#00ffd7', Cyan1='#00ffff', 
    DarkRed_0='#5f0000', DeepPink4_0='#5f005f', Purple4_0='#5f0087', Purple4_1='#5f00af', 
    Purple3='#5f00d7', BlueViolet='#5f00ff', Orange4_0='#5f5f00', Grey37='#5f5f5f', 
    MediumPurple4='#5f5f87', SlateBlue3_0='#5f5faf', SlateBlue3_1='#5f5fd7', RoyalBlue1='#5f5fff', 
    Chartreuse4='#5f8700', DarkSeaGreen4_0='#5f875f', PaleTurquoise4='#5f8787', SteelBlue='#5f87af', 
    SteelBlue3='#5f87d7', CornflowerBlue='#5f87ff', Chartreuse3_0='#5faf00', DarkSeaGreen4_1='#5faf5f', 
    CadetBlue_0='#5faf87', CadetBlue_1='#5fafaf', SkyBlue3='#5fafd7', SteelBlue1_0='#5fafff', 
    Chartreuse3_1='#5fd700', PaleGreen3_0='#5fd75f', SeaGreen3='#5fd787', Aquamarine3='#5fd7af', 
    MediumTurquoise='#5fd7d7', SteelBlue1_1='#5fd7ff', Chartreuse2_0='#5fff00', SeaGreen2='#5fff5f', 
    SeaGreen1_0='#5fff87', SeaGreen1_1='#5fffaf', Aquamarine1_0='#5fffd7', DarkSlateGray2='#5fffff', 
    DarkRed_1='#870000', DeepPink4_1='#87005f', DarkMagenta_0='#870087', DarkMagenta_1='#8700af', 
    DarkViolet_0='#8700d7', Purple_1='#8700ff', Orange4_1='#875f00', LightPink4='#875f5f', 
    Plum4='#875f87', MediumPurple3_0='#875faf', MediumPurple3_1='#875fd7', SlateBlue1='#875fff', 
    Yellow4_0='#878700', Wheat4='#87875f', Grey53='#878787', LightSlateGrey='#8787af', 
    MediumPurple='#8787d7', LightSlateBlue='#8787ff', Yellow4_1='#87af00', DarkOliveGreen3_0='#87af5f', 
    DarkSeaGreen='#87af87', LightSkyBlue3_0='#87afaf', LightSkyBlue3_1='#87afd7', SkyBlue2='#87afff', 
    Chartreuse2_1='#87d700', DarkOliveGreen3_1='#87d75f', PaleGreen3_1='#87d787', DarkSeaGreen3_0='#87d7af', 
    DarkSlateGray3='#87d7d7', SkyBlue1='#87d7ff', Chartreuse1='#87ff00', LightGreen_0='#87ff5f', 
    LightGreen_1='#87ff87', PaleGreen1_0='#87ffaf', Aquamarine1_1='#87ffd7', DarkSlateGray1='#87ffff', 
    Red3_0='#af0000', DeepPink4='#af005f', MediumVioletRed='#af0087', Magenta3='#af00af', 
    DarkViolet_1='#af00d7', Purple_2='#af00ff', DarkOrange3_0='#af5f00', IndianRed_0='#af5f5f', 
    HotPink3_0='#af5f87', MediumOrchid3='#af5faf', MediumOrchid='#af5fd7', MediumPurple2_0='#af5fff', 
    DarkGoldenrod='#af8700', LightSalmon3_0='#af875f', RosyBrown='#af8787', Grey63='#af87af', 
    MediumPurple2_1='#af87d7', MediumPurple1='#af87ff', Gold3_0='#afaf00', DarkKhaki='#afaf5f', 
    NavajoWhite3='#afaf87', Grey69='#afafaf', LightSteelBlue3='#afafd7', LightSteelBlue='#afafff', 
    Yellow3_0='#afd700', DarkOliveGreen3='#afd75f', DarkSeaGreen3_1='#afd787', DarkSeaGreen2_0='#afd7af', 
    LightCyan3='#afd7d7', LightSkyBlue1='#afd7ff', GreenYellow='#afff00', DarkOliveGreen2='#afff5f', 
    PaleGreen1_1='#afff87', DarkSeaGreen2_1='#afffaf', DarkSeaGreen1_0='#afffd7', PaleTurquoise1='#afffff', 
    Red3_1='#d70000', DeepPink3_0='#d7005f', DeepPink3_1='#d70087', Magenta3_0='#d700af', 
    Magenta3_1='#d700d7', Magenta2_0='#d700ff', DarkOrange3_1='#d75f00', IndianRed_1='#d75f5f', 
    HotPink3_1='#d75f87', HotPink2='#d75faf', Orchid='#d75fd7', MediumOrchid1_0='#d75fff', 
    Orange3='#d78700', LightSalmon3_1='#d7875f', LightPink3='#d78787', Pink3='#d787af', 
    Plum3='#d787d7', Violet='#d787ff', Gold3_1='#d7af00', LightGoldenrod3='#d7af5f', 
    Tan='#d7af87', MistyRose3='#d7afaf', Thistle3='#d7afd7', Plum2='#d7afff', 
    Yellow3_1='#d7d700', Khaki3='#d7d75f', LightGoldenrod2='#d7d787', LightYellow3='#d7d7af', 
    Grey84='#d7d7d7', LightSteelBlue1='#d7d7ff', Yellow2='#d7ff00', DarkOliveGreen1_0='#d7ff5f', 
    DarkOliveGreen1_1='#d7ff87', DarkSeaGreen1_1='#d7ffaf', Honeydew2='#d7ffd7', LightCyan1='#d7ffff', 
    Red1='#ff0000', DeepPink2='#ff005f', DeepPink1_0='#ff0087', DeepPink1_1='#ff00af', 
    Magenta2_1='#ff00d7', Magenta1='#ff00ff', OrangeRed1='#ff5f00', IndianRed1_0='#ff5f5f', 
    IndianRed1_1='#ff5f87', HotPink_0='#ff5faf', HotPink_1='#ff5fd7', MediumOrchid1_1='#ff5fff', 
    DarkOrange='#ff8700', Salmon1='#ff875f', LightCoral='#ff8787', PaleVioletRed1='#ff87af', 
    Orchid2='#ff87d7', Orchid1='#ff87ff', Orange1='#ffaf00', SandyBrown='#ffaf5f', 
    LightSalmon1='#ffaf87', LightPink1='#ffafaf', Pink1='#ffafd7', Plum1='#ffafff', 
    Gold1='#ffd700', LightGoldenrod2_0='#ffd75f', LightGoldenrod2_1='#ffd787', NavajoWhite1='#ffd7af', 
    MistyRose1='#ffd7d7', Thistle1='#ffd7ff', Yellow1='#ffff00', LightGoldenrod1='#ffff5f', 
    Khaki1='#ffff87', Wheat1='#ffffaf', Cornsilk1='#ffffd7', Grey100='#ffffff', 
    Grey3='#080808', Grey7='#121212', Grey11='#1c1c1c', Grey15='#262626', 
    Grey19='#303030', Grey23='#3a3a3a', Grey27='#444444', Grey30='#4e4e4e', 
    Grey35='#585858', Grey39='#626262', Grey42='#6c6c6c', Grey46='#767676', 
    Grey50='#808080', Grey54='#8a8a8a', Grey58='#949494', Grey62='#9e9e9e', 
    Grey66='#a8a8a8', Grey70='#b2b2b2', Grey74='#bcbcbc', Grey78='#c6c6c6', 
    Grey82='#d0d0d0', Grey85='#dadada', Grey89='#e4e4e4', Grey93='#eeeeee'
)

def color_256_xtrem(s):
    '''
    Get the xtrem number of 256 colors. Return `None` if not found.
    '''
    item = _COLOR256.name(s)
    if item is None:
        item = _COLOR256.hex(s)
    if type(item) is tuple:
        # item[0] is xtrem, item[1] is corresponding color name or hex code
        return item[0]
    return None

def hex_to_rgb(hex_str: str) -> tuple:
    '''
    Hex color code to RGB tuple

    Hex color code must use full format as '#89abcd'.
    '''
    digits = hex_str[1:]
    return (int(digits[0:2], 16), int(digits[2:4], 16), int(digits[4:6], 16))

def rgb_to_hex(rgb) -> str:
  '''
  RGB to hex color code.

  Argument must be iterable.
  '''
  return '#' + ''.join(map(lambda n: f'{n % 256:0>2x}', rgb[0:3]))

class Kolora():

    __color_deep = {
        '8': 5,
        '24': 2
    }
    __color_side = {
        'fg': 38,
        'bg': 48
    }

    __RESET = '\x1b[0m'

    @staticmethod
    def sgr_escape(*args) -> str:
        '''
        Make SGR (Select Graphic Rendition) escape code.

        Posiotional arguments are SGR parameters.
        '''
        params = ';'.join(map(str, args))
        return f"\x1b[{params}m"

    @staticmethod
    def validate_color_value(obj):
        '''
        `obj` must be color name string, hex color code string or tuple `(r, g, b)`.

        Return the valid formatted value of one of above.
        '''
        t = type(obj)
        tl = [str, tuple]

        if t not in tl:  # type check
            raise TypeError(
                '`obj` must be color name string, hex color code string or tuple `(r, g, b)`')

        if t is tl[0]:  # if is string

            if not str(obj).startswith('#'):  # if is color name
                return obj

            regex = r"^#([a-f0-9]{6}|[a-f0-9]{3})$"  # if is hex color code
            re_groups = re.findall(regex, obj.lower())

            if len(re_groups) < 1:  # formate check
                raise ValueError('hex color code must be like `#f0f` or `#ff00ff`')
            hex_str = re_groups[0]  # hex digits
            if len(hex_str) == 3:  # if is shorthand, extend it
                hex_str = hex_str[0]*2 + hex_str[1]*2 + hex_str[2]*2
            hex_str = '#' + hex_str
            return hex_str

        if t is tl[1]:  # if is tuple

            if len(obj) != 3:  # must contain 3 element
                ValueError('tuple `(r, g, b)` must contain 3 element')
            rgb = tuple([int(x) % 256 for x in obj])  # rgb 0~255 integers
            return rgb

    def __init__(self):
        self.__str = ''
    
    def __call__(self, text: str, deep=8, fg=..., bg=..., reset=False):
        '''
        Make colored text.
        '''
        if reset:
            self.__str += self.__RESET

        _deep = self.__color_deep.get(str(deep), 5)
        
        if fg != ... :
            fg_codes = self.__get_codes(fg, _deep)
            if fg_codes != ... :
                fg_sgr = self.sgr_escape(self.__color_side['fg'], _deep, *fg_codes)
                self.__str += fg_sgr
        if bg != ... :
            bg_codes = self.__get_codes(bg, _deep)
            if bg_codes != ... :
                bg_sgr = self.sgr_escape(self.__color_side['bg'], _deep, *bg_codes)
                self.__str += bg_sgr
        
        self.__str += text
        return self
    
    @property
    def text(self):
        '''
        Colored text
        '''
        return (self.__str + self.__RESET)

    def __get_codes(self, v, deep :int) -> tuple:
        # validate
        color_value = self.validate_color_value(v)

        if deep == 5: # 8 bits color
            xtrem = ...
            if type(color_value) is str: # color name or hex code
                xtrem = color_256_xtrem(color_value)
            elif type(color_value) is tuple: # rgb tuple
                hex_code = rgb_to_hex(color_value)
                xtrem = color_256_xtrem(hex_code)
            # temp return white xtrem code if not found
            return (xtrem,) if xtrem is not None else (15,)
        if deep == 2: # 24 bits color
            rgb = ...
            if type(color_value) is str: # color name or hex code
                regex = r'^#[a-f0-9]{6}$'
                m = re.match(regex, color_value)
                if m is not None: # hex code
                    rgb = hex_to_rgb(color_value)
            elif type(color_value) is tuple: # rgb tuple
                rgb = color_value
            return rgb
            