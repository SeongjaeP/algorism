#include <iostream> 
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
const int MAX = 501;
int map[MAX][MAX] = {0, };
bool visited[MAX][MAX] = {0, };
int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};
queue<pair<int, int>> q;
vector<int> v;
int s = 1;

void BFS(int y, int x) {
    visited[y][x] = true;
    q.push(make_pair(y,x));

    while (!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();

        for (int = 0; i < 4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (0 <= nx && < m && 0 <= ny && ny < n && map[nx][ny] == 1 && !visited)
        }
    }
}