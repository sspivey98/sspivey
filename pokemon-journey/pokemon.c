//INTRO TO HEAP OVERFLOWS
// GOTTA Catch'em all

#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>

struct data {
  char name[64];
};

struct functionPointer {
  int (*functionPointer)();
};

void mewtwo()
{
  printf("What?! How'd you know I had a Mewtwo in the back?!?!\n");
  printf("Here is your flag!\n");
  FILE *file;
  char line[64];  // Buffer to store the first line
  char *filename = "flag.txt";

  // Open the file in read mode
  file = fopen(filename, "r");

  // Read the first line from the file
  fgets(line, sizeof(line), file);
  fclose(file);

  printf("flag: %s", line);
}

void pikachu()
{
  printf("Oh, you want a Pikachu? Here you go!\n");
}

int main(int argc, char **argv)
{
  if (argc != 2)
  {
    printf("Professor Oak's words echoed: There is a time and place for one argument, and that is now.\n");
    return 0;
  }

  struct data *d;
  struct functionPointer *f;

  d = malloc(sizeof(struct data));
  f = malloc(sizeof(struct functionPointer));
  f->functionPointer = pikachu;

  //printf("data is at %p, fp is at %p\n", d, f);
  printf("Hello Pokemon trainer! Welcome to the world of pokemon!\n");
  printf("Tell me, what pokemon would you like as your starter?\n\n");

  strcpy(d->name, argv[1]);
  
  f->functionPointer();
}