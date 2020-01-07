# md5 : 2cdb8e874f0950ea17a7135427b4f07d
# sha1 : 73b16f132eb0247ea124b6243ca4109f179e564c
# sha256 : 099b17422e1df0235e024ff5128a60571e72af451e1c59f4d61d3cf32c1539ed

ord_names = {
    3: b'mciExecute',
    4: b'CloseDriver',
    5: b'DefDriverProc',
    6: b'DriverCallback',
    7: b'DrvGetModuleHandle',
    8: b'GetDriverModuleHandle',
    9: b'NotifyCallbackData',
    10: b'OpenDriver',
    11: b'PlaySound',
    12: b'PlaySoundA',
    13: b'PlaySoundW',
    14: b'SendDriverMessage',
    15: b'WOW32DriverCallback',
    16: b'WOW32ResolveMultiMediaHandle',
    17: b'WOWAppExit',
    18: b'aux32Message',
    19: b'auxGetDevCapsA',
    20: b'auxGetDevCapsW',
    21: b'auxGetNumDevs',
    22: b'auxGetVolume',
    23: b'auxOutMessage',
    24: b'auxSetVolume',
    25: b'joy32Message',
    26: b'joyConfigChanged',
    27: b'joyGetDevCapsA',
    28: b'joyGetDevCapsW',
    29: b'joyGetNumDevs',
    30: b'joyGetPos',
    31: b'joyGetPosEx',
    32: b'joyGetThreshold',
    33: b'joyReleaseCapture',
    34: b'joySetCapture',
    35: b'joySetThreshold',
    36: b'mci32Message',
    37: b'mciDriverNotify',
    38: b'mciDriverYield',
    39: b'mciFreeCommandResource',
    40: b'mciGetCreatorTask',
    41: b'mciGetDeviceIDA',
    42: b'mciGetDeviceIDFromElementIDA',
    43: b'mciGetDeviceIDFromElementIDW',
    44: b'mciGetDeviceIDW',
    45: b'mciGetDriverData',
    46: b'mciGetErrorStringA',
    47: b'mciGetErrorStringW',
    48: b'mciGetYieldProc',
    49: b'mciLoadCommandResource',
    50: b'mciSendCommandA',
    51: b'mciSendCommandW',
    52: b'mciSendStringA',
    53: b'mciSendStringW',
    54: b'mciSetDriverData',
    55: b'mciSetYieldProc',
    56: b'mid32Message',
    57: b'midiConnect',
    58: b'midiDisconnect',
    59: b'midiInAddBuffer',
    60: b'midiInClose',
    61: b'midiInGetDevCapsA',
    62: b'midiInGetDevCapsW',
    63: b'midiInGetErrorTextA',
    64: b'midiInGetErrorTextW',
    65: b'midiInGetID',
    66: b'midiInGetNumDevs',
    67: b'midiInMessage',
    68: b'midiInOpen',
    69: b'midiInPrepareHeader',
    70: b'midiInReset',
    71: b'midiInStart',
    72: b'midiInStop',
    73: b'midiInUnprepareHeader',
    74: b'midiOutCacheDrumPatches',
    75: b'midiOutCachePatches',
    76: b'midiOutClose',
    77: b'midiOutGetDevCapsA',
    78: b'midiOutGetDevCapsW',
    79: b'midiOutGetErrorTextA',
    80: b'midiOutGetErrorTextW',
    81: b'midiOutGetID',
    82: b'midiOutGetNumDevs',
    83: b'midiOutGetVolume',
    84: b'midiOutLongMsg',
    85: b'midiOutMessage',
    86: b'midiOutOpen',
    87: b'midiOutPrepareHeader',
    88: b'midiOutReset',
    89: b'midiOutSetVolume',
    90: b'midiOutShortMsg',
    91: b'midiOutUnprepareHeader',
    92: b'midiStreamClose',
    93: b'midiStreamOpen',
    94: b'midiStreamOut',
    95: b'midiStreamPause',
    96: b'midiStreamPosition',
    97: b'midiStreamProperty',
    98: b'midiStreamRestart',
    99: b'midiStreamStop',
    100: b'mixerClose',
    101: b'mixerGetControlDetailsA',
    102: b'mixerGetControlDetailsW',
    103: b'mixerGetDevCapsA',
    104: b'mixerGetDevCapsW',
    105: b'mixerGetID',
    106: b'mixerGetLineControlsA',
    107: b'mixerGetLineControlsW',
    108: b'mixerGetLineInfoA',
    109: b'mixerGetLineInfoW',
    110: b'mixerGetNumDevs',
    111: b'mixerMessage',
    112: b'mixerOpen',
    113: b'mixerSetControlDetails',
    114: b'mmDrvInstall',
    115: b'mmGetCurrentTask',
    116: b'mmTaskBlock',
    117: b'mmTaskCreate',
    118: b'mmTaskSignal',
    119: b'mmTaskYield',
    120: b'mmioAdvance',
    121: b'mmioAscend',
    122: b'mmioClose',
    123: b'mmioCreateChunk',
    124: b'mmioDescend',
    125: b'mmioFlush',
    126: b'mmioGetInfo',
    127: b'mmioInstallIOProcA',
    128: b'mmioInstallIOProcW',
    129: b'mmioOpenA',
    130: b'mmioOpenW',
    131: b'mmioRead',
    132: b'mmioRenameA',
    133: b'mmioRenameW',
    134: b'mmioSeek',
    135: b'mmioSendMessage',
    136: b'mmioSetBuffer',
    137: b'mmioSetInfo',
    138: b'mmioStringToFOURCCA',
    139: b'mmioStringToFOURCCW',
    140: b'mmioWrite',
    141: b'mmsystemGetVersion',
    142: b'mod32Message',
    143: b'mxd32Message',
    144: b'sndPlaySoundA',
    145: b'sndPlaySoundW',
    146: b'tid32Message',
    147: b'timeBeginPeriod',
    148: b'timeEndPeriod',
    149: b'timeGetDevCaps',
    150: b'timeGetSystemTime',
    151: b'timeGetTime',
    152: b'timeKillEvent',
    153: b'timeSetEvent',
    154: b'waveInAddBuffer',
    155: b'waveInClose',
    156: b'waveInGetDevCapsA',
    157: b'waveInGetDevCapsW',
    158: b'waveInGetErrorTextA',
    159: b'waveInGetErrorTextW',
    160: b'waveInGetID',
    161: b'waveInGetNumDevs',
    162: b'waveInGetPosition',
    163: b'waveInMessage',
    164: b'waveInOpen',
    165: b'waveInPrepareHeader',
    166: b'waveInReset',
    167: b'waveInStart',
    168: b'waveInStop',
    169: b'waveInUnprepareHeader',
    170: b'waveOutBreakLoop',
    171: b'waveOutClose',
    172: b'waveOutGetDevCapsA',
    173: b'waveOutGetDevCapsW',
    174: b'waveOutGetErrorTextA',
    175: b'waveOutGetErrorTextW',
    176: b'waveOutGetID',
    177: b'waveOutGetNumDevs',
    178: b'waveOutGetPitch',
    179: b'waveOutGetPlaybackRate',
    180: b'waveOutGetPosition',
    181: b'waveOutGetVolume',
    182: b'waveOutMessage',
    183: b'waveOutOpen',
    184: b'waveOutPause',
    185: b'waveOutPrepareHeader',
    186: b'waveOutReset',
    187: b'waveOutRestart',
    188: b'waveOutSetPitch',
    189: b'waveOutSetPlaybackRate',
    190: b'waveOutSetVolume',
    191: b'waveOutUnprepareHeader',
    192: b'waveOutWrite',
    193: b'wid32Message',
    194: b'wod32Message',
}