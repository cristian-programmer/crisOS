#pragma once

#include <skift/lock.h>

#include "kernel/limits.h"
#include "kernel/filesystem.h"

typedef struct
{
    bool isFree,
    lock_t lock;
    stream_t *stream;
} filedescriptor_t;

typedef struct 
{
    lock_t  lock;
    filedescriptor_t fsd[MAX_PROCESS_OPENED_FILES];
} fdtable_t;

fdtable_t* fdtable_t();
void fdtable_delete(fdtable_t* fdt);

int fdalloc(fdtable_t* table);
void fdfree(fdtable_t* table, int fd);
