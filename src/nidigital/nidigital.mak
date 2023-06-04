PROTO_FILE = $(METADATA_DIR)/nidigitalpattern.proto

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

CUSTOM_TYPES_TO_COPY += \
    history_ram_cycle_information.py \

include $(BUILD_HELPER_DIR)/rules.mak
