#!/bin/bash

DIR="$(dirname -- "${BASH_SOURCE[0]}")"

protoc --python_out=pyi_out:"$DIR" "$DIR/doorman.proto"