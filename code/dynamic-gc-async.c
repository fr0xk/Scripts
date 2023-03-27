#include <stdio.h>

#include <uv.h>   // for asynchronous programming

#include <gc.h>   // for garbage collection

// Callback function for the timer

void on_timer(uv_timer_t* handle) {

  // Demonstrate dynamic typing with void pointers

  void* variable = NULL;

  int i = 5;

  float f = 3.14;

  char c = 'a';

  variable = &i;

  printf("Value of i: %d\n", *(int*)variable);

  variable = &f;

  printf("Value of f: %f\n", *(float*)variable);

  variable = &c;

  printf("Value of c: %c\n", *(char*)variable);

}

int main() {

  // Demonstrate dynamic typing with void pointers

  void* variable = NULL;

  int i = 5;

  float f = 3.14;

  char c = 'a';

  variable = &i;

  printf("Value of i: %d\n", *(int*)variable);

  variable = &f;

  printf("Value of f: %f\n", *(float*)variable);

  variable = &c;

  printf("Value of c: %c\n", *(char*)variable);

  // Demonstrate garbage collection with the libgc library

  int* p = GC_MALLOC(sizeof(int));

  *p = 42;

  printf("Value of p: %d\n", *p);

  // Demonstrate asynchronous programming with the libuv library

  uv_timer_t timer;

  uv_timer_init(uv_default_loop(), &timer);

  uv_timer_start(&timer, on_timer, 5000, 0);  // start the timer to call on_timer() after 5 seconds

  uv_run(uv_default_loop(), UV_RUN_DEFAULT);

  return 0;

}

