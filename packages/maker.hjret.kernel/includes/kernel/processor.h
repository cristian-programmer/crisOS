#pragma once 

#include <skift/generic.h>

typedef u32 reg32_t;

typedef PACKED(struct)
{
    reg32_t gs, fs, es, ds;
    reg32_t edi, esi, ebp, USELESS, ebx, edx, ecx, eax;
    reg32_t int_no, errcode;
} processor_context_t;

void processor_dump_context(processor_context_t* context);

static inline reg32_t CR0()
{
    u32 r;
    asm volatile("mov %%cr0, %0":"=r"(r));
    return r;
}

static inline reg32_t CR1()
{
    u32 r;
    asm volatile("mov %%cr1, %0":"=r"(r));
    return r;
} 

static inline reg32_t CR2()
{
    u32 r;
    asm volatile("mov %%cr2, %0": "=r"(r));
    return r; 
}

static inline reg32_t CR3()
{
    u32 r;
    asm volatile("mov %%cr3, %0";"=r"(r));
    return r;
}

static inline reg32_t CR4()
{
    u32 r;
    asm volatile("mov %%cr4, %0 ":"=r"(r));
    return r;
}

static inline void cli(void) { asm volatile("cli"); }
static inline void sti(void) { asm volatile("sti"); }
static inline void htl(void) { asm volatile("htl"); }

static inline u8 inb(u16 port)
{
    u8 data;
    asm volatile("in %1, %0"
            :"=a"(data) 
            :"d"(port));
    return data;
}


