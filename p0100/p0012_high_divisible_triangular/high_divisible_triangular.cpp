#include <iostream>
#include <vector>


// int numdivisores()



class PrimeGenerator {
public:    
    PrimeGenerator() {
        this->n = 1;
        this->flag = true;
    }

    int next() {
        if (this->flag) {
            this->flag = false;
            return 2;
        }
        this->n += 2;
        for (int i = 0, psize = primes.size(); i < psize; ++i) {
            if (this->n == primes[i]) {
                return this->n;
            }
            if (this->n > primes[i]) {
                break;
            }
        }
        while (true) {
            bool isPrime = true;
            for (int i = 0, psize = primes.size(); i < psize; ++i) {
                int p = primes[i];
                if (this->n % p == 0) {
                    isPrime = false;
                    break;
                }
                if (p * p > this->n) {
                    break;
                }
            }
            if (isPrime) {
                primes.push_back(this->n);
                return this->n;
            }
            this->n += 2;
        }        
    }

    void reset() {
        this->n = 1;
        this->flag = true;
    }

private:
    bool flag;
    int n;
    static std::vector<int> primes; //  = {};
};

std::vector<int> PrimeGenerator::primes = {};


int countDivisors(int n) {
    PrimeGenerator pg;
    int numdivisores = 1;
    while (n > 1) {
        int p = pg.next();
        int count = 0;
        while (n % p == 0) {
            count++;
            n /= p;
        }
        numdivisores *= (count + 1);
    }
    return numdivisores;
}


int findTriangleNumber(int N) {
    int d0 = 3;
    while (true) {
        // std::cout << "Current d0: " << d0 << std::endl;
        int nd0 = countDivisors(d0);
        for (int j = 0; j < 2; ++j) {
            int d1 = d0 / 2 + j;
            // std::cout << "Current d1: " << d1 << std::endl;
            int nd1 = countDivisors(d1);
            if (nd0 * nd1 > N) {
                return d0 * d1;
            }
        }
        d0 += 2;
    }
}


int main() {

    int N = 500;
    int triangleNumber = findTriangleNumber(N); 
    std::cout << "The first triangular number with more than " 
              << N << " divisors is: " << triangleNumber << std::endl;

    return 0;
}