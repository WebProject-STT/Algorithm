#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, start;
        bool check = true;
        string previous = "";
        vector<string> phoneNumbers;
        cin >> n;
        phoneNumbers.resize(n);
        for (int i = 0; i < n; i++)
        {
            cin >> phoneNumbers[i];
        }
        // 전화번호 정렬
        // (113, 12340, 123440, 12345) => (113, 12340, 123440, 12345)
        sort(phoneNumbers.begin(), phoneNumbers.end());
        for (int i = 0; i < n - 1; i++)
        {
            // 현재 원소가 다음 원소에 포함되어 있는지 확인하면 됨
            // 다음 원소의 길이가 현재 원소보다 짧을 경우에는
            // 다음 원소.substr(0, 현재 원소 길이) => 다음 원소 전체
            if (phoneNumbers[i] == phoneNumbers[i + 1].substr(0, phoneNumbers[i].length()))
            {
                check = false;
                break;
            }
        }
        if (check)
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }
    }

    return 0;
}