#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stack>

using namespace std;
const int k = 100010;

int n, m;
vector<vector<pair<int, int>>> v;
long long path[k];
bool v_visit[k];


void deikstry() {
	int point = 0, size; // �������
	long long min;  // ��� �����
	for (int c = 0; c < n; c++) {
		min = 10000000000000;  // ��������� ����� ��������������
		for (int i = 0; i < n; i++) { //�������� ���� ������� ��� ��������
			if (!v_visit[i] && path[i] < min) {
				point = i;
				min = path[i];
			}
		}
		v_visit[point] = true;
		size = v[point].size();

		for (int i = 0; i < size; i++) {
			if (path[v[point][i].first] >(path[point] + v[point][i].second)) { // ����� ����� �������� ����
				path[v[point][i].first] = path[point] + v[point][i].second;
			}
		}
	}
}


int main()
{
	cin >> n >> m;
	vector<pair<int, int>> t;

	for (int i = 0; i < n; i++) { // �������� ������
		v.push_back(t);
		path[i] = 10000000000000;    // ��������� ����� ��������������
		v_visit[i] = false;   
	}
	int v1, v2, w;
	for (int i = 0; i < m; i++) { // �����
		cin >> v1 >> v2 >> w;
		v1--;
		v2--;
		v[v1].push_back(pair<int, int>(v2, w));
		v[v2].push_back(pair<int, int>(v1, w));
	}
	int start, end;
	cin >> start >> end;
	start--;
	end--;
	path[start] = 0;
	deikstry();
	cout << path[end];


	return 0;
}