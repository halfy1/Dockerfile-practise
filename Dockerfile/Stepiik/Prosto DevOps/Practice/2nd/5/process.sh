#!/bin/sh
echo "Running with $TEXT_TOOL on $1"

# Если TEXT_TOOL=grep, можно искать ERROR:
if [ -z "$TEXT_TOOL" ]; then
  echo "No TEXT_TOOL set, defaulting to grep"
  TEXT_TOOL="grep"
fi

$TEXT_TOOL "ERROR" $1