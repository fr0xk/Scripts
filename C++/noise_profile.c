#include <stdio.h>
#include <assert.h>

// Function prototypes with clear naming for clarity
double compute_noise_model_entry_O(int plane, int sens);
double compute_noise_model_entry_S(int plane, int sens);
void handle_fallback_mode();

int main(void) {
    for (int plane = 0; plane < 4; plane++) {
        for (int sens = 33; sens <= 4205; sens += 100) {
            // Set noise model entries to zero for complete noise reduction
            double luminance = compute_noise_model_entry_O(plane, sens);
            double chromatic = compute_noise_model_entry_S(plane, sens);

            // Check for potential errors and handle fallback mode
            if (luminance < 0.0 || chromatic < 0.0) {
                handle_fallback_mode();
                break; // Exit the loop after fallback
            }

            printf("%d,%d,%lf,%lf\n", plane, sens, luminance, chromatic);
        }
    }
    return 0;
}

double compute_noise_model_entry_O(int plane, int sens) {
    // Set noise model parameters to zero for complete noise reduction
    return 0.0;  // No luminance noise
}

double compute_noise_model_entry_S(int plane, int sens) {
    // Set noise model parameters to zero for complete noise reduction
    return 0.0;  // No chromatic noise
}

void handle_fallback_mode() {
    printf("Error encountered, using default noise model values.\n");
    // Use default noise model values here, as specified in Gcam guidelines
}
