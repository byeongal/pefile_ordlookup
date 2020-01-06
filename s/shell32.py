
ord_names = {
    2: b'SHChangeNotifyRegister',
    3: b'SHDefExtractIconA',
    4: b'SHChangeNotifyDeregister',
    6: b'SHDefExtractIconW',
    9: b'PifMgr_OpenProperties',
    10: b'PifMgr_GetProperties',
    11: b'PifMgr_SetProperties',
    13: b'PifMgr_CloseProperties',
    14: b'SHStartNetConnectionDialogW',
    16: b'ILFindLastID',
    17: b'ILRemoveLastID',
    18: b'ILClone',
    19: b'ILCloneFirst',
    21: b'ILIsEqual',
    22: b'DAD_DragEnterEx2',
    23: b'ILIsParent',
    24: b'ILFindChild',
    25: b'ILCombine',
    27: b'ILSaveToStream',
    28: b'SHILCreateFromPath',
    41: b'IsLFNDriveA',
    42: b'IsLFNDriveW',
    43: b'PathIsExe',
    47: b'PathMakeUniqueName',
    49: b'PathQualify',
    51: b'PathResolve',
    59: b'RestartDialog',
    62: b'PickIconDlg',
    63: b'GetFileNameFromBrowse',
    64: b'DriveType',
    66: b'IsNetDrive',
    67: b'Shell_MergeMenus',
    68: b'SHGetSetSettings',
    71: b'Shell_GetImageLists',
    72: b'Shell_GetCachedImageIndex',
    73: b'SHShellFolderView_Message',
    74: b'SHCreateStdEnumFmtEtc',
    75: b'PathYetAnotherMakeUniqueName',
    77: b'SHMapPIDLToSystemImageListIndex',
    80: b'SHOpenPropSheetW',
    81: b'OpenAs_RunDLL',
    83: b'CIDLData_CreateFromIDArray',
    85: b'OpenRegStream',
    88: b'SHDoDragDrop',
    89: b'SHCloneSpecialIDList',
    90: b'SHFindFiles',
    92: b'PathGetShortPath',
    98: b'SHGetRealIDL',
    100: b'SHRestricted',
    102: b'SHCoCreateInstance',
    103: b'SignalFileOpen',
    119: b'IsLFNDrive',
    125: b'OpenAs_RunDLLA',
    129: b'DAD_AutoScroll',
    131: b'DAD_DragEnterEx',
    132: b'DAD_DragLeave',
    133: b'OpenAs_RunDLLW',
    134: b'DAD_DragMove',
    135: b'PrepareDiscForBurnRunDllW',
    136: b'DAD_SetDragImage',
    137: b'DAD_ShowDragImage',
    138: b'PrintersGetCommand_RunDLL',
    139: b'PrintersGetCommand_RunDLLA',
    147: b'SHCLSIDFromString',
    149: b'SHFind_InitMenuPopup',
    150: b'PrintersGetCommand_RunDLLW',
    152: b'ILGetSize',
    153: b'ILGetNext',
    154: b'ILAppendID',
    155: b'ILFree',
    157: b'ILCreateFromPath',
    162: b'SHSimpleIDListFromPath',
    164: b'Win32DeleteFile',
    165: b'SHCreateDirectory',
    167: b'SHAddFromPropSheetExtArray',
    168: b'SHCreatePropSheetExtArray',
    169: b'SHDestroyPropSheetExtArray',
    170: b'SHReplaceFromPropSheetExtArray',
    171: b'PathCleanupSpec',
    173: b'SHValidateUNC',
    174: b'SHCreateShellFolderViewEx',
    176: b'SHSetInstanceExplorer',
    178: b'SHObjectProperties',
    179: b'SHGetNewLinkInfoA',
    180: b'SHGetNewLinkInfoW',
    182: b'ShellMessageBoxW',
    183: b'ShellMessageBoxA',
    189: b'ILCreateFromPathA',
    190: b'ILCreateFromPathW',
    191: b'SHUpdateImageA',
    192: b'SHUpdateImageW',
    193: b'SHHandleUpdateImage',
    195: b'SHFree',
    196: b'SHAlloc',
    199: b'RealShellExecuteA',
    207: b'RealShellExecuteExA',
    208: b'RealShellExecuteExW',
    226: b'RealShellExecuteW',
    228: b'SHHelpShortcuts_RunDLL',
    229: b'SHHelpShortcuts_RunDLLA',
    231: b'SHSetFolderPathA',
    232: b'SHSetFolderPathW',
    238: b'SHHelpShortcuts_RunDLLW',
    239: b'PathIsSlowW',
    240: b'PathIsSlowA',
    245: b'SHTestTokenMembership',
    255: b'AppCompat_RunDLLW',
    256: b'SHCreateShellFolderView',
    263: b'AssocCreateForClasses',
    267: b'AssocGetDetailsOfPropKey',
    268: b'CheckEscapesW',
    269: b'CommandLineToArgvW',
    272: b'Control_RunDLL',
    273: b'Control_RunDLLA',
    274: b'Control_RunDLLAsUserW',
    275: b'Control_RunDLLW',
    276: b'DllCanUnloadNow',
    277: b'DllGetActivationFactory',
    278: b'DllGetClassObject',
    279: b'DllGetVersion',
    280: b'DllInstall',
    281: b'DllRegisterServer',
    282: b'DllUnregisterServer',
    283: b'DoEnvironmentSubstA',
    284: b'DoEnvironmentSubstW',
    285: b'DragAcceptFiles',
    286: b'DragFinish',
    287: b'DragQueryFile',
    288: b'DragQueryFileA',
    289: b'DragQueryFileAorW',
    290: b'DragQueryFileW',
    291: b'DragQueryPoint',
    292: b'DuplicateIcon',
    293: b'ExtractAssociatedIconA',
    294: b'ExtractAssociatedIconExA',
    295: b'ExtractAssociatedIconExW',
    296: b'ExtractAssociatedIconW',
    297: b'ExtractIconA',
    298: b'ExtractIconEx',
    299: b'ExtractIconExA',
    300: b'ExtractIconExW',
    301: b'ExtractIconW',
    302: b'FindExecutableA',
    303: b'FindExecutableW',
    304: b'FreeIconList',
    305: b'GetCurrentProcessExplicitAppUserModelID',
    306: b'InitNetworkAddressControl',
    307: b'InternalExtractIconListA',
    308: b'InternalExtractIconListW',
    309: b'LaunchMSHelp_RunDLLW',
    310: b'Options_RunDLL',
    311: b'Options_RunDLLA',
    312: b'Options_RunDLLW',
    313: b'PathCleanupSpecWorker',
    314: b'PathIsExeWorker',
    315: b'RegenerateUserEnvironment',
    316: b'RunAsNewUser_RunDLLW',
    317: b'SHAddDefaultPropertiesByExt',
    318: b'SHAddToRecentDocs',
    319: b'SHAppBarMessage',
    320: b'SHAssocEnumHandlers',
    321: b'SHAssocEnumHandlersForProtocolByApplication',
    322: b'SHBindToFolderIDListParent',
    323: b'SHBindToFolderIDListParentEx',
    324: b'SHBindToObject',
    325: b'SHBindToParent',
    326: b'SHBrowseForFolder',
    327: b'SHBrowseForFolderA',
    328: b'SHBrowseForFolderW',
    329: b'SHChangeNotify',
    330: b'SHChangeNotifyRegisterThread',
    331: b'SHChangeNotifySuspendResume',
    332: b'SHCoCreateInstanceWorker',
    333: b'SHCreateAssociationRegistration',
    334: b'SHCreateDataObject',
    335: b'SHCreateDefaultContextMenu',
    336: b'SHCreateDefaultExtractIcon',
    337: b'SHCreateDefaultPropertiesOp',
    338: b'SHCreateDirectoryExA',
    339: b'SHCreateDirectoryExW',
    340: b'SHCreateDirectoryExWWorker',
    341: b'SHCreateItemFromIDList',
    342: b'SHCreateItemFromParsingName',
    343: b'SHCreateItemFromRelativeName',
    344: b'SHCreateItemInKnownFolder',
    345: b'SHCreateItemWithParent',
    346: b'SHCreateLocalServerRunDll',
    347: b'SHCreateProcessAsUserW',
    348: b'SHCreateQueryCancelAutoPlayMoniker',
    349: b'SHCreateShellItem',
    350: b'SHCreateShellItemArray',
    351: b'SHCreateShellItemArrayFromDataObject',
    352: b'SHCreateShellItemArrayFromIDLists',
    353: b'SHCreateShellItemArrayFromShellItem',
    354: b'SHEmptyRecycleBinA',
    355: b'SHEmptyRecycleBinW',
    356: b'SHEnableServiceObject',
    357: b'SHEnumerateUnreadMailAccountsW',
    358: b'SHEvaluateSystemCommandTemplate',
    359: b'SHExtractIconsW',
    360: b'SHFileOperation',
    361: b'SHFileOperationA',
    362: b'SHFileOperationW',
    363: b'SHFormatDrive',
    364: b'SHFreeNameMappings',
    365: b'SHGetDataFromIDListA',
    366: b'SHGetDataFromIDListW',
    367: b'SHGetDesktopFolder',
    368: b'SHGetDesktopFolderWorker',
    369: b'SHGetDiskFreeSpaceA',
    370: b'SHGetDiskFreeSpaceExA',
    371: b'SHGetDiskFreeSpaceExW',
    372: b'SHGetDriveMedia',
    373: b'SHGetFileInfo',
    374: b'SHGetFileInfoA',
    375: b'SHGetFileInfoW',
    376: b'SHGetFileInfoWWorker',
    377: b'SHGetFolderLocation',
    378: b'SHGetFolderLocationWorker',
    379: b'SHGetFolderPathA',
    380: b'SHGetFolderPathAWorker',
    381: b'SHGetFolderPathAndSubDirA',
    382: b'SHGetFolderPathAndSubDirW',
    383: b'SHGetFolderPathAndSubDirWWorker',
    384: b'SHGetFolderPathEx',
    385: b'SHGetFolderPathW',
    386: b'SHGetFolderPathWWorker',
    387: b'SHGetIDListFromObject',
    388: b'SHGetIconOverlayIndexA',
    389: b'SHGetIconOverlayIndexW',
    390: b'SHGetInstanceExplorer',
    391: b'SHGetInstanceExplorerWorker',
    392: b'SHGetItemFromDataObject',
    393: b'SHGetItemFromObject',
    394: b'SHGetKnownFolderIDList',
    395: b'SHGetKnownFolderItem',
    396: b'SHGetKnownFolderPath',
    397: b'SHGetKnownFolderPathWorker',
    398: b'SHGetLocalizedName',
    399: b'SHGetMalloc',
    400: b'SHGetNameFromIDList',
    401: b'SHGetNewLinkInfo',
    402: b'SHGetPathFromIDList',
    403: b'SHGetPathFromIDListA',
    404: b'SHGetPathFromIDListEx',
    405: b'SHGetPathFromIDListW',
    406: b'SHGetPropertyStoreForWindow',
    407: b'SHGetPropertyStoreFromIDList',
    408: b'SHGetPropertyStoreFromParsingName',
    409: b'SHGetSettings',
    410: b'SHGetSpecialFolderLocation',
    411: b'SHGetSpecialFolderPathA',
    412: b'SHGetSpecialFolderPathAWorker',
    413: b'SHGetSpecialFolderPathW',
    414: b'SHGetSpecialFolderPathWWorker',
    415: b'SHGetStockIconInfo',
    416: b'SHGetTemporaryPropertyForItem',
    417: b'SHGetUnreadMailCountW',
    418: b'SHInvokePrinterCommandA',
    419: b'SHInvokePrinterCommandW',
    420: b'SHIsFileAvailableOffline',
    421: b'SHLoadInProc',
    422: b'SHLoadNonloadedIconOverlayIdentifiers',
    423: b'SHOpenFolderAndSelectItems',
    424: b'SHOpenWithDialog',
    425: b'SHParseDisplayName',
    426: b'SHPathPrepareForWriteA',
    427: b'SHPathPrepareForWriteW',
    428: b'SHQueryRecycleBinA',
    429: b'SHQueryRecycleBinW',
    430: b'SHQueryUserNotificationState',
    431: b'SHRemoveLocalizedName',
    432: b'SHResolveLibrary',
    433: b'SHSetDefaultProperties',
    434: b'SHSetKnownFolderPath',
    435: b'SHSetKnownFolderPathWorker',
    436: b'SHSetLocalizedName',
    437: b'SHSetTemporaryPropertyForItem',
    438: b'SHSetUnreadMailCountW',
    439: b'SHShowManageLibraryUI',
    440: b'SHUpdateRecycleBinIcon',
    441: b'SetCurrentProcessExplicitAppUserModelID',
    442: b'SheChangeDirA',
    443: b'SheChangeDirExW',
    444: b'SheGetDirA',
    445: b'SheSetCurDrive',
    446: b'ShellAboutA',
    447: b'ShellAboutW',
    448: b'ShellExec_RunDLL',
    449: b'ShellExec_RunDLLA',
    450: b'ShellExec_RunDLLW',
    451: b'ShellExecuteA',
    452: b'ShellExecuteEx',
    453: b'ShellExecuteExA',
    454: b'ShellExecuteExW',
    455: b'ShellExecuteW',
    456: b'ShellHookProc',
    457: b'Shell_GetCachedImageIndexA',
    458: b'Shell_GetCachedImageIndexW',
    459: b'Shell_NotifyIcon',
    460: b'Shell_NotifyIconA',
    461: b'Shell_NotifyIconGetRect',
    462: b'Shell_NotifyIconW',
    463: b'StrChrA',
    464: b'StrChrIA',
    465: b'StrChrIW',
    466: b'StrChrW',
    467: b'StrCmpNA',
    468: b'StrCmpNIA',
    469: b'StrCmpNIW',
    470: b'StrCmpNW',
    471: b'StrNCmpA',
    472: b'StrNCmpIA',
    473: b'StrNCmpIW',
    474: b'StrNCmpW',
    475: b'StrRChrA',
    476: b'StrRChrIA',
    477: b'StrRChrIW',
    478: b'StrRChrW',
    479: b'StrRStrA',
    480: b'StrRStrIA',
    481: b'StrRStrIW',
    482: b'StrRStrW',
    483: b'StrStrA',
    484: b'StrStrIA',
    485: b'StrStrIW',
    486: b'StrStrW',
    487: b'WOWShellExecute',
    488: b'WaitForExplorerRestartW',
    524: b'RealDriveType',
    526: b'SHFlushSFCache',
    644: b'SHChangeNotification_Lock',
    645: b'SHChangeNotification_Unlock',
    652: b'WriteCabinetState',
    654: b'ReadCabinetState',
    680: b'IsUserAnAdmin',
    682: b'StgMakeUniqueName',
    685: b'SHPropStgCreate',
    688: b'SHPropStgReadMultiple',
    689: b'SHPropStgWriteMultiple',
    701: b'CDefFolderMenu_Create2',
    709: b'SHGetSetFolderCustomSettings',
    716: b'SHMultiFileProperties',
    727: b'SHGetImageList',
    730: b'RestartDialogEx',
    743: b'SHCreateFileExtractIconW',
    747: b'SHLimitInputEdit',
    750: b'SHGetAttributesFromDataObject',
    846: b'ILLoadFromStreamEx',
    919: b'GetSystemPersistedStorageItemList',
    921: b'CreateStorageItemFromShellItem_FullTrustCaller',
    925: b'CreateStorageItemFromShellItem_FullTrustCaller_ForPackage',
    929: b'CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandle',
    931: b'CreateStorageItemFromShellItem_FullTrustCaller_UseImplicitFlagsAndPackage',
}