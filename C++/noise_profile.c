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
    // Set noise model parameters A and C to zero for complete noise reduction
    static double noise_model_A[] = { 0.0, 0.0, 0.0, 0.0 };
    static double noise_model_C[] = { 0.0, 0.0, 0.0, 0.0 };

    double B = 0.0; // Set noise model parameter B to zero
    double D = 0.0; // Set noise model parameter D to zero

    double A = noise_model_A[plane];
    double C = noise_model_C[plane];

    double digital_gain = (sens / 262.0) < 1.0 ? 1.0 : (sens / 262.0);

    double o = A * sens * sens + B * digital_gain * digital_gain + C * sens + D;
    return o < 0.0 ? 0.0 : o;
}

double compute_noise_model_entry_S(int plane, int sens) {
    // Set noise model parameters B and D to zero for complete noise reduction
    static double noise_model_B[] = { 0.0, 0.0, 0.0, 0.0 };
    static double noise_model_D[] = { 0.0, 0.0, 0.0, 0.0 };

    double A = 0.0; // Set noise model parameter A to zero
    double C = 0.0; // Set noise model parameter C to zero

    double B = noise_model_B[plane];
    double D = noise_model_D[plane];

    double s = A * sens + B;
    return s < 0.0 ? 0.0 : s;
}

void handle_fallback_mode() {
    printf("Error encountered, using default noise model values.\n");
    // Use default noise model values here, as specified in Gcam guidelines
}
