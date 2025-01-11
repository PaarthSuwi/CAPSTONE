#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_set>

using namespace std;

// BFS Implementation
vector<int> bfs(const vector<vector<int>>& graph, int start) {
    queue<int> q;
    unordered_set<int> visited;
    vector<int> order;

    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        order.push_back(node);

        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }

    return order;
}

// DFS Implementation
vector<int> dfs(const vector<vector<int>>& graph, int start) {
    stack<int> s;
    unordered_set<int> visited;
    vector<int> order;

    s.push(start);
    visited.insert(start);

    while (!s.empty()) {
        int node = s.top();
        s.pop();
        order.push_back(node);

        // Traverse neighbors in reverse order to maintain left-to-right order
        for (auto it = graph[node].rbegin(); it != graph[node].rend(); ++it) {
            int neighbor = *it;
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                s.push(neighbor);
            }
        }
    }

    return order;
}

int main() {
    // Graph representation as an adjacency list
    vector<vector<int>> graph = {
        {},         // 0 (unused)
        {2, 3},     // 1
        {1, 4, 5},  // 2
        {1},        // 3
        {2},        // 4
        {2}         // 5
    };

    int start_node = 1;

    // BFS Traversal
    vector<int> bfs_order = bfs(graph, start_node);
    cout << "BFS Order: ";
    for (int node : bfs_order) {
        cout << node << " ";
    }
    cout << endl;

    // DFS Traversal
    vector<int> dfs_order = dfs(graph, start_node);
    cout << "DFS Order: ";
    for (int node : dfs_order) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}