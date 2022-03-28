# -*- mode: python ; coding: utf-8 -*-
# type: ignore

import python_minifier
import os

for files in ["deverser", "pyimg4"]:
    with open(f"{files}.py", "r") as f, open(f"{files}.min.py", "w") as f2:
        lines = [x for x in f.readlines() if "from typing import" not in x]
        f2.write(
            python_minifier.minify("\n".join(lines), remove_literal_statements=True)
        )


block_cipher = None
debug = False

a = Analysis(
    ["deverser.min.py", "pyimg4.min.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "setuptools",
        "pytest",
        "test",
        "unittest",
        "doctest",
        "IPython",
        "csv",
        "Tkinter",
        "pydoc",
        "tcl",
        "Tkconstants",
        "pywin.debugger",
        "pywin.debugger.dbgcon",
        "pywin.dialogs",
        "distutils",
        "paramiko.compression",
        "tarfile",
        "_gtkagg",
        "_tkagg",
        "curses",
        "black",
        "python_minifier",
        "_codecs_cn",
        "_codecs_jp",
        "_codecs_kr",
        "_codecs_tw",
        "_codecs_hk",
        "_codecs_iso2022",
        "_datetime",
        "_decimal",
        "_statistics",
        "_uuid",
        "_multibytecodec",
        "_lzma",
        "_bz2",
        "_heapq",
        "_multiprocessing",
        "multiprocessing",
        "encodings.cp037",
        "encodings.cp1006",
        "encodings.cp1026",
        "encodings.cp1125",
        "encodings.cp1140",
        "encodings.cp1250",
        "encodings.cp1251",
        "encodings.cp1253",
        "encodings.cp1254",
        "encodings.cp1255",
        "encodings.cp1256",
        "encodings.cp1257",
        "encodings.cp1258",
        "encodings.cp273",
        "encodings.cp424",
        "encodings.cp437",
        "encodings.cp500",
        "encodings.cp720",
        "encodings.cp737",
        "encodings.cp775",
        "encodings.cp850",
        "encodings.cp852",
        "encodings.cp855",
        "encodings.cp856",
        "encodings.cp857",
        "encodings.cp858",
        "encodings.cp860",
        "encodings.cp861",
        "encodings.cp862",
        "encodings.cp863",
        "encodings.cp864",
        "encodings.cp865",
        "encodings.cp866",
        "encodings.cp869",
        "encodings.cp874",
        "encodings.cp875",
        "encodings.cp932",
        "encodings.cp949",
        "encodings.cp950",
        "encodings.euc_jis_2004",
        "encodings.euc_jisx0213",
        "encodings.euc_jp",
        "encodings.euc_kr",
        "encodings.gb18030",
        "encodings.gb2312",
        "encodings.gbk",
        "encodings.hex_codec",
        "encodings.hp_roman8",
        "encodings.hz",
        "encodings.iso2022_jp",
        "encodings.iso2022_jp_1",
        "encodings.iso2022_jp_2",
        "encodings.iso2022_jp_2004",
        "encodings.iso2022_jp_3",
        "encodings.iso2022_jp_ext",
        "encodings.iso2022_kr",
        "encodings.iso8859_1",
        "encodings.iso8859_10",
        "encodings.iso8859_11",
        "encodings.iso8859_13",
        "encodings.iso8859_14",
        "encodings.iso8859_15",
        "encodings.iso8859_16",
        "encodings.iso8859_2",
        "encodings.iso8859_3",
        "encodings.iso8859_4",
        "encodings.iso8859_5",
        "encodings.iso8859_6",
        "encodings.iso8859_7",
        "encodings.iso8859_8",
        "encodings.iso8859_9",
        "encodings.johab",
        "encodings.koi8_r",
        "encodings.koi8_t",
        "encodings.koi8_u",
        "encodings.kz1048",
        "encodings.mac_arabic",
        "encodings.mac_croatian",
        "encodings.mac_cyrillic",
        "encodings.mac_farsi",
        "encodings.mac_greek",
        "encodings.mac_iceland",
        "encodings.mac_latin2",
        "encodings.mac_roman",
        "encodings.mac_romanian",
        "encodings.mac_turkish",
        "encodings.mbcs",
        "encodings.oem",
        "encodings.palmos",
        "encodings.ptcp154",
        "encodings.punycode",
        "encodings.quopri_codec",
        "encodings.rot_13",
        "encodings.shift_jis",
        "encodings.shift_jis_2004",
        "encodings.shift_jisx0213",
        "encodings.tis_620",
        "encodings.undefined",
        "encodings.uu_codec",
        "encodings.zlib_codec",
        "encodings.big5",
        "encodings.big5hkscs",
        "encodings.bz2_codec",
        "_compression",
        "urllib.request",
        "email._encoded_words",
        "email._header_value_parser",
        "email.contentmanager",
        "email.generator",
        "email.headerregistry",
        "email.iterators",
        "email.policy",
        "importlib.metadata",
    ]
    + (["pdb", "code"] if not debug else [])
    + (["encodings.cp1252"] if os.name != "nt" else [])
    + (["encodings.latin1"] if os.name != "posix" else []),
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

excluded_files = [
    "cryptography-36.0.2.dist-info/LICENSE",
    "cryptography-36.0.2.dist-info",
    "cryptography-36.0.2.dist-info/INSTALLER",
    "cryptography-36.0.2.dist-info/REQUESTED",
    "cryptography-36.0.2.dist-info/LICENSE.APACHE",
    "cryptography-36.0.2.dist-info/direct_url.json",
    "cryptography-36.0.2.dist-info/LICENSE.PSF",
    "cryptography-36.0.2.dist-info/LICENSE",
    "cryptography-36.0.2.dist-info/RECORD",
    "cryptography-36.0.2.dist-info/top_level.txt",
    "cryptography-36.0.2.dist-info/WHEEL",
    "cryptography-36.0.2.dist-info/METADATA",
    "cryptography-36.0.2.dist-info/LICENSE.BSD",
    "nacl/py.typed",
    "libintl.8.dylib",
]

a.binaries = TOC([x for x in a.binaries if x[0] not in excluded_files])
a.datas = TOC([x for x in a.datas if x[0] not in excluded_files])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="deverser",
    debug=debug,
    bootloader_ignore_signals=False,
    strip=False if os.name == "nt" else True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
