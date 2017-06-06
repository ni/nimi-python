

DRIVERS := NI-DMM
TEMPLATE_FOLDER := src/codegen/templates
TEMPLATE_FILES := \
             attributes.py.mako \
             enums.py.mako \
             library.py.mako \
             session.py.mako

GENERATOR_SCRIPT := src/codegen/generateTemplate.py
GENERATOR_COMMAND := python3 $(GENERATOR_SCRIPT)

OUTPUT_DIR := bin

define driver_build
METADATA_FILES_$1 := $(wildcard src/$1/metadata/*.py)

MKDIR_$1:
	mkdir --parents $(OUTPUT_DIR)/$1
endef

define file_build
TARGETS += $(OUTPUT_DIR)/$1/$(subst .mako,,$2)

$(OUTPUT_DIR)/$1/$(subst .mako,,$2): $(GENERATOR_SCRIPT) $(METADATA_FILES_$1) MKDIR_$1
	$(GENERATOR_COMMAND) \
      --template $(TEMPLATE_FOLDER)/$2 \
      --driver $1 \
      --dest-dir $(OUTPUT_DIR)/$1 \

endef

all: files

$(foreach d, $(DRIVERS), \
   $(eval $(call driver_build,$(d))))

$(foreach d, $(DRIVERS), \
   $(foreach t, $(TEMPLATE_FILES), \
      $(eval $(call file_build,$(d),$(t)))))

files: $(TARGETS)

print:
	@echo DRIVERS = $(DRIVERS)
	@echo TEMPLATE_FILES = $(TEMPLATE_FILES)
	@echo METADATA_FILES_nidmm = $(METADATA_FILES_nidmm)
	@echo TARGETS = $(TARGETS)
	@echo test = $(test)

clean:
	rm -Rf bin

