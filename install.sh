#!/bin/bash

sudo chmod +x sus/executables/*

sudo mv sus/executables/* /usr/local/bin

sudo mv sus ~/.sus_src
cd ~/.doccli_src && sudo python3 -m venv .venv