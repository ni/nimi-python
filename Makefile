
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
	@echo 'Cleaning...'
	@rm -Rf bin
	@find -name __pycache__ -print -exec rm -Rf {} \;


# From https://stackoverflow.com/questions/14760124/how-to-split-in-gnu-makefile-list-of-files-into-separate-lines
DRIVER_TARGETS_HELP := echo Drivers: $(addprefix  && echo - ,$(ALL_DRIVERS))
help:
	@echo 'Supported commands:'
	@echo '* help'
	@echo '* clean'
	@echo '* print-<VARIABLE>'
	@echo ''
	@$(DRIVER_TARGETS_HELP)

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $* is $(flavor $*) variable set to [$($*)]) @true
