# md5 : d9af3498fa5fe659c8f65408fdbf3990
# sha1 : 898848790d08c86a05833b841b5f83aaf42b1d03
# sha256 : a9810703b4708fa1e28886bad1e74e53becb8413257fa151f4548609b710215d

ord_names = {
    1: b'ParseURLA',
    2: b'ParseURLW',
    7: b'SHAllocShared',
    8: b'SHLockShared',
    9: b'SHUnlockShared',
    10: b'SHFreeShared',
    12: b'SHCreateMemStream',
    14: b'GetAcceptLanguagesA',
    15: b'GetAcceptLanguagesW',
    16: b'SHCreateThread',
    29: b'IsCharSpaceW',
    151: b'StrCmpNCA',
    152: b'StrCmpNCW',
    153: b'StrCmpNICA',
    154: b'StrCmpNICW',
    155: b'StrCmpCA',
    156: b'StrCmpCW',
    157: b'StrCmpICA',
    158: b'StrCmpICW',
    163: b'IUnknown_QueryStatus',
    164: b'IUnknown_Exec',
    168: b'ConnectToConnectionPoint',
    169: b'IUnknown_AtomicRelease',
    172: b'IUnknown_GetWindow',
    174: b'IUnknown_SetSite',
    176: b'IUnknown_QueryService',
    184: b'IStream_Read',
    185: b'SHMessageBoxCheckA',
    191: b'SHMessageBoxCheckW',
    199: b'IUnknown_Set',
    203: b'SHStripMneumonicA',
    204: b'SHIsChildOrSelf',
    212: b'IStream_Write',
    213: b'IStream_Reset',
    214: b'IStream_Size',
    215: b'SHAnsiToUnicode',
    217: b'SHUnicodeToAnsi',
    218: b'SHUnicodeToAnsiCP',
    219: b'QISearch',
    225: b'SHStripMneumonicW',
    236: b'SHPinDllOfCLSID',
    256: b'IUnknown_GetSite',
    270: b'GUIDFromStringW',
    276: b'WhichPlatform',
    278: b'SHCreateWorkerWindowW',
    280: b'SHRegGetIntW',
    281: b'SHPackDispParamsV',
    345: b'SHAnsiToAnsi',
    346: b'SHUnicodeToUnicode',
    353: b'SHFormatDateTimeA',
    354: b'SHFormatDateTimeW',
    377: b'MLLoadLibraryA',
    378: b'MLLoadLibraryW',
    388: b'ShellMessageBoxW',
    432: b'SHSendMessageBroadcastA',
    433: b'SHSendMessageBroadcastW',
    437: b'IsOS',
    446: b'PathFileExistsAndAttributesW',
    462: b'UrlFixupW',
    467: b'SHRunIndirectRegClientCommand',
    487: b'SHLoadIndirectString',
    500: b'AssocCreate',
    501: b'AssocGetPerceivedType',
    502: b'AssocIsDangerous',
    503: b'AssocQueryKeyA',
    504: b'AssocQueryKeyW',
    512: b'IStream_ReadPidl',
    513: b'IStream_WritePidl',
    515: b'SHGetViewStatePropertyBag',
    553: b'IsInternetESCEnabled',
    567: b'SHPropertyBag_ReadStrAlloc',
    568: b'IStream_Copy',
    569: b'DelayLoadFailureHook',
    570: b'SHPropertyBag_WriteBSTR',
    579: b'AssocQueryStringA',
    584: b'AssocQueryStringByKeyA',
    585: b'AssocQueryStringByKeyW',
    586: b'AssocQueryStringW',
    587: b'ChrCmpIA',
    588: b'ChrCmpIW',
    589: b'ColorAdjustLuma',
    590: b'ColorHLSToRGB',
    591: b'ColorRGBToHLS',
    592: b'DllGetClassObject',
    593: b'DllGetVersion',
    594: b'GetMenuPosFromID',
    595: b'HashData',
    596: b'IStream_ReadStr',
    597: b'IStream_WriteStr',
    607: b'IntlStrEqWorkerA',
    608: b'IntlStrEqWorkerW',
    609: b'IsCharSpaceA',
    610: b'PathAddBackslashA',
    612: b'PathAddBackslashW',
    615: b'SHCreateThreadWithHandle',
    620: b'PathAddExtensionA',
    622: b'PathAddExtensionW',
    623: b'PathAppendA',
    624: b'PathAppendW',
    625: b'PathBuildRootA',
    629: b'SHRegGetValueFromHKCUHKLM',
    630: b'SHRegGetBoolValueFromHKCUHKLM',
    649: b'PathBuildRootW',
    650: b'PathCanonicalizeA',
    651: b'PathCanonicalizeW',
    652: b'PathCombineA',
    653: b'PathCombineW',
    654: b'PathCommonPrefixA',
    655: b'PathCommonPrefixW',
    656: b'PathCompactPathA',
    657: b'PathCompactPathExA',
    658: b'PathCompactPathExW',
    659: b'PathCompactPathW',
    660: b'PathCreateFromUrlA',
    661: b'PathCreateFromUrlAlloc',
    662: b'PathCreateFromUrlW',
    663: b'PathFileExistsA',
    664: b'PathFileExistsW',
    665: b'PathFindExtensionA',
    666: b'PathFindExtensionW',
    667: b'PathFindFileNameA',
    668: b'PathFindFileNameW',
    669: b'PathFindNextComponentA',
    670: b'PathFindNextComponentW',
    671: b'PathFindOnPathA',
    672: b'PathFindOnPathW',
    673: b'PathFindSuffixArrayA',
    674: b'PathFindSuffixArrayW',
    675: b'PathGetArgsA',
    676: b'PathGetArgsW',
    677: b'PathGetCharTypeA',
    678: b'PathGetCharTypeW',
    679: b'PathGetDriveNumberA',
    680: b'PathGetDriveNumberW',
    681: b'PathIsContentTypeA',
    682: b'PathIsContentTypeW',
    683: b'PathIsDirectoryA',
    684: b'PathIsDirectoryEmptyA',
    685: b'PathIsDirectoryEmptyW',
    686: b'PathIsDirectoryW',
    687: b'PathIsFileSpecA',
    688: b'PathIsFileSpecW',
    689: b'PathIsLFNFileSpecA',
    690: b'PathIsLFNFileSpecW',
    691: b'PathIsNetworkPathA',
    692: b'PathIsNetworkPathW',
    693: b'PathIsPrefixA',
    694: b'PathIsPrefixW',
    695: b'PathIsRelativeA',
    696: b'PathIsRelativeW',
    697: b'PathIsRootA',
    698: b'PathIsRootW',
    699: b'PathIsSameRootA',
    700: b'PathIsSameRootW',
    701: b'PathIsSystemFolderA',
    702: b'PathIsSystemFolderW',
    703: b'PathIsUNCA',
    704: b'PathIsUNCServerA',
    705: b'PathIsUNCServerShareA',
    706: b'PathIsUNCServerShareW',
    707: b'PathIsUNCServerW',
    708: b'PathIsUNCW',
    709: b'PathIsURLA',
    710: b'PathIsURLW',
    711: b'PathMakePrettyA',
    712: b'PathMakePrettyW',
    713: b'PathMakeSystemFolderA',
    714: b'PathMakeSystemFolderW',
    715: b'PathMatchSpecA',
    716: b'PathMatchSpecExA',
    717: b'PathMatchSpecExW',
    718: b'PathMatchSpecW',
    719: b'PathParseIconLocationA',
    720: b'PathParseIconLocationW',
    721: b'PathQuoteSpacesA',
    722: b'PathQuoteSpacesW',
    723: b'PathRelativePathToA',
    724: b'PathRelativePathToW',
    725: b'PathRemoveArgsA',
    726: b'PathRemoveArgsW',
    727: b'PathRemoveBackslashA',
    728: b'PathRemoveBackslashW',
    729: b'PathRemoveBlanksA',
    730: b'PathRemoveBlanksW',
    731: b'PathRemoveExtensionA',
    732: b'PathRemoveExtensionW',
    733: b'PathRemoveFileSpecA',
    734: b'PathRemoveFileSpecW',
    735: b'PathRenameExtensionA',
    736: b'PathRenameExtensionW',
    737: b'PathSearchAndQualifyA',
    738: b'PathSearchAndQualifyW',
    739: b'PathSetDlgItemPathA',
    740: b'PathSetDlgItemPathW',
    741: b'PathSkipRootA',
    742: b'PathSkipRootW',
    743: b'PathStripPathA',
    744: b'PathStripPathW',
    745: b'PathStripToRootA',
    746: b'PathStripToRootW',
    747: b'PathUnExpandEnvStringsA',
    748: b'PathUnExpandEnvStringsW',
    749: b'PathUndecorateA',
    750: b'PathUndecorateW',
    751: b'PathUnmakeSystemFolderA',
    752: b'PathUnmakeSystemFolderW',
    753: b'PathUnquoteSpacesA',
    754: b'PathUnquoteSpacesW',
    755: b'SHAutoComplete',
    756: b'SHCopyKeyA',
    757: b'SHCopyKeyW',
    758: b'SHCreateShellPalette',
    759: b'SHCreateStreamOnFileA',
    760: b'SHCreateStreamOnFileEx',
    761: b'SHCreateStreamOnFileW',
    762: b'SHCreateStreamWrapper',
    763: b'SHCreateThreadRef',
    764: b'SHDeleteEmptyKeyA',
    765: b'SHDeleteEmptyKeyW',
    766: b'SHDeleteKeyA',
    767: b'SHDeleteKeyW',
    768: b'SHDeleteOrphanKeyA',
    769: b'SHDeleteOrphanKeyW',
    770: b'SHDeleteValueA',
    771: b'SHDeleteValueW',
    772: b'SHEnumKeyExA',
    773: b'SHEnumKeyExW',
    774: b'SHEnumValueA',
    775: b'SHEnumValueW',
    776: b'SHGetInverseCMAP',
    777: b'SHGetThreadRef',
    778: b'SHGetValueA',
    779: b'SHGetValueW',
    780: b'SHIsLowMemoryMachine',
    781: b'SHOpenRegStream2A',
    782: b'SHOpenRegStream2W',
    783: b'SHOpenRegStreamA',
    784: b'SHOpenRegStreamW',
    785: b'SHQueryInfoKeyA',
    786: b'SHQueryInfoKeyW',
    787: b'SHQueryValueExA',
    788: b'SHQueryValueExW',
    789: b'SHRegCloseUSKey',
    790: b'SHRegCreateUSKeyA',
    791: b'SHRegCreateUSKeyW',
    792: b'SHRegDeleteEmptyUSKeyA',
    793: b'SHRegDeleteEmptyUSKeyW',
    794: b'SHRegDeleteUSValueA',
    795: b'SHRegDeleteUSValueW',
    796: b'SHRegDuplicateHKey',
    797: b'SHRegEnumUSKeyA',
    798: b'SHRegEnumUSKeyW',
    799: b'SHRegEnumUSValueA',
    800: b'SHRegEnumUSValueW',
    801: b'SHRegGetBoolUSValueA',
    802: b'SHRegGetBoolUSValueW',
    803: b'SHRegGetPathA',
    804: b'SHRegGetPathW',
    805: b'SHRegGetUSValueA',
    806: b'SHRegGetUSValueW',
    807: b'SHRegGetValueA',
    808: b'SHRegGetValueW',
    809: b'SHRegOpenUSKeyA',
    810: b'SHRegOpenUSKeyW',
    811: b'SHRegQueryInfoUSKeyA',
    812: b'SHRegQueryInfoUSKeyW',
    813: b'SHRegQueryUSValueA',
    814: b'SHRegQueryUSValueW',
    815: b'SHRegSetPathA',
    816: b'SHRegSetPathW',
    817: b'SHRegSetUSValueA',
    818: b'SHRegSetUSValueW',
    819: b'SHRegWriteUSValueA',
    820: b'SHRegWriteUSValueW',
    821: b'SHRegisterValidateTemplate',
    822: b'SHReleaseThreadRef',
    823: b'SHSetThreadRef',
    824: b'SHSetValueA',
    825: b'SHSetValueW',
    826: b'SHSkipJunction',
    827: b'SHStrDupA',
    828: b'SHStrDupW',
    829: b'ShellMessageBoxA',
    830: b'StrCSpnA',
    831: b'StrCSpnIA',
    832: b'StrCSpnIW',
    833: b'StrCSpnW',
    834: b'StrCatBuffA',
    835: b'StrCatBuffW',
    836: b'StrCatChainW',
    837: b'StrCatW',
    838: b'StrChrA',
    839: b'StrChrIA',
    840: b'StrChrIW',
    841: b'StrChrNIW',
    842: b'StrChrNW',
    843: b'StrChrW',
    844: b'StrCmpIW',
    845: b'StrCmpLogicalW',
    846: b'StrCmpNA',
    847: b'StrCmpNIA',
    848: b'StrCmpNIW',
    849: b'StrCmpNW',
    850: b'StrCmpW',
    851: b'StrCpyNW',
    852: b'StrCpyW',
    853: b'StrDupA',
    854: b'StrDupW',
    855: b'StrFormatByteSize64A',
    856: b'StrFormatByteSizeA',
    857: b'StrFormatByteSizeEx',
    858: b'StrFormatByteSizeW',
    859: b'StrFormatKBSizeA',
    860: b'StrFormatKBSizeW',
    861: b'StrFromTimeIntervalA',
    862: b'StrFromTimeIntervalW',
    863: b'StrIsIntlEqualA',
    864: b'StrIsIntlEqualW',
    865: b'StrNCatA',
    866: b'StrNCatW',
    867: b'StrPBrkA',
    868: b'StrPBrkW',
    869: b'StrRChrA',
    870: b'StrRChrIA',
    871: b'StrRChrIW',
    872: b'StrRChrW',
    873: b'StrRStrIA',
    874: b'StrRStrIW',
    875: b'StrRetToBSTR',
    876: b'StrRetToBufA',
    877: b'StrRetToBufW',
    878: b'StrRetToStrA',
    879: b'StrRetToStrW',
    880: b'StrSpnA',
    881: b'StrSpnW',
    882: b'StrStrA',
    883: b'StrStrIA',
    884: b'StrStrIW',
    885: b'StrStrNIW',
    886: b'StrStrNW',
    887: b'StrStrW',
    888: b'StrToInt64ExA',
    889: b'StrToInt64ExW',
    890: b'StrToIntA',
    891: b'StrToIntExA',
    892: b'StrToIntExW',
    893: b'StrToIntW',
    894: b'StrTrimA',
    895: b'StrTrimW',
    896: b'UrlApplySchemeA',
    897: b'UrlApplySchemeW',
    898: b'UrlCanonicalizeA',
    899: b'UrlCanonicalizeW',
    900: b'UrlCombineA',
    901: b'UrlCombineW',
    902: b'UrlCompareA',
    903: b'UrlCompareW',
    904: b'UrlCreateFromPathA',
    905: b'UrlCreateFromPathW',
    906: b'UrlEscapeA',
    907: b'UrlEscapeW',
    908: b'UrlGetLocationA',
    909: b'UrlGetLocationW',
    910: b'UrlGetPartA',
    911: b'UrlGetPartW',
    912: b'UrlHashA',
    913: b'UrlHashW',
    914: b'UrlIsA',
    915: b'UrlIsNoHistoryA',
    916: b'UrlIsNoHistoryW',
    917: b'UrlIsOpaqueA',
    918: b'UrlIsOpaqueW',
    919: b'UrlIsW',
    920: b'UrlUnescapeA',
    921: b'UrlUnescapeW',
    922: b'wnsprintfA',
    923: b'wnsprintfW',
    924: b'wvnsprintfA',
    925: b'wvnsprintfW',
}