#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <cstdlib>

// Function to check if a string contains only numeric characters
bool is_numeric(const std::string &str) {
    return std::all_of(str.begin(), str.end(), ::isdigit);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " [args...]" << std::endl;
        return 1;
    }

    // Create a vector to hold command-line arguments
    std::vector<std::string> args;
    args.reserve(argc - 1);

    // Populate the vector with arguments
    for (int i = 1; i < argc; ++i) {
        args.emplace_back(argv[i]);
    }

    // Define a custom comparator for sorting
    auto compare = [](const std::string &a, const std::string &b) {
        bool a_is_num = is_numeric(a);
        bool b_is_num = is_numeric(b);

        if (a_is_num && b_is_num) {
            // If both are numeric, compare as integers
            return std::stoi(a) < std::stoi(b);
        } else if (!a_is_num && !b_is_num) {
            // If both are non-numeric, compare lexicographically
            return a < b;
        } else {
            // If one is numeric and the other is not, numeric strings come first
            return a_is_num;
        }
    };

    // Sort the vector using the custom comparator
    std::sort(args.begin(), args.end(), compare);

    // Output the sorted results
    std::cout << "Sorted results:" << std::endl;
    for (const auto &arg : args) {
        std::cout << arg << std::endl;
    }

    return 0; // Indicate successful completion
}

