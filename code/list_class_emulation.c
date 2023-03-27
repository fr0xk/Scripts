#include <stdio.h>

#include <stdlib.h>

#include <string.h>

// Define a struct to represent a person

typedef struct {

    char name[50];

    int age;

    float height;

} Person;

// Define a function that initializes a person

void init_person(Person* person, const char* name, int age, float height) {

    strcpy(person->name, name);

    person->age = age;

    person->height = height;

}

// Define a function that prints out a person's details

void print_person(const Person* person) {

    printf("Name: %s\n", person->name);

    printf("Age: %d\n", person->age);

    printf("Height: %f\n", person->height);

}

// Define a struct to represent a list

typedef struct {

    int size;

    int capacity;

    int* data;

} List;

// Define a function that initializes a list

void init_list(List* list, int capacity) {

    list->size = 0;

    list->capacity = capacity;

    list->data = malloc(capacity * sizeof(int));

}

// Define a function that adds an element to the end of the list

void append_list(List* list, int value) {

    if (list->size == list->capacity) {

        // If the list is full, resize it by doubling its capacity

        list->capacity *= 2;

        list->data = realloc(list->data, list->capacity * sizeof(int));

    }

    // Add the new element to the end of the list

    list->data[list->size++] = value;

}

// Define a function that prints out a list

void print_list(const List* list) {

    printf("[");

    for (int i = 0; i < list->size; i++) {

        printf("%d", list->data[i]);

        if (i < list->size - 1) {

            printf(", ");

        }

    }

    printf("]\n");

}

int main() {

    // Create a new person

    Person* person = malloc(sizeof(Person));

    init_person(person, "John Doe", 30, 6.0);

    // Print the person's details

    print_person(person);

    // Free the person's memory

    free(person);

    // Create a new list with an initial capacity of 5

    List list;

    init_list(&list, 5);

    // Add some elements to the list

    append_list(&list, 1);

    append_list(&list, 2);

    append_list(&list, 3);

    append_list(&list, 4);

    append_list(&list, 5);

    // Print the list

    print_list(&list);

    // Free the list's memory

    free(list.data);

    return 0;

}

