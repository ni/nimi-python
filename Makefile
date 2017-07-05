
DRIVERS := nidmm nimodinst

ROOT_DIR := $(abspath .)
BUILD_DIR := $(ROOT_DIR)/build
export ROOT_DIR
export BUILD_DIR

POSSIBLE_TARGETS := module unit_tests run_unit_tests
TARGETS := $(MAKECMDGOALS)
ifeq (,$(TARGETS))
TARGETS := $(POSSIBLE_TARGETS)
endif
export TARGETS

all: $(DRIVERS)

define invoke_driver_make
make --no-print-directory -f src/$1/$1.mak DRIVER=$1 $2
endef

define per_driver_all
$1:
	make --no-print-directory -f src/$1/$1.mak DRIVER=$1
endef

$(foreach d,$(DRIVERS),$(eval $(call per_driver_all,$(d))))

clean:
	rm -Rf bin

