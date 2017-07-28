

include $(BUILD_HELPER_DIR)/defines.mak

# We want everything but enums.py
MODULE_FILES_TO_GENERATE := $(filter-out enums.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out enums.rst,$(DEFAULT_RST_FILES_TO_GENERATE))

include $(BUILD_HELPER_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for ModInst
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako
	@echo Creating $(DRIVER) $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

