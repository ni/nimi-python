DRIVERS := nidmm
TEMPLATE_FOLDER := src/codegen/templates
GENERATOR_SCRIPT := src/codegen/generateTemplate.py
GENERATOR_COMMAND := python3 $(GENERATOR_SCRIPT)

OUTPUT_DIR := bin

all: files

$(OUTPUT_DIR):
	mkdir --parents $(OUTPUT_DIR)


define driver_build
METADATA_FILES_$1 := $(wildcard src/$1/metadata/*.py)

include $(OUTPUT_DIR)/$1.mak

$(OUTPUT_DIR)/$1.mak: $(GENERATOR_SCRIPT) $(METADATA_FILES_$1) \
                      $(TEMPLATE_FOLDER)/build.mak.mako $(OUTPUT_DIR)
	@echo Generating $1.mak
	@$(GENERATOR_COMMAND) \
      --template $(TEMPLATE_FOLDER)/build.mak.mako \
      --driver $1 \
      --dest-dir $(OUTPUT_DIR) \
      --dest-file $1.mak \

endef

$(foreach d, $(DRIVERS), \
   $(eval $(call driver_build,$(d))))

files: $(TARGETS)

print:
	@echo DRIVERS = $(DRIVERS)
	@echo TEMPLATE_FILES = $(TEMPLATE_FILES)
	@echo METADATA_FILES_nidmm = $(METADATA_FILES_nidmm)
	@echo TARGETS = $(TARGETS)
	@echo test = $(test)

clean:
	rm -Rf bin

