#pragma once

#include <skift/generic.h>
#include "kernel/protocol.h"

void mouse_setup();
void mouse_get_state(mouse_state_t *state);
void mouse_set_state(mouse_state_t *state);

