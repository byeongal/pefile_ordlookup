
ord_names = {
    1: b'SQLAllocConnect',
    2: b'SQLAllocEnv',
    3: b'SQLAllocStmt',
    4: b'SQLBindCol',
    5: b'SQLCancel',
    6: b'SQLColAttributes',
    7: b'SQLConnect',
    8: b'SQLDescribeCol',
    9: b'SQLDisconnect',
    10: b'SQLError',
    11: b'SQLExecDirect',
    12: b'SQLExecute',
    13: b'SQLFetch',
    14: b'SQLFreeConnect',
    15: b'SQLFreeEnv',
    16: b'SQLFreeStmt',
    17: b'SQLGetCursorName',
    18: b'SQLNumResultCols',
    19: b'SQLPrepare',
    20: b'SQLRowCount',
    21: b'SQLSetCursorName',
    22: b'SQLSetParam',
    23: b'SQLTransact',
    24: b'SQLAllocHandle',
    25: b'SQLBindParam',
    26: b'SQLCloseCursor',
    27: b'SQLColAttribute',
    28: b'SQLCopyDesc',
    29: b'SQLEndTran',
    30: b'SQLFetchScroll',
    31: b'SQLFreeHandle',
    32: b'SQLGetConnectAttr',
    33: b'SQLGetDescField',
    34: b'SQLGetDescRec',
    35: b'SQLGetDiagField',
    36: b'SQLGetDiagRec',
    37: b'SQLGetEnvAttr',
    38: b'SQLGetStmtAttr',
    39: b'SQLSetConnectAttr',
    40: b'SQLColumns',
    41: b'SQLDriverConnect',
    42: b'SQLGetConnectOption',
    43: b'SQLGetData',
    44: b'SQLGetFunctions',
    45: b'SQLGetInfo',
    46: b'SQLGetStmtOption',
    47: b'SQLGetTypeInfo',
    48: b'SQLParamData',
    49: b'SQLPutData',
    50: b'SQLSetConnectOption',
    51: b'SQLSetStmtOption',
    52: b'SQLSpecialColumns',
    53: b'SQLStatistics',
    54: b'SQLTables',
    55: b'SQLBrowseConnect',
    56: b'SQLColumnPrivileges',
    57: b'SQLDataSources',
    58: b'SQLDescribeParam',
    59: b'SQLExtendedFetch',
    60: b'SQLForeignKeys',
    61: b'SQLMoreResults',
    62: b'SQLNativeSql',
    63: b'SQLNumParams',
    64: b'SQLParamOptions',
    65: b'SQLPrimaryKeys',
    66: b'SQLProcedureColumns',
    67: b'SQLProcedures',
    68: b'SQLSetPos',
    69: b'SQLSetScrollOptions',
    70: b'SQLTablePrivileges',
    71: b'SQLDrivers',
    72: b'SQLBindParameter',
    73: b'SQLSetDescField',
    74: b'SQLSetDescRec',
    75: b'SQLSetEnvAttr',
    76: b'SQLSetStmtAttr',
    77: b'SQLAllocHandleStd',
    78: b'SQLBulkOperations',
    79: b'CloseODBCPerfData',
    80: b'CollectODBCPerfData',
    81: b'CursorLibLockDbc',
    82: b'CursorLibLockDesc',
    83: b'CursorLibLockStmt',
    84: b'ODBCGetTryWaitValue',
    85: b'CursorLibTransact',
    86: b'ODBCSetTryWaitValue',
    87: b'DllBidEntryPoint',
    88: b'GetODBCSharedData',
    89: b'LockHandle',
    90: b'ODBCInternalConnectW',
    91: b'OpenODBCPerfData',
    92: b'PostComponentError',
    93: b'PostODBCComponentError',
    94: b'PostODBCError',
    95: b'SQLCancelHandle',
    96: b'SQLCompleteAsync',
    97: b'SearchStatusCode',
    98: b'VFreeErrors',
    99: b'VRetrieveDriverErrorsRowCol',
    100: b'ValidateErrorQueue',
    101: b'g_hHeapMalloc',
    106: b'SQLColAttributesW',
    107: b'SQLConnectW',
    108: b'SQLDescribeColW',
    110: b'SQLErrorW',
    111: b'SQLExecDirectW',
    117: b'SQLGetCursorNameW',
    119: b'SQLPrepareW',
    121: b'SQLSetCursorNameW',
    127: b'SQLColAttributeW',
    132: b'SQLGetConnectAttrW',
    133: b'SQLGetDescFieldW',
    134: b'SQLGetDescRecW',
    135: b'SQLGetDiagFieldW',
    136: b'SQLGetDiagRecW',
    138: b'SQLGetStmtAttrW',
    139: b'SQLSetConnectAttrW',
    140: b'SQLColumnsW',
    141: b'SQLDriverConnectW',
    142: b'SQLGetConnectOptionW',
    145: b'SQLGetInfoW',
    147: b'SQLGetTypeInfoW',
    150: b'SQLSetConnectOptionW',
    152: b'SQLSpecialColumnsW',
    153: b'SQLStatisticsW',
    154: b'SQLTablesW',
    155: b'SQLBrowseConnectW',
    156: b'SQLColumnPrivilegesW',
    157: b'SQLDataSourcesW',
    160: b'SQLForeignKeysW',
    162: b'SQLNativeSqlW',
    165: b'SQLPrimaryKeysW',
    166: b'SQLProcedureColumnsW',
    167: b'SQLProceduresW',
    170: b'SQLTablePrivilegesW',
    171: b'SQLDriversW',
    173: b'SQLSetDescFieldW',
    176: b'SQLSetStmtAttrW',
    206: b'SQLColAttributesA',
    207: b'SQLConnectA',
    208: b'SQLDescribeColA',
    210: b'SQLErrorA',
    211: b'SQLExecDirectA',
    217: b'SQLGetCursorNameA',
    219: b'SQLPrepareA',
    221: b'SQLSetCursorNameA',
    227: b'SQLColAttributeA',
    232: b'SQLGetConnectAttrA',
    233: b'SQLGetDescFieldA',
    234: b'SQLGetDescRecA',
    235: b'SQLGetDiagFieldA',
    236: b'SQLGetDiagRecA',
    238: b'SQLGetStmtAttrA',
    239: b'SQLSetConnectAttrA',
    240: b'SQLColumnsA',
    241: b'SQLDriverConnectA',
    242: b'SQLGetConnectOptionA',
    245: b'SQLGetInfoA',
    247: b'SQLGetTypeInfoA',
    250: b'SQLSetConnectOptionA',
    252: b'SQLSpecialColumnsA',
    253: b'SQLStatisticsA',
    254: b'SQLTablesA',
    255: b'SQLBrowseConnectA',
    256: b'SQLColumnPrivilegesA',
    257: b'SQLDataSourcesA',
    260: b'SQLForeignKeysA',
    262: b'SQLNativeSqlA',
    265: b'SQLPrimaryKeysA',
    266: b'SQLProcedureColumnsA',
    267: b'SQLProceduresA',
    270: b'SQLTablePrivilegesA',
    271: b'SQLDriversA',
    273: b'SQLSetDescFieldA',
    276: b'SQLSetStmtAttrA',
    301: b'ODBCQualifyFileDSNW',
}