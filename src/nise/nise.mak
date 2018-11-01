include $(BUILD_HELPER_DIR)/defines.mak
include $(BUILD_HELPER_DIR)/tools.mak

# We want everything but _attributes.py
MODULE_FILES_TO_GENERATE := $(filter-out _attributes.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

include $(BUILD_HELPER_DIR)/rules.mak


