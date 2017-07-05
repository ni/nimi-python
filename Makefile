
ALL_DRIVERS := nidmm nimodinst
DRIVERS ?= $(ALL_DRIVERS)

ROOT_DIR := $(abspath .)
BUILD_DIR := $(ROOT_DIR)/build
export ROOT_DIR
export BUILD_DIR

POSSIBLE_TARGETS := module unit_tests run_unit_tests
export POSSIBLE_TARGETS

all: $(DRIVERS)

define per_driver_per_target
$1_$2:
	make --no-print-directory -f src/$1/$1.mak DRIVER=$1 $2
endef

define per_driver_all
$1:
	make --no-print-directory -f src/$1/$1.mak DRIVER=$1
endef

$(foreach d,$(ALL_DRIVERS),$(eval $(call per_driver_all,$(d))))
$(foreach d,$(ALL_DRIVERS),\
   $(foreach t,$(POSSIBLE_TARGETS),\
      $(eval $(call per_driver_per_target,$(d),$(t)))))

clean:
	@echo 'Cleaning...'
	@rm -Rf bin
	@find . -path '*/__pycache__/*' -delete
	@find . -name __pycache__ -delete


# From https://stackoverflow.com/questions/14760124/how-to-split-in-gnu-makefile-list-of-files-into-separate-lines
DRIVER_ALL_TARGETS_HELP := echo Drivers: $(addprefix  && echo - ,$(ALL_DRIVERS))
TARGETS_HELP := echo Targets \(not implemented yet\): $(addprefix  && echo - ,$(POSSIBLE_TARGETS))
PER_DRIVER_PER_TARGET := \
   $(foreach d,$(ALL_DRIVERS),\
      $(foreach t,$(POSSIBLE_TARGETS),\
         $(d)_$(t)))
DRIVER_TARGETS_HELP := echo Per driver, per target: $(addprefix  && echo - ,$(PER_DRIVER_PER_TARGET))
help:
	@echo 'Supported commands:'
	@echo '* help'
	@echo '* clean'
	@echo '* print-<VARIABLE> (only top level variables)'
	@echo ''
	@$(DRIVER_ALL_TARGETS_HELP)
	@echo ''
	@$(TARGETS_HELP)
	@echo ''
	@$(DRIVER_TARGETS_HELP)
	@echo ''

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $* is $(flavor $*) variable set to [$($*)]) @true


