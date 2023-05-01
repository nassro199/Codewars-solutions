#include <vector>
#include <utility>
#include <algorithm>

int sum_intervals(std::vector<std::pair<int, int>> intervals) {
  std::vector<std::pair<int, int>> non_overlapping_intervals;
  std::sort(intervals.begin(), intervals.end());

  for (const auto& interval : intervals) {
    if (non_overlapping_intervals.empty() || interval.first > non_overlapping_intervals.back().second) {
      non_overlapping_intervals.push_back(interval);
    } else {
      non_overlapping_intervals.back().second = std::max(non_overlapping_intervals.back().second, interval.second);
    }
  }

  int sum = 0;
  for (const auto& interval : non_overlapping_intervals) {
    sum += interval.second - interval.first;
  }
  return sum;
}