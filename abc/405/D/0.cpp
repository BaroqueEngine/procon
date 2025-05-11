/*
Orignal Python Code
import heapq
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
cnt = [[10**18] * W for _ in range(H)]

dir = {
    (1, 0): "<",
    (-1, 0): ">",
    (0, 1): "^",
    (0, -1): "v",
}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def write(px, py, cx, cy):
    dx = cx - px
    dy = cy - py
    S[cy][cx] = dir[(dx, dy)]

q = []
for y in range(H):
    for x in range(W):
        if S[y][x] == "E":
            cnt[y][x] = 0
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx < 0 or tx >= W or ty < 0 or ty >= H:
                    continue
                if S[ty][tx] != ".":
                    continue
                write(x, y, tx, ty)
                cnt[ty][tx] = 1
                heapq.heappush(q, (1, tx, ty))

while len(q) > 0:
    step, x, y = heapq.heappop(q)
    if cnt[y][x] != step:
        continue
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or tx >= W or ty < 0 or ty >= H:
            continue
        if S[ty][tx] != ".":
            continue
        write(x, y, tx, ty)
        cnt[ty][tx] = step + 1
        heapq.heappush(q, (step + 1, tx, ty))

for line in S:
    print("".join(line))
*/
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <tuple>
#include <map>

using namespace std;

const long long INF = 1e18;

void write(vector<string>& s, int px, int py, int cx, int cy) {
    int dx = cx - px;
    int dy = cy - py;
    if (dx == 1 && dy == 0) {
        s[cy][cx] = '<';
    } else if (dx == -1 && dy == 0) {
        s[cy][cx] = '>';
    } else if (dx == 0 && dy == 1) {
        s[cy][cx] = '^';
    } else if (dx == 0 && dy == -1) {
        s[cy][cx] = 'v';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int h, w;
    cin >> h >> w;

    vector<string> s(h);
    for (int i = 0; i < h; ++i) {
        cin >> s[i];
    }

    vector<vector<long long>> cnt(h, vector<long long>(w, INF));

    // Using priority_queue for Dijkstra-like approach: {step, x, y}
    priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<tuple<long long, int, int>>> q;

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int y = 0; y < h; ++y) {
        for (int x = 0; x < w; ++x) {
            if (s[y][x] == 'E') {
                cnt[y][x] = 0;
                for (int i = 0; i < 4; ++i) {
                    int tx = x + dx[i];
                    int ty = y + dy[i];

                    if (tx < 0 || tx >= w || ty < 0 || ty >= h) {
                        continue;
                    }
                    if (s[ty][tx] != '.') {
                        continue;
                    }
                    write(s, x, y, tx, ty);
                    cnt[ty][tx] = 1;
                    q.push({1, tx, ty});
                }
            }
        }
    }

    while (!q.empty()) {
        auto [step, x, y] = q.top();
        q.pop();

        if (cnt[y][x] != step) {
            continue;
        }

        for (int i = 0; i < 4; ++i) {
            int tx = x + dx[i];
            int ty = y + dy[i];

            if (tx < 0 || tx >= w || ty < 0 || ty >= h) {
                continue;
            }
            if (s[ty][tx] != '.') {
                continue;
            }

            if (cnt[y][x] + 1 < cnt[ty][tx]) {
                 write(s, x, y, tx, ty);
                 cnt[ty][tx] = cnt[y][x] + 1;
                 q.push({cnt[ty][tx], tx, ty});
            }
        }
    }

    for (int i = 0; i < h; ++i) {
        cout << s[i] << endl;
    }

    return 0;
}