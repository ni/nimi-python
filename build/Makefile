
POSSIBLE_TARGETS := module unit_tests run_unit_tests wheel sdist
export POSSIBLE_TARGETS

ifeq (,$(PRINT))
_hide_cmds := @
endif

all: $(DRIVERS)

define per_driver_per_target
$1_$2:
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 $2
endef

define per_driver_all
$1:
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1
endef

$(foreach d,$(ALL_DRIVERS),$(eval $(call per_driver_all,$(d))))
$(foreach d,$(ALL_DRIVERS),\
   $(foreach t,$(POSSIBLE_TARGETS) test,\
      $(eval $(call per_driver_per_target,$(d),$(t)))))

define per_target
$1:
	$(foreach d,$(DRIVERS),make --no-print-directory -f src/$(d)/$(d).mak DRIVER=$(d) $1 &&)  echo
endef

# We add test when we create the $(POSSIBLE_TARGETS). This is because it shouldn't be
# run when all is used, but we want it to work
$(foreach t,$(POSSIBLE_TARGETS) test,$(eval $(call per_target,$(t))))

clean:
	@echo 'Cleaning...'
	-@rm -Rf $(BIN_DIR)
	-@find $(ROOT_DIR) -path '*/__pycache__/*' -exec rm {} \;
	-@find $(ROOT_DIR) -name __pycache__ -exec rmdir {} \;
	-@find $(ROOT_DIR) -name '*.pyc' -exec rm {} \;
	-@rm command_history.txt

# From https://stackoverflow.com/questions/14760124/how-to-split-in-gnu-makefile-list-of-files-into-separate-lines
DRIVER_ALL_TARGETS_HELP := echo Drivers: $(addprefix  && echo - ,$(ALL_DRIVERS))
TARGETS_HELP := echo Targets: $(addprefix  && echo - ,$(POSSIBLE_TARGETS) test)
PER_DRIVER_PER_TARGET := \
   $(foreach d,$(ALL_DRIVERS),\
      $(foreach t,$(POSSIBLE_TARGETS) test,\
         $(d)_$(t)))
DRIVER_TARGETS_HELP := echo Per driver, per target: $(addprefix  && echo - ,$(PER_DRIVER_PER_TARGET))
help:
	@echo 'Supported targets:'
	@echo '* help'
	@echo '* clean'
	@echo '* print-<VARIABLE> (only top level variables)'
	@echo '* printvar VAR=<VARIABLE> (per driver print variable)'
	@echo ''
	@echo 'Any/multiple target(s) listed below:'
	@$(DRIVER_ALL_TARGETS_HELP)
	@echo ''
	@$(TARGETS_HELP)
	@echo ''
	@$(DRIVER_TARGETS_HELP)
	@echo ''

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $* is $(flavor $*) variable set to [$($*)]) @true

# Per driver variable printing
per_driver_variable_print = make --no-print-directory -f src/$1/$1.mak DRIVER=$1 print-$2
.PHONY:
printvar:
	$(_hide_cmds)$(foreach d,$(DRIVERS),$(call per_driver_variable_print,$(d),$(VAR)) && ) echo


