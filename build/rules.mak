
include $(BUILD_HELPER_DIR)/tools.mak

MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_COPY)) \
                $(addprefix $(MODULE_DIR)/,$(CUSTOM_TYPES_TO_COPY)) \
                $(DOCS_DIR)/conf.py \


RST_FILES := \
                $(addprefix $(DRIVER_DOCS_DIR)/,$(RST_FILES_TO_GENERATE)) \

MKDIR: $(MKDIRECTORIES)

CURRENT_DIR := $(shell pwd)

define mkdir_rule
$1:
	$(call trace_to_console, "Making dir",$1)
	$(_hide_cmds)$(call log_command,mkdir -p $1)
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

$(MODULE_DIR)/session.py: $(wildcard $(TEMPLATE_DIR)/session.py/*.mako) $(wildcard $(DRIVER_DIR)/templates/session.py/*.mako)
$(DRIVER_DOCS_DIR)/functions.rst: $(wildcard $(TEMPLATE_DIR)/functions.rst/*.mako) $(wildcard $(DRIVER_DIR)/templates/functions.rst/*.mako)

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

$(DOCS_DIR)/conf.py: $(TEMPLATE_DIR)/conf.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(DOCS_DIR), $(METADATA_DIR))

$(DRIVER_DOCS_DIR)/%.rst: %.rst.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(DRIVER_DOCS_DIR)/%.inc: %.inc.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/unit_tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/unit_tests/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

clean:

.PHONY: module unit_tests sdist wheel
$(UNIT_TEST_FILES): $(MODULE_FILES)
module: $(MODULE_FILES)

$(UNIT_TEST_FILES): $(MODULE_FILES)

README := $(OUTPUT_DIR)/README.rst
ifneq (nifake,$(DRIVER))
  ROOT_README := $(ROOT_DIR)/README.rst
endif

$(OUTPUT_DIR)/setup.py: $(TEMPLATE_DIR)/setup.py.mako $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

sdist: $(SDIST_BUILD_DONE) $(UNIT_TEST_FILES)

$(SDIST_BUILD_DONE): $(OUTPUT_DIR)/setup.py $(README) $(ROOT_README) $(MODULE_FILES)
	$(call trace_to_console, "Creating sdist",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call make_with_tracking_file,$@,cd $(OUTPUT_DIR) && $(PYTHON_CMD) setup.py sdist $(LOG_OUTPUT) $(LOG_DIR)/sdist.log)

wheel: $(WHEEL_BUILD_DONE) $(UNIT_TEST_FILES)

$(WHEEL_BUILD_DONE): $(OUTPUT_DIR)/setup.py $(README) $(ROOT_README) $(MODULE_FILES)
	$(call trace_to_console, "Creating wheel",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call make_with_tracking_file,$@,cd $(OUTPUT_DIR) && $(PYTHON_CMD) setup.py bdist_wheel --universal $(LOG_OUTPUT) $(LOG_DIR)/wheel.log)

# If we are building nifake, we just need a placeholder file for inclusion into the wheel that will never be used. We can't build the actual readme since not all the files are created
ifeq (nifake,$(DRIVER))
$(README):
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $(ROOT_DIR)/LICENSE $@)

else
# We piece together the readme files instead of relying on the rst include directive because we need these files to be standalone and not require any additional files that are in specific locations.
$(README): $(MODULE_FILES) $(RST_FILES) $(wildcard $(STATIC_DOCS_DIR)/*)
	$(call trace_to_console, "Creating",$@)
	$(_hide_cmds)$(call log_command,cat $(STATIC_DOCS_DIR)/status_project.inc $(STATIC_DOCS_DIR)/about.inc $(DRIVER_DOCS_DIR)/status.inc $(DRIVER_DOCS_DIR)/installation.inc $(STATIC_DOCS_DIR)/contributing.inc $(STATIC_DOCS_DIR)/$(DRIVER)_usage.inc $(STATIC_DOCS_DIR)/support.inc $(STATIC_DOCS_DIR)/documentation.inc $(STATIC_DOCS_DIR)/license.inc > $@)

$(ROOT_README): $(MODULE_FILES) $(RST_FILES) $(wildcard $(STATIC_DOCS_DIR)/*) $(wildcard $(DOCS_DIR)/*/status.inc)
	$(call trace_to_console, "Creating",$@)
	$(_hide_cmds)$(call log_command,cat $(STATIC_DOCS_DIR)/status_project.inc $(STATIC_DOCS_DIR)/about.inc $(DOCS_DIR)/*/status.inc $(STATIC_DOCS_DIR)/installation.inc $(STATIC_DOCS_DIR)/contributing.inc $(STATIC_DOCS_DIR)/nidmm_usage.inc $(STATIC_DOCS_DIR)/support.inc $(STATIC_DOCS_DIR)/documentation.inc $(STATIC_DOCS_DIR)/license.inc > $@)

endif

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true

update_generated_files: $(GENERATED_FILES_COPY_DONE)

$(GENERATED_FILES_COPY_DONE): $(MODULE_FILES) $(OUTPUT_DIR)/setup.py $(UNIT_TEST_FILES) $(RST_FILES)
	$(call trace_to_console, "Updating",$(DRIVER_GENERATED_DIR)/)
	$(_hide_cmds)$(call make_with_tracking_file, $@, \
      rm -Rf $(DRIVER_GENERATED_DIR)/* && \
      cp -Rf $(MODULE_DIR)/* $(DRIVER_GENERATED_DIR) && \
      cp -Rf $(OUTPUT_DIR)/setup.py $(DRIVER_GENERATED_DIR) \
   )


