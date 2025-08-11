#include <iostream>
#include <cmath>

// Check if a number is pentagonal
bool isPentagonal(long long number) {
    long long s = static_cast<long long>(std::round(std::sqrt(1 + 8 * number)));
    return s * s == (1 + 8 * number) && (s - 1) % 2 == 0;
}

// Check if a number is triangular
bool isTriangular(long long number) {
    long long s = static_cast<long long>(std::round(std::sqrt(1 + 24 * number)));
    return s * s == (1 + 24 * number) && (1 + s) % 6 == 0;
}

// Brute force search for next number that is triangular, pentagonal, and hexagonal
long long tphBruteForce() {
    for (long long k = 144;; ++k) {
        long long hk = k * (2 * k - 1);  // hexagonal number formula
        if (isPentagonal(hk) && isTriangular(hk)) {
            return hk;
        }
    }
}

int main() {
    long long result = tphBruteForce();
    std::cout << "Hexagonal number: " << result << std::endl;
    return 0;
}
