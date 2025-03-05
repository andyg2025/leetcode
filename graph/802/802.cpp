#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
    public:
        vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
            int n=graph.size();
            vector<int> visited(n), instack(n);
            vector<int> result;

            for(int i=0; i<n; i++){
                dfs(i, graph, visited, instack);
            }

            // for(int i=0; i<n; i++){
            //     cout<<instack[i]<<"";
            // }

            for(int i=0; i<n; i++){
                if(!instack[i]) result.push_back(i);
            }
            return result;
        }

        bool dfs(int node, vector<vector<int>>& graph, vector<int>& visited, vector<int>& instack) {
            if(instack[node]) return true;
            if(visited[node]) return false;
            
            instack[node]=true;
            visited[node]=true;

            for(int n:graph[node]){
                if(dfs(n, graph, visited, instack)) return true;
            }
            instack[node] = false;
            return false;
        }
};


int main() {
    Solution s;
    vector<vector<int>> graph = {{1,2},{2,3},{5},{0},{5},{},{}};
    
    auto result = s.eventualSafeNodes(graph);

    for(int n:result){
        cout<<n<<" ";
    }

    return 0;
}