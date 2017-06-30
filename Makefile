
DRIVERS := nidmm nimodinst

all:
	make -f build/build.mak DRIVER=nidmm all
	make -f build/build.mak DRIVER=nimodinst all

clean:
	rm -Rf bin
#	make -f build/build.mak DRIVER=nidmm clean
#	make -f build/build.mak DRIVER=nimodinst clean

