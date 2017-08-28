
MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_COPY))

RST_FILES := \
                $(addprefix $(DRIVER_DOCS_DIR)/,$(RST_FILES_TO_GENERATE)) \

MKDIR: $(MKDIRECTORIES)

CURRENT_DIR := $(shell pwd)

# Executes a command, then logs it to $(COMMAND_LOG_BATCH) and $(COMMAND_LOG_SH).
# $1 is the command.
# TODO(marcoskirsch): This is duplicated in Makefile.
define log_command
	$1
	@echo '$1' >> $(COMMAND_LOG_BATCH)
	@echo '$1' >> $(COMMAND_LOG_SH)
endef


# Traces to console, nicely formatted.
# $1 is the Action, for example: "Generating"
# $2 is a Path.
# Action will be padded on the left so colons align, for readability.
# Path will be turned from absolute to relative, for readability.
define trace_to_console
	@echo "$(shell printf '%15s' $1): $(subst $(CURRENT_DIR)/,,$2)"
endef

define mkdir_rule
$1:
	$(call trace_to_console, "Making dir",$1)
	$(_hide_cmds)$(call log_command,mkdir -p $1)
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

$(MODULE_DIR)/%.py: %.py.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/tests/%.py: %.py.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%.py: %.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)cp $< $@

$(DRIVER_DOCS_DIR)/%.rst: %.rst.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/tests/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

clean:

.PHONY: module unit_tests sdist wheel
$(UNIT_TEST_FILES): $(MODULE_FILES) $(RST_FILES)
module: $(MODULE_FILES)


$(UNIT_TEST_FILES): $(MODULE_FILES) $(RST_FILES)

unit_tests: $(UNIT_TEST_FILES)

$(LOG_DIR)/tests_passed: $(UNIT_TEST_FILES)
	$(call trace_to_console, "Running pytest",$@)
	$(_hide_cmds)$(call log_command,touch $(LOG_DIR)/tests_passed)
	$(_hide_cmds)$(call log_command,rm $(LOG_DIR)/tests_passed)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 -m pytest -s $(LOG_OUTPUT) $(LOG_DIR)/test_results.log)
	$(_hide_cmds)$(call log_command,touch $(LOG_DIR)/tests_passed)

$(OUTPUT_DIR)/README.rst: $(ROOT_DIR)/README.rst
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

$(OUTPUT_DIR)/setup.py: $(TEMPLATE_DIR)/setup.py.mako
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

sdist: $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/tests_passed
	$(call trace_to_console, "Creating sdist",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 setup.py sdist $(LOG_OUTPUT) $(LOG_DIR)/sdist.log)

wheel: $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/tests_passed
	$(call trace_to_console, "Creating wheel",$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 setup.py bdist_wheel --universal $(LOG_OUTPUT) $(LOG_DIR)/wheel.log)

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true

$(TOX_INI): $(ROOT_DIR)/tox.ini
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

test: $(TOX_INI)
	$(call trace_to_console, "Running tox",$(OUTPUT_DIR))
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && set DRIVER=$(DRIVER) && tox)

flake8: $(TOX_INI)
	$(call trace_to_console, "Running flake",$(OUTPUT_DIR))
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && tox -e flake8)

update_generated_files: $(MODULE_FILES) $(OUTPUT_DIR)/setup.py
	$(call trace_to_console, "Updating",$(GENERATED_DIR)/$(DRIVER)/)
	$(_hide_cmds)$(call log_command,rm -Rf $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,mkdir -p $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,cp -Rf $(MODULE_DIR)/* $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,cp -Rf $(OUTPUT_DIR)/setup.py $(GENERATED_DIR)/$(DRIVER))

ifneq (,$(wildcard $(DRIVER_DIR)/system_tests))
SYSTEM_TESTS_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/system_tests/*)
SYSTEM_TESTS_FILES := $(addprefix $(SYSTEM_TEST_DIR)/,$(notdir $(SYSTEM_TESTS_FILES_TO_COPY)))
endif
update_system_tests: $(SYSTEM_TESTS_FILES)

$(SYSTEM_TEST_DIR)/%.py: $(DRIVER_DIR)/system_tests/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)

ifneq (,$(wildcard $(DRIVER_DIR)/examples))
EXAMPLE_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/examples/*)
EXAMPLE_FILES := $(addprefix $(EXAMPLES_DIR)/,$(notdir $(EXAMPLE_FILES_TO_COPY)))
endif
update_examples: $(EXAMPLE_FILES)

$(EXAMPLES_DIR)/%.py: $(DRIVER_DIR)/examples/%.py
	$(call trace_to_console, "Copying",$@)
	$(_hide_cmds)$(call log_command,cp $< $@)


