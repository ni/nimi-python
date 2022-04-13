
include $(BUILD_HELPER_DIR)/tools.mak

README := $(OUTPUT_DIR)/README.rst
SETUP := $(OUTPUT_DIR)/setup.py
TOX_INI := $(OUTPUT_DIR)/tox-system_tests.ini

MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_COPY)) \
                $(addprefix $(MODULE_DIR)/,$(CUSTOM_TYPES_TO_COPY)) \
                $(README) \
                $(SETUP) \
                $(TOX_INI) \

RST_FILES := \
                $(addprefix $(DRIVER_DOCS_DIR)/,$(RST_FILES_TO_GENERATE)) \

EXAMPLE_FILES := $(if $(wildcard src/$(DRIVER)/examples/*),$(shell find src/$(DRIVER)/examples/* -type f -print),)

# If there are any examples, we will need to build the examples zip file for this driver
ifneq (,$(EXAMPLE_FILES))

EXAMPLES_DIR := $(GENERATED_DIR)/examples
MKDIRECTORIES += $(EXAMPLES_DIR)
DRIVER_EXAMPLES_ZIP_FILE := $(EXAMPLES_DIR)/$(DRIVER)_examples.zip
MODULE_FILES += $(DRIVER_EXAMPLES_ZIP_FILE)

endif # ifneq (,$(EXAMPLE_FILES))

MKDIR: $(MKDIRECTORIES)

CURRENT_DIR := $(shell pwd)

define mkdir_rule
$1:
	$(call trace_to_console, "Making dir",$1)
	$(_hide_cmds)$(call log_command,mkdir -p $1)
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

# We set up some additional dependencies for specific files
# examples.rst needs to use find since there may be folders of files and it needs to be recursive. wildcard is not recursive
$(MODULE_DIR)/session.py: $(wildcard $(TEMPLATE_DIR)/session.py/*.mako) $(wildcard $(DRIVER_DIR)/templates/session.py/*.mako)
$(DRIVER_DOCS_DIR)/class.rst: $(wildcard $(TEMPLATE_DIR)/functions.rst/*.mako) $(wildcard $(DRIVER_DIR)/templates/functions.rst/*.mako)
$(DRIVER_DOCS_DIR)/examples.rst: $(EXAMPLE_FILES) $(MODULE_DIR)/VERSION

$(MODULE_DIR)/%.py: %.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/unit_tests/%.py: %.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%: %.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%.py: %.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)cp $< $@

$(MODULE_DIR)/%.py: $(DRIVER_DIR)/custom_types/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)cp $< $@

$(DRIVER_DOCS_DIR)/%.rst: %.rst.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_DOCS_DIR)/%.inc: %.inc.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_EXAMPLES_ZIP_FILE): $(EXAMPLE_FILES)
	$(call trace_to_console, "Zipping",$@)
	$(_hide_cmds)$(call log_command,cd src/$(DRIVER)/examples && zip -u -r -9 $@ * || ([ $$? -eq 12 ] && exit 0) || exit)

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/unit_tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/unit_tests/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

clean:

.PHONY: module doc_files sdist wheel installers
module: $(MODULE_FILES) $(UNIT_TEST_FILES)
doc_files: $(RST_FILES)
installers: sdist wheel

$(UNIT_TEST_FILES): $(MODULE_FILES)

$(SETUP): $(TEMPLATE_DIR)/setup.py.mako $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(TOX_INI): $(TEMPLATE_DIR)/tox-system_tests.ini.mako $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

sdist: $(SDIST_BUILD_DONE)

$(SDIST_BUILD_DONE): # codegen should have already run or just use what is is git
	$(call trace_to_console, "Creating sdist",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command_no_tracking,cd $(OUTPUT_DIR) && $(PYTHON_CMD) setup.py sdist $(LOG_OUTPUT) $(LOG_DIR)/sdist.log)
	$(_hide_cmds)$(call log_command_no_tracking,touch $@)

wheel: $(WHEEL_BUILD_DONE)

$(WHEEL_BUILD_DONE): # codegen should have already run or just use what is is git
	$(call trace_to_console, "Creating wheel",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command_no_tracking,cd $(OUTPUT_DIR) && $(PYTHON_CMD) setup.py bdist_wheel $(LOG_OUTPUT) $(LOG_DIR)/wheel.log)
	$(_hide_cmds)$(call log_command_no_tracking,touch $@)

# If we are building nifake, we just need a placeholder file for inclusion into the wheel that will never be used. We can't build the actual readme since not all the files are created
ifeq (nifake,$(DRIVER))
$(README):
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $(ROOT_DIR)/LICENSE $@)

else
# We piece together the readme files instead of relying on the rst include directive because we need these files to be standalone and not require any additional files that are in specific locations.
$(README): $(RST_FILES) $(wildcard $(STATIC_DOCS_DIR)/*)
	$(call trace_to_console, "Creating",$@)
	$(_hide_cmds)$(call log_command,cat $(STATIC_DOCS_DIR)/status_project.inc $(STATIC_DOCS_DIR)/about.inc $(DRIVER_DOCS_DIR)/status.inc $(DRIVER_DOCS_DIR)/installation.inc $(STATIC_DOCS_DIR)/contributing.inc $(STATIC_DOCS_DIR)/$(DRIVER)_usage.inc $(STATIC_DOCS_DIR)/support.inc $(STATIC_DOCS_DIR)/documentation.inc $(STATIC_DOCS_DIR)/license.inc > $@)

endif

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true


