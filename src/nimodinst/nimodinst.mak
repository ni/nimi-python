

include $(BUILD_DIR)/defines.mak

FILES_TO_GENERATE := $(DEFAULT_FILES_TO_GENERATE)

FILES_TO_COPY := $(DEFAULT_FILES_TO_COPY)

include $(BUILD_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for ModInst
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako MKDIR
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

