CC=mpicc
CFLAGS=-std=gnu99 -Wall

.PHONY: clean

ring.x: ring.c
	$(CC) $(CFLAGS) $< -o $@

test: test.c
	$(CC) $(CFLAGS) $< -o $@	

clean:
	rm -f ring.x ring-*.o*

