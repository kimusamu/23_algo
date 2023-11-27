def color_argb(value):
    value = value.lstrip('#')
    lv = len(value)
    return [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]


def color_argb_array(array):
    return [color_argb(value) for value in array]


def color_darker(color):
    r, g, b = color
    return [r // 2, g // 2, b // 2]


class Color:
    # from D3.js colors
    pair = color_argb_array(
        ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a",
         "#ffff99", "#b15928"])
    pastel1 = color_argb_array(
        ["#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4", "#fed9a6", "#ffffcc", "#e5d8bd", "#fddaec", "#f2f2f2"])
    pastel2 = color_argb_array(["#b3e2cd", "#fdcdac", "#cbd5e8", "#f4cae4", "#e6f5c9", "#fff2ae", "#f1e2cc", "#cccccc"])
    set1 = color_argb_array(
        ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"])
    set2 = color_argb_array(["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"])
    set3 = color_argb_array(
        ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3", "#fdb462", "#b3de69", "#fccde5", "#d9d9d9", "#bc80bd",
         "#ccebc5", "#ffed6f"])
    dark = color_argb_array(["#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666"])
    gray = color_argb_array(['#f0f0f0', '#dbdbdb', '#c1c1c1', '#9f9f9f', '#7d7d7d', '#5d5d5d', '#383838', '#121212'])
    back = color_argb('#ffffff')
    text = color_argb('#00001f')
    line = dark[0]

    # Browser Colors
    # https://htmlcolorcodes.com/color-names/

    IndianRed = color_argb('#CD5C5C')
    LightCoral = color_argb('#F08080')
    Salmon = color_argb('#FA8072')
    DarkSalmon = color_argb('#E9967A')
    LightSalmon = color_argb('#FFA07A')
    Crimson = color_argb('#DC143C')
    Red = color_argb('#FF0000')
    FireBrick = color_argb('#B22222')
    DarkRed = color_argb('#8B0000')
    RedGroup = [IndianRed, LightCoral, Salmon, DarkSalmon, LightSalmon, Crimson, Red, FireBrick, DarkRed]  # 9 colors

    Pink = color_argb('#FFC0CB')
    LightPink = color_argb('#FFB6C1')
    HotPink = color_argb('#FF69B4')
    DeepPink = color_argb('#FF1493')
    MediumVioletRed = color_argb('#C71585')
    PaleVioletRed = color_argb('#DB7093')
    PinkGroup = [Pink, LightPink, HotPink, DeepPink, MediumVioletRed, PaleVioletRed]  # 6 colors

    LightSalmon = color_argb('#FFA07A')
    Coral = color_argb('#FF7F50')
    Tomato = color_argb('#FF6347')
    OrangeRed = color_argb('#FF4500')
    DarkOrange = color_argb('#FF8C00')
    Orange = color_argb('#FFA500')
    OrangeGroup = [LightSalmon, Coral, Tomato, OrangeRed, DarkOrange, Orange]  # 6 colors

    Gold = color_argb('#FFD700')
    Yellow = color_argb('#FFFF00')
    LightYellow = color_argb('#FFFFE0')
    LemonChiffon = color_argb('#FFFACD')
    LightGoldenrodYellow = color_argb('#FAFAD2')
    PapayaWhip = color_argb('#FFEFD5')
    Moccasin = color_argb('#FFE4B5')
    PeachPuff = color_argb('#FFDAB9')
    PaleGoldenrod = color_argb('#EEE8AA')
    Khaki = color_argb('#F0E68C')
    DarkKhaki = color_argb('#BDB76B')
    YellowGroup = [Gold, Yellow, LightYellow, LemonChiffon, LightGoldenrodYellow, PapayaWhip, Moccasin, PeachPuff,
                   PaleGoldenrod, Khaki, DarkKhaki]  # 11 colors

    Lavender = color_argb('#E6E6FA')
    Thistle = color_argb('#D8BFD8')
    Plum = color_argb('#DDA0DD')
    Violet = color_argb('#EE82EE')
    Orchid = color_argb('#DA70D6')
    Fuchsia = color_argb('#FF00FF')
    Magenta = color_argb('#FF00FF')
    MediumOrchid = color_argb('#BA55D3')
    MediumPurple = color_argb('#9370DB')
    RebeccaPurple = color_argb('#663399')
    BlueViolet = color_argb('#8A2BE2')
    DarkViolet = color_argb('#9400D3')
    DarkOrchid = color_argb('#9932CC')
    DarkMagenta = color_argb('#8B008B')
    Purple = color_argb('#800080')
    Indigo = color_argb('#4B0082')
    SlateBlue = color_argb('#6A5ACD')
    DarkSlateBlue = color_argb('#483D8B')
    MediumSlateBlue = color_argb('#7B68EE')
    PurpleGroup = [Lavender, Thistle, Plum, Violet, Orchid, Fuchsia, Magenta, MediumOrchid, MediumPurple, RebeccaPurple,
                   BlueViolet, DarkViolet, DarkOrchid, DarkMagenta, Purple, Indigo, SlateBlue, DarkSlateBlue,
                   MediumSlateBlue]  # 19 colors

    GreenYellow = color_argb('#ADFF2F')
    Chartreuse = color_argb('#7FFF00')
    LawnGreen = color_argb('#7CFC00')
    Lime = color_argb('#00FF00')
    LimeGreen = color_argb('#32CD32')
    PaleGreen = color_argb('#98FB98')
    LightGreen = color_argb('#90EE90')
    MediumSpringGreen = color_argb('#00FA9A')
    SpringGreen = color_argb('#00FF7F')
    MediumSeaGreen = color_argb('#3CB371')
    SeaGreen = color_argb('#2E8B57')
    ForestGreen = color_argb('#228B22')
    Green = color_argb('#008000')
    DarkGreen = color_argb('#006400')
    YellowGreen = color_argb('#9ACD32')
    OliveDrab = color_argb('#6B8E23')
    Olive = color_argb('#808000')
    DarkOliveGreen = color_argb('#556B2F')
    MediumAquamarine = color_argb('#66CDAA')
    DarkSeaGreen = color_argb('#8FBC8B')
    LightSeaGreen = color_argb('#20B2AA')
    DarkCyan = color_argb('#008B8B')
    Teal = color_argb('#008080')
    GreenGroup = [GreenYellow, Chartreuse, LawnGreen, Lime, LimeGreen, PaleGreen, LightGreen, MediumSpringGreen,
                  SpringGreen, MediumSeaGreen, SeaGreen, ForestGreen, Green, DarkGreen, YellowGreen, OliveDrab, Olive,
                  DarkOliveGreen, MediumAquamarine, DarkSeaGreen, LightSeaGreen, DarkCyan, Teal]  # 23 colors

    Aqua = color_argb('#00FFFF')
    Cyan = color_argb('#00FFFF')
    LightCyan = color_argb('#E0FFFF')
    PaleTurquoise = color_argb('#AFEEEE')
    Aquamarine = color_argb('#7FFFD4')
    Turquoise = color_argb('#40E0D0')
    MediumTurquoise = color_argb('#48D1CC')
    DarkTurquoise = color_argb('#00CED1')
    CadetBlue = color_argb('#5F9EA0')
    SteelBlue = color_argb('#4682B4')
    LightSteelBlue = color_argb('#B0C4DE')
    PowderBlue = color_argb('#B0E0E6')
    LightBlue = color_argb('#ADD8E6')
    SkyBlue = color_argb('#87CEEB')
    LightSkyBlue = color_argb('#87CEFA')
    DeepSkyBlue = color_argb('#00BFFF')
    DodgerBlue = color_argb('#1E90FF')
    CornflowerBlue = color_argb('#6495ED')
    MediumSlateBlue = color_argb('#7B68EE')
    RoyalBlue = color_argb('#4169E1')
    Blue = color_argb('#0000FF')
    MediumBlue = color_argb('#0000CD')
    DarkBlue = color_argb('#00008B')
    Navy = color_argb('#000080')
    MidnightBlue = color_argb('#191970')
    BlueGroup = [Aqua, Cyan, LightCyan, PaleTurquoise, Aquamarine, Turquoise, MediumTurquoise, DarkTurquoise, CadetBlue,
                 SteelBlue, LightSteelBlue, PowderBlue, LightBlue, SkyBlue, LightSkyBlue, DeepSkyBlue, DodgerBlue,
                 CornflowerBlue, MediumSlateBlue, RoyalBlue, Blue, MediumBlue, DarkBlue, Navy,
                 MidnightBlue]  # 25 colors

    Cornsilk = color_argb('#FFF8DC')
    BlanchedAlmond = color_argb('#FFEBCD')
    Bisque = color_argb('#FFE4C4')
    NavajoWhite = color_argb('#FFDEAD')
    Wheat = color_argb('#F5DEB3')
    BurlyWood = color_argb('#DEB887')
    Tan = color_argb('#D2B48C')
    RosyBrown = color_argb('#BC8F8F')
    SandyBrown = color_argb('#F4A460')
    Goldenrod = color_argb('#DAA520')
    DarkGoldenrod = color_argb('#B8860B')
    Peru = color_argb('#CD853F')
    Chocolate = color_argb('#D2691E')
    SaddleBrown = color_argb('#8B4513')
    Sienna = color_argb('#A0522D')
    Brown = color_argb('#A52A2A')
    Maroon = color_argb('#800000')
    BrownGroup = [Cornsilk, BlanchedAlmond, Bisque, NavajoWhite, Wheat, BurlyWood, Tan, RosyBrown, SandyBrown,
                  Goldenrod, DarkGoldenrod, Peru, Chocolate, SaddleBrown, Sienna, Brown, Maroon]  # 17 colors

    White = color_argb('#FFFFFF')
    Snow = color_argb('#FFFAFA')
    HoneyDew = color_argb('#F0FFF0')
    MintCream = color_argb('#F5FFFA')
    Azure = color_argb('#F0FFFF')
    AliceBlue = color_argb('#F0F8FF')
    GhostWhite = color_argb('#F8F8FF')
    WhiteSmoke = color_argb('#F5F5F5')
    SeaShell = color_argb('#FFF5EE')
    Beige = color_argb('#F5F5DC')
    OldLace = color_argb('#FDF5E6')
    FloralWhite = color_argb('#FFFAF0')
    Ivory = color_argb('#FFFFF0')
    AntiqueWhite = color_argb('#FAEBD7')
    Linen = color_argb('#FAF0E6')
    LavenderBlush = color_argb('#FFF0F5')
    MistyRose = color_argb('#FFE4E1')
    WhiteGroup = [White, Snow, HoneyDew, MintCream, Azure, AliceBlue, GhostWhite, WhiteSmoke, SeaShell, Beige, OldLace,
                  FloralWhite, Ivory, AntiqueWhite, Linen, LavenderBlush, MistyRose]  # 17 colors

    Gainsboro = color_argb('#DCDCDC')
    LightGray = color_argb('#D3D3D3')
    Silver = color_argb('#C0C0C0')
    DarkGray = color_argb('#A9A9A9')
    Gray = color_argb('#808080')
    DimGray = color_argb('#696969')
    LightSlateGray = color_argb('#778899')
    SlateGray = color_argb('#708090')
    DarkSlateGray = color_argb('#2F4F4F')
    Black = color_argb('#000000')
    GrayGroup = [Gainsboro, LightGray, Silver, DarkGray, Gray, DimGray, LightSlateGray, SlateGray, DarkSlateGray,
                 Black]  # 10 colors