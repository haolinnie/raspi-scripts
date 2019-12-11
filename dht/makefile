TARGET=read_dht.out

CC=gcc
CFLAGS:=-I.
SRCS := $(wildcard *.c)
OBJS := $(%.0)
HDRS := $(wildcard *.h)

program_INCLUDE_DIRS :=
program_LIBRARY_DIRS :=
program_LIBRARIES := wiringPi wiringPiDev

CFLAGS += $(foreach includedir,$(program_INCLUDE_DIRS),-I $(includedir))
LDFLAGS += $(foreach librarydir,$(program_LIBRARY_DIRS),-L$(librarydir))
LDFLAGS += $(foreach library,$(program_LIBRARIES),-l$(library))

.PHONY: all
all: $(SRCS) $(HRDS)
	$(CC) -o $(TARGET) $(SRCS) $(LDFLAGS) $(CFLAGS) 

.PHONY: clean
clean:
	-rm -f *.o $(TARGET)

rebuild: clean all

#gcc -o example main.c -lwiringPi -lwiringPiDev
