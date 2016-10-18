#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

long long MaxPairwiseProduct(const vector<int>& numbers) {
  long long result = 0;
  int n = numbers.size();
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      if (((long long)numbers[i]) * numbers[j] > result) {
        result = ((long long)numbers[i]) * numbers[j];
      }
    }
  }
  return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    } 

    long long result = MaxPairwiseProduct(numbers);
    cout << result << "\n";
    return 0;
}

/**
problem: our program performs about n^2 steps on a sequence of length
n. For the maximal possible value n = 200,000 = 2*10^5, the number of
steps is about 10,000,000,000 = 10^10. This is too much. Recall that
modern machines can perform roughly 10^9 basic operations per second
(this depends on a machine of course, but 10^9 is a reasonable average
estimate). y hay un límite de 1 segundo para resolver esto. Thus, we
need a faster algorithm.
**/
