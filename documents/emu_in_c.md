# Language emulatuons in C

## Python-like list comprehension in C:

```c
#include <stdio.h>

int main() {
    int squares[10];
    for (int i = 0; i < 10; i++) {
        squares[i] = i * i;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", squares[i]);
    }
    return 0;
}
```

## Ruby-like string interpolation:

```c
#include <stdio.h>

int main() {
    char name[] = "John";
    int age = 30;
    char message[100];
    sprintf(message, "My name is %s and I'm %d years old.", name, age);
    printf("%s", message);
    return 0;
}
```

## PHP-like dynamic typing:

```c
#include <stdio.h>

int main() {
    void *my_var;
    my_var = "Hello, world!";
    printf("%s\n", (char *)my_var);
    my_var = 42;
    printf("%d\n", *(int *)my_var);
    return 0;
}
```

# Swift-like optionals:

```c
#include <stdio.h>

int main() {
    int *my_var = NULL;
    if (my_var != NULL) {
        printf("%d\n", *my_var);
    } else {
        printf("my_var is null\n");
    }
    int my_value = 42;
    my_var = &my_value;
    if (my_var != NULL) {
        printf("%d\n", *my_var);
    } else {
        printf("my_var is null\n");
    }
    return 0;
}
```

## Kotlin-like null safety:

```c
#include <stdio.h>

int main() {
    int *my_var = NULL;
    if (my_var != NULL) {
        printf("%d\n", *my_var);
    } else {
        printf("my_var is null\n");
    }
    int my_value = 42;
    my_var = &my_value;
    if (my_var != NULL) {
        printf("%d\n", *my_var);
    } else {
        printf("my_var is null\n");
    }
    return 0;
}
```

## Go-like channels:

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h

#define BUFFER_SIZE 10

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int count = 0;

pthread_mutex_t mutex;
pthread_cond_t full;
pthread_cond_t empty;

void *producer(void *arg) {
    for (int i = 0; i < 100; i++) {
        pthread_mutex_lock(&mutex);
        while (count == BUFFER_SIZE) {
            pthread_cond_wait(&full, &mutex);
        }
        buffer[in] = i;
        in = (in + 1) % BUFFER_SIZE;
        count++;
        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void *consumer(void *arg) {
    for (int i = 0; i < 100; i++) {
        pthread_mutex_lock(&mutex);
        while (count == 0) {
            pthread_cond_wait(&empty, &mutex);
        }
        int value = buffer[out];
        out = (out + 1) % BUFFER_SIZE;
        count--;
        pthread_cond_signal(&full);
        pthread_mutex_unlock(&mutex);
        printf("%d\n", value);
    }
    return NULL;
}

int main() {
    pthread_t producer_thread, consumer_thread;
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&full, NULL);
    pthread_cond_init(&empty, NULL);
    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);
    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&full);
    pthread_cond_destroy(&empty);
    return 0;
}
```

## Rust-like ownership and borrowing:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
} Vec;

void vec_init(Vec *vec, int size) {
    vec->data = malloc(size * sizeof(int));
    vec->size = size;
}

void vec_free(Vec *vec) {
    free(vec->data);
    vec->size = 0;
}

void vec_push(Vec *vec, int value) {
    vec->data[vec->size++] = value;
}

int vec_pop(Vec *vec) {
    return vec->data[--vec->size];
}

int main() {
    Vec vec;
    vec_init(&vec, 10);
    vec_push(&vec, 1);
    vec_push(&vec, 2);
    vec_push(&vec, 3);
    printf("%d\n", vec_pop(&vec));
    printf("%d\n", vec_pop(&vec));
    vec_free(&vec);
    return 0;
}

```

## Haskell-like lazy evaluation:

```c

#include <stdio.h>
#include <stdlib.h>

typedef struct thunk {
    int (*eval)(struct thunk *);
    int value;
} Thunk;

int force(Thunk *thunk) {
    if (thunk->eval) {
        thunk->value = thunk->eval(thunk);
        thunk->eval = NULL;
    }
    return thunk->value;
}

#define lazy(thunk_expr) ({             \
    Thunk *thunk = malloc(sizeof(Thunk)); \
    thunk->eval = (int (*)(struct thunk *))(&thunk_expr); \
    thunk;                               \
})

int fibonacci(int n) {
    if (n < 2) {
        return n;
    }
    Thunk *a = lazy(fibonacci(n - 1));
    Thunk *b = lazy(fibonacci(n - 2));
    return force(a) + force(b);
}

int main() {
    for (int i = 0; i < 10; i++) {
        printf("%d\n", fibonacci(i));
    }
    return 0;
}

```
 ## Idris-like dependent types:

 ```c
 #include <stdio.h>
#include <stdlib.h>

#define Nat int
#define Zero 0
#define Succ(n) ((n) + 1)

#define Vect(t, n) t *
#define Nil(t) NULL
#define Cons(x, xs) ((x), (xs))
#define length(xs) _Generic((xs), Vect(int, Zero): Zero, Vect(int, Succ(Zero)): Succ(length(tail(xs))))

#define head(xs) ((xs)[0])
#define tail(xs) ((xs) + 1)

int main() {
    Vect(int, Succ(Succ(Succ(Zero)))) xs = Cons(1, Cons(2, Cons(3, Nil(int))));
    printf("%d\n", length(xs));
    printf("%d\n", head(xs));
    printf("%d\n", head(tail(xs)));
    printf("%d\n", head(tail(tail(xs))));
    return 0;
}

```
## Lisp implementation in C:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TOKENS 100
#define MAX_TOKEN_LEN 100

typedef struct {
    char *tokens[MAX_TOKENS];
    int count;
} TokenList;

void tokenize(char *input, TokenList *tokens) {
    char *token = strtok(input, " \n\t");
    while (token != NULL && tokens->count < MAX_TOKENS) {
        tokens->tokens[tokens->count++] = token;
        token = strtok(NULL, " \n\t");
    }
}

int eval(TokenList *tokens) {
    if (tokens->count == 0) {
        return 0;
    }
    char *token = tokens->tokens[0];
    if (strcmp(token, "exit") == 0) {
        return 1;
    }
    if (strcmp(token, "+") == 0) {
        int sum = 0;
        for (int i = 1; i < tokens->count; i++) {
            sum += atoi(tokens->tokens[i]);
        }
        printf("%d\n", sum);
    } else if (strcmp(token, "-") == 0) {
        int diff = atoi(tokens->tokens[1]);
        for (int i = 2; i < tokens->count; i++) {
            diff -= atoi(tokens->tokens[i]);
        }
        printf("%d\n", diff);
    } else {
        printf("Unknown command: %s\n", token);
    }
    return 0;
}

int main() {
    TokenList tokens;
    char input[MAX_TOKEN_LEN * MAX_TOKENS];
    while (1) {
        printf("> ");
        fgets(input, sizeof(input), stdin);
        tokens.count = 0;
        tokenize(input, &tokens);
        if (eval(&tokens)) {
            break;
        }
    }
    return 0;
}

```
