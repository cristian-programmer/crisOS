ENTRY(_start)

SECTIONS
{
        . = 1M;
        __start = .;

        .text BLOCK(4K) : ALIGN(4K)
        {
                *(.multiboot)
                *(.text)
        }

        .rodata BLOCK(4K) : ALIGN(4K)
        {
                *(.rodata)
        }

        .data BLOCK(4K) : ALIGN(4K)
        {
            *(COMMON)
            *(.bss)
        }

        __end = .;
}

