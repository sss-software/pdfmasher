#!/usr/bin/env  python
# Copyright 2008, Kovid Goyal kovid@kovidgoyal.net
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "GPL v3" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/gplv3_license



from struct import pack

main_language = {
    0 : "NEUTRAL",
    54 : "AFRIKAANS",
    28 : "ALBANIAN",
    1 : "ARABIC",
    43 : "ARMENIAN",
    77 : "ASSAMESE",
    44 : "AZERI",
    45 : "BASQUE",
    35 : "BELARUSIAN",
    69 : "BENGALI",
    2 : "BULGARIAN",
    3 : "CATALAN",
    4 : "CHINESE",
    26 : "CROATIAN",
    5 : "CZECH",
    6 : "DANISH",
    19 : "DUTCH",
    9 : "ENGLISH",
    37 : "ESTONIAN",
    56 : "FAEROESE",
    41 : "FARSI",
    11 : "FINNISH",
    12 : "FRENCH",
    55 : "GEORGIAN",
    7 : "GERMAN",
    8 : "GREEK",
    71 : "GUJARATI",
    13 : "HEBREW",
    57 : "HINDI",
    14 : "HUNGARIAN",
    15 : "ICELANDIC",
    33 : "INDONESIAN",
    16 : "ITALIAN",
    17 : "JAPANESE",
    75 : "KANNADA",
    63 : "KAZAK",
    87 : "KONKANI",
    18 : "KOREAN",
    38 : "LATVIAN",
    39 : "LITHUANIAN",
    47 : "MACEDONIAN",
    62 : "MALAY",
    76 : "MALAYALAM",
    58 : "MALTESE",
    78 : "MARATHI",
    97 : "NEPALI",
    20 : "NORWEGIAN",
    72 : "ORIYA",
    21 : "POLISH",
    22 : "PORTUGUESE",
    70 : "PUNJABI",
    23 : "RHAETOROMANIC",
    24 : "ROMANIAN",
    25 : "RUSSIAN",
    59 : "SAMI",
    79 : "SANSKRIT",
    26 : "SERBIAN",
    27 : "SLOVAK",
    36 : "SLOVENIAN",
    46 : "SORBIAN",
    10 : "SPANISH",
    48 : "SUTU",
    65 : "SWAHILI",
    29 : "SWEDISH",
    73 : "TAMIL",
    68 : "TATAR",
    74 : "TELUGU",
    30 : "THAI",
    49 : "TSONGA",
    50 : "TSWANA",
    31 : "TURKISH",
    34 : "UKRAINIAN",
    32 : "URDU",
    67 : "UZBEK",
    42 : "VIETNAMESE",
    52 : "XHOSA",
    53 : "ZULU",
}

sub_language = {
    0 : "NEUTRAL",
    1 : "ARABIC_SAUDI_ARABIA",
    2 : "ARABIC_IRAQ",
    3 : "ARABIC_EGYPT",
    4 : "ARABIC_LIBYA",
    5 : "ARABIC_ALGERIA",
    6 : "ARABIC_MOROCCO",
    7 : "ARABIC_TUNISIA",
    8 : "ARABIC_OMAN",
    9 : "ARABIC_YEMEN",
    10 : "ARABIC_SYRIA",
    11 : "ARABIC_JORDAN",
    12 : "ARABIC_LEBANON",
    13 : "ARABIC_KUWAIT",
    14 : "ARABIC_UAE",
    15 : "ARABIC_BAHRAIN",
    16 : "ARABIC_QATAR",
    1 : "AZERI_LATIN",
    2 : "AZERI_CYRILLIC",
    1 : "CHINESE_TRADITIONAL",
    2 : "CHINESE_SIMPLIFIED",
    3 : "CHINESE_HONGKONG",
    4 : "CHINESE_SINGAPORE",
    1 : "DUTCH",
    2 : "DUTCH_BELGIAN",
    1 : "FRENCH",
    2 : "FRENCH_BELGIAN",
    3 : "FRENCH_CANADIAN",
    4 : "FRENCH_SWISS",
    5 : "FRENCH_LUXEMBOURG",
    6 : "FRENCH_MONACO",
    1 : "GERMAN",
    2 : "GERMAN_SWISS",
    3 : "GERMAN_AUSTRIAN",
    4 : "GERMAN_LUXEMBOURG",
    5 : "GERMAN_LIECHTENSTEIN",
    1 : "ITALIAN",
    2 : "ITALIAN_SWISS",
    1 : "KOREAN",
    1 : "LITHUANIAN",
    1 : "MALAY_MALAYSIA",
    2 : "MALAY_BRUNEI_DARUSSALAM",
    1 : "NORWEGIAN_BOKMAL",
    2 : "NORWEGIAN_NYNORSK",
    2 : "PORTUGUESE",
    1 : "PORTUGUESE_BRAZILIAN",
    2 : "SERBIAN_LATIN",
    3 : "SERBIAN_CYRILLIC",
    1 : "SPANISH",
    2 : "SPANISH_MEXICAN",
    4 : "SPANISH_GUATEMALA",
    5 : "SPANISH_COSTA_RICA",
    6 : "SPANISH_PANAMA",
    7 : "SPANISH_DOMINICAN_REPUBLIC",
    8 : "SPANISH_VENEZUELA",
    9 : "SPANISH_COLOMBIA",
    10 : "SPANISH_PERU",
    11 : "SPANISH_ARGENTINA",
    12 : "SPANISH_ECUADOR",
    13 : "SPANISH_CHILE",
    14 : "SPANISH_URUGUAY",
    15 : "SPANISH_PARAGUAY",
    16 : "SPANISH_BOLIVIA",
    17 : "SPANISH_EL_SALVADOR",
    18 : "SPANISH_HONDURAS",
    19 : "SPANISH_NICARAGUA",
    20 : "SPANISH_PUERTO_RICO",
    1 : "SWEDISH",
    2 : "SWEDISH_FINLAND",
    1 : "UZBEK_LATIN",
    2 : "UZBEK_CYRILLIC",
}

IANA_MOBI = \
    {None: {None: (0, 0)},
     'af': {None: (54, 0)},
     'ar': {None: (1, 0),
            'AE': (1, 56),
            'BH': (1, 60),
            'DZ': (1, 20),
            'EG': (1, 12),
            'JO': (1, 44),
            'KW': (1, 52),
            'LB': (1, 48),
            'MA': (1, 24),
            'OM': (1, 32),
            'QA': (1, 64),
            'SA': (1, 4),
            'SY': (1, 40),
            'TN': (1, 28),
            'YE': (1, 36)},
     'as': {None: (77, 0)},
     'az': {None: (44, 0)},
     'be': {None: (35, 0)},
     'bg': {None: (2, 0)},
     'bn': {None: (69, 0)},
     'ca': {None: (3, 0)},
     'cs': {None: (5, 0)},
     'da': {None: (6, 0)},
     'de': {None: (7, 0),
            'AT': (7, 12),
            'CH': (7, 8),
            'LI': (7, 20),
            'LU': (7, 16)},
     'el': {None: (8, 0)},
     'en': {None: (9, 0),
            'AU': (9, 12),
            'BZ': (9, 40),
            'CA': (9, 16),
            'GB': (9, 8),
            'IE': (9, 24),
            'JM': (9, 32),
            'NZ': (9, 20),
            'PH': (9, 52),
            'TT': (9, 44),
            'US': (9, 4),
            'ZA': (9, 28),
            'ZW': (9, 48)},
     'es': {None: (10, 0),
            'AR': (10, 44),
            'BO': (10, 64),
            'CL': (10, 52),
            'CO': (10, 36),
            'CR': (10, 20),
            'DO': (10, 28),
            'EC': (10, 48),
            'ES': (10, 4),
            'GT': (10, 16),
            'HN': (10, 72),
            'MX': (10, 8),
            'NI': (10, 76),
            'PA': (10, 24),
            'PE': (10, 40),
            'PR': (10, 80),
            'PY': (10, 60),
            'SV': (10, 68),
            'UY': (10, 56),
            'VE': (10, 32)},
     'et': {None: (37, 0)},
     'eu': {None: (45, 0)},
     'fa': {None: (41, 0)},
     'fi': {None: (11, 0)},
     'fo': {None: (56, 0)},
     'fr': {None: (12, 0),
            'BE': (12, 8),
            'CA': (12, 12),
            'CH': (12, 16),
            'FR': (12, 4),
            'LU': (12, 20),
            'MC': (12, 24)},
     'gu': {None: (71, 0)},
     'he': {None: (13, 0)},
     'hi': {None: (57, 0)},
     'hr': {None: (26, 0)},
     'hu': {None: (14, 0)},
     'hy': {None: (43, 0)},
     'id': {None: (33, 0)},
     'is': {None: (15, 0)},
     'it': {None: (16, 0),
            'CH': (16, 8),
            'IT': (16, 4)},
     'ja': {None: (17, 0)},
     'ka': {None: (55, 0)},
     'kk': {None: (63, 0)},
     'kn': {None: (75, 0)},
     'ko': {None: (18, 0)},
     'kok': {None: (87, 0)},
     'lt': {None: (39, 0)},
     'lv': {None: (38, 0)},
     'mk': {None: (47, 0)},
     'ml': {None: (76, 0)},
     'mr': {None: (78, 0)},
     'ms': {None: (62, 0)},
     'mt': {None: (58, 0)},
     'ne': {None: (97, 0)},
     'nl': {None: (19, 0),
            'BE': (19, 8)},
     'no': {None: (20, 0)},
     'or': {None: (72, 0)},
     'pa': {None: (70, 0)},
     'pl': {None: (21, 0)},
     'pt': {None: (22, 0),
            'BR': (22, 4),
            'PT': (22, 8)},
     'rm': {None: (23, 0)},
     'ro': {None: (24, 0)},
     'ru': {None: (25, 0)},
     'sa': {None: (79, 0)},
     'se': {None: (59, 0)},
     'sk': {None: (27, 0)},
     'sl': {None: (36, 0)},
     'sq': {None: (28, 0)},
     'sr': {None: (26, 12),
            'RS': (26, 12)},
     'st': {None: (48, 0)},
     'sv': {None: (29, 0),
            'FI': (29, 8)},
     'sw': {None: (65, 0)},
     'ta': {None: (73, 0)},
     'te': {None: (74, 0)},
     'th': {None: (30, 0)},
     'tn': {None: (50, 0)},
     'tr': {None: (31, 0)},
     'ts': {None: (49, 0)},
     'tt': {None: (68, 0)},
     'uk': {None: (34, 0)},
     'ur': {None: (32, 0)},
     'uz': {None: (67, 0),
            'UZ': (67, 8)},
     'vi': {None: (42, 0)},
     'wen': {None: (46, 0)},
     'xh': {None: (52, 0)},
     'zh': {None: (4, 0),
            'CN': (4, 8),
            'HK': (4, 12),
            'SG': (4, 16),
            'TW': (4, 4)},
     'zu': {None: (53, 0)}}

def iana2mobi(icode):
    langdict, subtags = IANA_MOBI[None], []
    if icode:
        subtags = list(icode.split('-'))
        while len(subtags) > 0:
            lang = subtags.pop(0).lower()
            if lang in IANA_MOBI:
                langdict = IANA_MOBI[lang]
                break

    mcode = langdict[None]
    while len(subtags) > 0:
        subtag = subtags.pop(0)
        if subtag not in langdict:
            subtag = subtag.title()
        if subtag not in langdict:
            subtag = subtag.upper()
        if subtag in langdict:
            mcode = langdict[subtag]
            break
    return pack(b'>HBB', 0, mcode[1], mcode[0])

def mobi2iana(langcode, sublangcode):
    prefix = suffix = None
    for code, d in list(IANA_MOBI.items()):
        for subcode, t in list(d.items()):
            cc, cl = t
            if cc == langcode:
                prefix = code
            if cl == sublangcode:
                suffix = subcode.lower() if subcode else None
                break
        if prefix is not None:
            break
    if prefix is None:
        return 'und'
    if suffix is None:
        return prefix
    return prefix + '-' + suffix