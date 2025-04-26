// Given an integer array nums and an integer k, return the k most frequent elements within the array.
// The test cases are generated such that the answer is always unique.
// Input: nums = [1,2,2,3,3,3], k = 2
// Output: [2,3]

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> updateMap;
    map<int, unordered_set<int>> mainMap;
    mainMap[1] = unordered_set<int>();

    for (int num : nums) {
        if (updateMap.find(num) == updateMap.end()) {
            updateMap[num] = 1;
            mainMap[1].insert(num);
        } else {
            int freq = updateMap[num];
            mainMap[freq].erase(num);
            updateMap[num]++;
            mainMap[updateMap[num]].insert(num);
        }
    }

    vector<int> return_list;
    int counter_pop = k;
    auto it = mainMap.rbegin();
    while (counter_pop > 0 && it != mainMap.rend()) {
        auto& num_set = it->second;
        for (auto iter = num_set.begin(); iter != num_set.end() && counter_pop > 0; ) {
            return_list.push_back(*iter);
            iter = num_set.erase(iter);
            counter_pop--;
        }
        ++it;
    }
    return return_list;
}

int main() {
    vector<int> numbers = {4,1,-1,2,-1,2,3};
    int x = 3;
    vector<int> result = topKFrequent(numbers, x);
    for (int n : result) {
        cout << n << " ";
    }
    cout << endl;
    return 0;
}