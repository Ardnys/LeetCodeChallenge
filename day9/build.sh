#!/bin/sh

set -xe

CFLAGS="-Wall -Wextra -std=c11"

gcc $CFLAGS -o compress strcompress.c

