#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <iostream>

// Solution by: Ting Wei Liu and Jeffrey Kam

bool isExact(const std::vector<std::vector<int>>& A, size_t i, size_t j) {
	for (size_t k = 0; k < A.size(); ++k) {
		if (A[i][k] != A[j][k]) {
			return false;
		}
	}
	return true;
}

int truthfullness(const std::vector<std::vector<int>>& A, size_t i) {
	if (A[i][i] != 1) {
		return 0;
	}

	for (size_t j = 0; j < A.size(); ++j) {
		if (A[i][j] == 1) {
			if (!isExact(A, i, j)) {
				return 0;
			}
		} else {
			if (isExact(A, i, j)) {
				return 0;
			}
		}
	}

	return std::accumulate(A[i].begin(), A[i].end(), 0);
}

int main() {
	size_t testCases;
	std::cin >> testCases;
	for (size_t i = 0; i < testCases; ++i) {
		std::cout << "Class Room#" << i + 1 << ' ';

		size_t num;
		std::cin >> num;
		if (num == 0) {
			std::cout << "contains atleast 0 and atmost 0 liars\n";
			continue;
		}

		std::vector<std::vector<int>> A (num, std::vector<int>(num, 0));
		for (size_t j = 0; j < num; ++j) {
			std::string row;
			std::cin >> row;
			for (size_t k = 0; k < num; ++k) {
				if (row[k] == 'T') {
					A[j][k] = 1;
				}
			}
		}

		int minTruth = std::numeric_limits<int>::max() / 2;
		int maxTruth = 0;
		int minRow = num;

		for (size_t j = 0; j < num; ++j) {
			const int truth = truthfullness(A, j);
			if (truth > 0) {
				minTruth = std::min(minTruth, truth);
			}
			maxTruth = std::max(maxTruth, truth);
			minRow = std::min(minRow, std::accumulate(A[j].begin(), A[j].end(), 0));
		}

		int upperBound = num;
		int lowerBound = num - maxTruth;
		
		if (minRow == 0) {
			upperBound -= minTruth;
		}

		if (upperBound < lowerBound) {
			std::cout << "is paradoxical\n";
		} else {
			std::cout << "contains atleast " << lowerBound
			          << " and atmost " << upperBound << " liars\n";
		}
	}
}