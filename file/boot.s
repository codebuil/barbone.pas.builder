global _starts
extern mains
global FPC_LIB_EXIT
global PC_LIB_EXIT
global fpc_libinitializeunits
global THREADVARLIST_$SYSTEM$indirect
global INIT$_$SYSTEM
extern P$KERNEL_$$_MAINS
_starts:
	
	call P$KERNEL_$$_MAINS
haltss:
    jmp haltss
    INIT$_$SYSTEM:
THREADVARLIST_$SYSTEM$indirect:
FPC_LIB_EXIT:
PC_LIB_EXIT:
fpc_libinitializeunits:
ret
MODULEALIGN       equ     1<<0
MEMINFO           equ     1<<1
FLAGS             equ     MODULEALIGN | MEMINFO
MAGIC             equ     0x1BADB002
CHECKSUM          equ     -(MAGIC + FLAGS)
align 4
dd MAGIC
dd FLAGS
dd CHECKSUM
HREADVARLIST_x86indirect:
