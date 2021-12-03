#!/bin/python3
import sys;
BLUE=('\033[38;5;50m');
used_libs = ["Marshal", "ArgParse", "Sys", "Re", "Time", "OS\n" ]
for demo in used_libs:
	sys.stdout.write(f" {BLUE}{demo} ")

