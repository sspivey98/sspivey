#!/bin/bash

set -e

socat tcp-listen:1996,reuseaddr,fork SYSTEM:"/app/pokemon"