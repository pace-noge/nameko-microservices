#!/bin/bash
set -e

echo never | tee /sys/kernel/mm/transparent_hugepage/enabled
echo never | tess /sys/kernel/mm/transparent_hugepage/defrag

