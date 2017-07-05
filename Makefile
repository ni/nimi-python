
DRIVERS := nidmm nimodinst

ROOT_DIR := $(abspath .)
BUILD_DIR := $(ROOT_DIR)/build
export ROOT_DIR
export BUILD_DIR

all:
	make --no-print-directory -f src/nidmm/nidmm.mak DRIVER=nidmm all
#	make --no-print-directory -f build/build.mak DRIVER=nimodinst all

clean:
	rm -Rf bin
#	make -f build/build.mak DRIVER=nidmm clean
#	make -f build/build.mak DRIVER=nimodinst clean

