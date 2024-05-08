#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// Debug macro to print internal state
#define DEBUG_PRINT(fmt, ...) \
    fprintf(stderr, "DEBUG: " fmt "\n", __VA_ARGS__)

// Structure to represent a dynamic array
typedef struct {
    int *array;      // Pointer to the array of integers
    size_t size;     // Current number of elements in the array
    size_t capacity; // Total capacity of the array
} DynamicArray;

// Function to create a new dynamic array with a specific capacity
DynamicArray *create_dynamic_array(size_t initial_capacity) {
    DynamicArray *dyn_array = (DynamicArray *)malloc(sizeof(DynamicArray));
    if (!dyn_array) {
        perror("Failed to allocate memory for DynamicArray");
        exit(EXIT_FAILURE);
    }

    dyn_array->array = (int *)malloc(initial_capacity * sizeof(int));
    if (!dyn_array->array) {
        perror("Failed to allocate memory for internal array");
        free(dyn_array);
        exit(EXIT_FAILURE);
    }

    dyn_array->size = 0;
    dyn_array->capacity = initial_capacity;
    DEBUG_PRINT("Created dynamic array with capacity %zu", initial_capacity);
    return dyn_array;
}

// Function to resize the array when it reaches capacity
void resize_array(DynamicArray *dyn_array, size_t new_capacity) {
    assert(dyn_array != NULL);
    assert(new_capacity >= dyn_array->size);

    int *new_array = (int *)realloc(dyn_array->array, new_capacity * sizeof(int));
    if (!new_array) {
        perror("Failed to resize array");
        exit(EXIT_FAILURE);
    }

    dyn_array->array = new_array;
    dyn_array->capacity = new_capacity;
    DEBUG_PRINT("Resized array to new capacity: %zu", new_capacity);
}

// Function to add an element to the end of the array
void push_back(DynamicArray *dyn_array, int value) {
    assert(dyn_array != NULL);

    if (dyn_array->size == dyn_array->capacity) {
        // Double the capacity
        resize_array(dyn_array, dyn_array->capacity * 2);
    }

    dyn_array->array[dyn_array->size] = value;
    dyn_array->size++;
    DEBUG_PRINT("Added element %d at index %zu", value, dyn_array->size - 1);
}

// Function to remove the last element of the array
void pop_back(DynamicArray *dyn_array) {
    assert(dyn_array != NULL);

    if (dyn_array->size == 0) {
        fprintf(stderr, "Error: Cannot pop from an empty array\n");
        exit(EXIT_FAILURE);
    }

    dyn_array->size--;
    DEBUG_PRINT("Popped element, new size is %zu", dyn_array->size);
}

// Function to get an element by index
int get(DynamicArray *dyn_array, size_t index) {
    assert(dyn_array != NULL);

    if (index >= dyn_array->size) {
        fprintf(stderr, "Error: Index %zu out of bounds\n", index);
        exit(EXIT_FAILURE);
    }

    return dyn_array->array[index];
}

// Function to set an element at a specific index
void set(DynamicArray *dyn_array, size_t index, int value) {
    assert(dyn_array != NULL);

    if (index >= dyn_array->size) {
        fprintf(stderr, "Error: Index %zu out of bounds\n", index);
        exit(EXIT_FAILURE);
    }

    dyn_array->array[index] = value;
    DEBUG_PRINT("Set element %d at index %zu", value, index);
}

// Function to insert an element at a specific index
void insert(DynamicArray *dyn_array, size_t index, int value) {
    assert(dyn_array != NULL);

    if (index > dyn_array->size) {
        fprintf(stderr, "Error: Index %zu out of bounds\n", index);
        exit(EXIT_FAILURE);
    }

    if (dyn_array->size == dyn_array->capacity) {
        resize_array(dyn_array, dyn_array->capacity * 2);
    }

    // Shift elements to the right
    for (size_t i = dyn_array->size; i > index; i--) {
        dyn_array->array[i] = dyn_array->array[i - 1];
    }

    dyn_array->array[index] = value;
    dyn_array->size++;
    DEBUG_PRINT("Inserted element %d at index %zu", value, index);
}

// Function to remove an element at a specific index
void erase(DynamicArray *dyn_array, size_t index) {
    assert(dyn_array != NULL);

    if (index >= dyn_array->size) {
        fprintf(stderr, "Error: Index %zu out of bounds\n", index);
        exit(EXIT_FAILURE);
    }

    // Shift elements to the left
    for (size_t i = index; i < dyn_array->size - 1; i++) {
        dyn_array->array[i] = dyn_array->array[i + 1];
    }

    dyn_array->size--;
    DEBUG_PRINT("Erased element at index %zu, new size %zu", index, dyn_array->size);
}

// Function to shrink the array capacity to fit the current size
void shrink_to_fit(DynamicArray *dyn_array) {
    assert(dyn_array != NULL);

    resize_array(dyn_array, dyn_array->size);
    DEBUG_PRINT("Shrunk array to fit current size %zu", dyn_array->size);
}

// Function to free the memory used by the dynamic array
void free_dynamic_array(DynamicArray *dyn_array) {
    assert(dyn_array != NULL);

    free(dyn_array->array);
    free(dyn_array);
    DEBUG_PRINT("Freed dynamic array memory");
}

// Example usage of the dynamic array
int main() {
    // Create a dynamic array with initial capacity 2
    DynamicArray *dyn_array = create_dynamic_array(2);

    // Add elements
    push_back(dyn_array, 10);
    push_back(dyn_array, 20);
    push_back(dyn_array, 30);

    // Insert and erase elements
    insert(dyn_array, 1, 15); // Insert 15 at index 1
    erase(dyn_array, 2);      // Erase element at index 2

    // Retrieve and set elements
    printf("Element at index 0: %d\n", get(dyn_array, 0)); // 10
    set(dyn_array, 0, 100);  // Change the first element to 100

    // Print all elements
    for (size_t i = 0; i < dyn_array->size; i++) {
        printf("Element at index %zu: %d\n", i, get(dyn_array, i));
    }

    // Pop last element and shrink to fit
    pop_back(dyn_array);
    shrink_to_fit(dyn_array);

    // Free the memory
    free_dynamic_array(dyn_array);

    return 0;
}
