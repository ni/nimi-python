
DEFAULT_TARGETS := module unit_tests update_generated_files run_unit_tests wheel sdist
export DEFAULT_TARGETS

ADDITIONAL_TARGETS := test flake8
export ADDITIONAL_TARGETS

GENERATED_DIR := $(ROOT_DIR)/generated
export GENERATED_DIR

COMMAND_LOG_BATCH := $(GENERATED_DIR)/command_history.bat
export COMMAND_LOG_BATCH
COMMAND_LOG_SH := $(GENERATED_DIR)/command_history.sh
export COMMAND_LOG_SH

define log_command
	$1
	@echo '$1' >> $(COMMAND_LOG_BATCH)
	@echo '$1' >> $(COMMAND_LOG_SH)
endef

ifeq (,$(PRINT))
_hide_cmds := @
endif

all: $(DRIVERS)

define per_driver_per_target
$1_$2: start
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 $2
endef

define per_driver_all
$1: start
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1 MKDIR
	$(_hide_cmds)make --no-print-directory -f src/$1/$1.mak DRIVER=$1
endef

$(foreach d,$(ALL_DRIVERS),$(eval $(call per_driver_all,$(d))))
$(foreach d,$(ALL_DRIVERS),\
   $(foreach t,$(DEFAULT_TARGETS) $(ADDITIONAL_TARGETS),\
      $(eval $(call per_driver_per_target,$(d),$(t)))))

define per_target
$1:
	$(foreach d,$(DRIVERS),make --no-print-directory -f src/$(d)/$(d).mak DRIVER=$(d) $1 &&)  echo
endef

# We add test when we create the $(DEFAULT_TARGETS). This is because it shouldn't be
# run when all is used, but we want it to work
$(foreach t,$(DEFAULT_TARGETS) $(ADDITIONAL_TARGETS),$(eval $(call per_target,$(t))))

SUPPRESS_ERROR_OUTPUT := 2> /dev/null
clean: start
	@echo 'Cleaning...'
	-@rm -Rf $(BIN_DIR) $(SUPPRESS_ERROR_OUTPUT)
	-@find $(ROOT_DIR) -path '*/__pycache__/*' -exec rm {} \; $(SUPPRESS_ERROR_OUTPUT)
	-@find $(ROOT_DIR) -name __pycache__ -exec rmdir {} \; $(SUPPRESS_ERROR_OUTPUT)
	-@find $(ROOT_DIR) -name '*.pyc' -exec rm {} \; $(SUPPRESS_ERROR_OUTPUT)
	-@rm $(foreach d,$(DRIVERS), $(ROOT_DIR)/docs/$(d)/*.rst) $(SUPPRESS_ERROR_OUTPUT)

start:
	-@echo "rem This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script." > $(COMMAND_LOG_BATCH)
	-@echo "# This is the list of commands that make invoked in order to build nimi-python. If you want to reproduce the build but don't have GNU Make setup in your system, you can invoke this script." > $(COMMAND_LOG_SH)


# From https://stackoverflow.com/questions/14760124/how-to-split-in-gnu-makefile-list-of-files-into-separate-lines
DRIVER_ALL_TARGETS_HELP := echo Drivers: $(addprefix  && echo - ,$(ALL_DRIVERS))
TARGETS_HELP := echo Targets: $(addprefix  && echo - ,$(DEFAULT_TARGETS) $(ADDITIONAL_TARGETS))
PER_DRIVER_PER_TARGET := \
   $(foreach d,$(ALL_DRIVERS),\
      $(foreach t,$(DEFAULT_TARGETS) $(ADDITIONAL_TARGETS),\
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


# Minimal makefile for Sphinx documentation
#
PYTHON_CMD ?= python3

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = $(PYTHON_CMD) -msphinx
SPHINXPROJ    = NIModularInstrumentsPythonAPI
SOURCEDIR     = $(ROOT_DIR)/docs
BUILDDIR      = $(BIN_DIR)/docs

html:
	$(_hide_cmds)$(call log_command,$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS))

.PHONY: help Makefile


