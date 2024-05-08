#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <cstdlib>

// Function to check if a string represents a numeric value
bool is_numeric(const std::string &str) {
    return !str.empty() && std::all_of(str.begin(), str.end(), ::isdigit);
}

int main(int argc, char *argv[]) {
    // Check for the correct number of arguments
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " [args...]" << std::endl;
        return EXIT_FAILURE;
    }

    // Reserve memory for the arguments vector
    std::vector<std::string> args;
    args.reserve(argc - 1);

    // Populate the vector with command-line arguments
    for (int i = 1; i < argc; ++i) {
        args.emplace_back(argv[i]);
    }

    // Define a lambda for sorting strings and numbers
    auto compare =  {
        bool a_is_num = is_numeric(a);
        bool b_is_num = is_numeric(b);
        if (a_is_num && b_is_num) {
            // Convert to long long to handle larger numbers
            return std::stoll(a) < std::stoll(b);
        } else if (!a_is_num && !b_is_num) {
            return a < b;
        }
        return a_is_num; // Numbers come first
    };

    // Sort the arguments based on the compare lambda
    std::sort(args.begin(), args.end(), compare);

    // Output the sorted results
    std::cout << "Sorted results:" << std::endl;
    for (const auto &arg : args) {
        std::cout << arg << std::endl;
    }

    return EXIT_SUCCESS; // Successful exit
}

