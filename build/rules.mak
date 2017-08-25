
MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(MODULE_FILES_TO_COPY))

RST_FILES := \
                $(addprefix $(DRIVER_DOCS_DIR)/,$(RST_FILES_TO_GENERATE)) \

MKDIR: $(MKDIRECTORIES)

CURRENT_DIR := $(shell pwd)

define log_command
	$1
	@echo '$1' >> $(COMMAND_LOG_BATCH)
	@echo '$1' >> $(COMMAND_LOG_SH)
endef


define mkdir_rule
$1:
	@echo "    Making dir: $(subst $(CURRENT_DIR)/,,$1)"
	$(_hide_cmds)$(call log_command,mkdir -p $1)
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

$(MODULE_DIR)/%.py: %.py.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	@echo "    Generating: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/tests/%.py: %.py.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	@echo "    Generating: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

$(MODULE_DIR)/%.py: %.py
	@echo "       Copying: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)cp $< $@

$(DRIVER_DOCS_DIR)/%.rst: %.rst.mako $(BUILD_HELPER_SCRIPT) $(METADATA_FILES)
	@echo "    Generating: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/tests/%.py
	@echo "       Copying: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,cp $< $@)

clean:

.PHONY: module unit_tests sdist wheel
$(UNIT_TEST_FILES): $(MODULE_FILES) $(RST_FILES)
module: $(MODULE_FILES)


$(UNIT_TEST_FILES): $(MODULE_FILES) $(RST_FILES)

unit_tests: $(UNIT_TEST_FILES)

$(LOG_DIR)/tests_passed: $(UNIT_TEST_FILES)
	@echo Running pytest: $(subst $(CURRENT_DIR)/,,$(OUTPUT_DIR))
	$(_hide_cmds)$(call log_command,touch $(LOG_DIR)/tests_passed)
	$(_hide_cmds)$(call log_command,rm $(LOG_DIR)/tests_passed)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 -m pytest -s $(LOG_OUTPUT) $(LOG_DIR)/test_results.log)
	$(_hide_cmds)$(call log_command,touch $(LOG_DIR)/tests_passed)

$(OUTPUT_DIR)/README.rst: $(ROOT_DIR)/README.rst
	@echo "       Copying: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,cp $< $@)

$(OUTPUT_DIR)/setup.py: $(TEMPLATE_DIR)/setup.py.mako
	@echo "    Generating: $(subst $(CURRENT_DIR)/,,$@)"
	$(_hide_cmds)$(call log_command,$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR)))

sdist: $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/tests_passed
	@echo Creating sdist: $(subst $(CURRENT_DIR)/,,$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 setup.py sdist $(LOG_OUTPUT) $(LOG_DIR)/sdist.log)

wheel: $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/tests_passed
	@echo Creating wheel: $(subst $(CURRENT_DIR)/,,$(OUTPUT_DIR)/dist)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && python3 setup.py bdist_wheel --universal $(LOG_OUTPUT) $(LOG_DIR)/wheel.log)

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true

$(TOX_INI): $(ROOT_DIR)/tox.ini
	@echo Copying tox.ini to $(DRIVER) $@
	$(_hide_cmds)$(call log_command,cp $< $@)

test: $(TOX_INI)
	@echo Running tox tests for $(DRIVER)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && set DRIVER=$(DRIVER) && tox)

flake8: $(TOX_INI)
	@echo Running flake8 for $(DRIVER)
	$(_hide_cmds)$(call log_command,cd $(OUTPUT_DIR) && tox -e flake8)

update_generated_files: $(MODULE_FILES) $(OUTPUT_DIR)/setup.py
	@echo "      Updating: $(subst $(CURRENT_DIR)/,,$(GENERATED_DIR)/$(DRIVER)/)"
	$(_hide_cmds)$(call log_command,rm -Rf $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,mkdir -p $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,cp -Rf $(MODULE_DIR)/* $(GENERATED_DIR)/$(DRIVER))
	$(_hide_cmds)$(call log_command,cp -Rf $(OUTPUT_DIR)/setup.py $(GENERATED_DIR)/$(DRIVER))


