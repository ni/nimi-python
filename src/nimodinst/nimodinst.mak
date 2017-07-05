

include $(BUILD_DIR)/defines.mak

FILES_TO_GENERATE := \
                     attributes.py \
                     enums.py \
                     library.py \
                     session.py \
                     errors.py \
                     ctypes_library.py \
                     tests/mock_helper.py \
                     __init__.py \

FILES_TO_COPY := \
                 ctypes_types.py \
                 python_types.py \

include $(BUILD_DIR)/rules.mak

$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako MKDIR
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

