CC      := gcc
CFLAGS  := -std=c11 -Wall -Wextra -O2 -Iinclude
LDFLAGS :=

SRC     := $(wildcard src/*.c)
OBJ     := $(SRC:.c=.o)
TARGET  := mytool

.PHONY: all clean test

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	rm -f $(OBJ) $(TARGET)

test:
	@echo "Add your tests here (or integrate a framework like Unity / Check)"
	@./$(TARGET) --help || true