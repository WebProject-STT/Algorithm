#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    int L, R, answer = 0, length;
    string iStr, rStr;

    cin >> L >> R;
    // 입력받은 정수 L과 R을 문자열 형태로 변경
    iStr = to_string(L);
    rStr = to_string(R);

    length = iStr.length();
    // 두 수의 자릿수가 다르다면 두 수 사이에 8이 안들어가는 정수가 있을 수 밖에 없음
    if (length != rStr.length())
    {
        answer = 0;
    }
    else
    {
        int length = iStr.length();
        // 두 정수의 첫번째 자릿수부터 검사
        for (int i = 0; i < length; i++)
        {
            char iCurrent = iStr[i];
            char rCurrent = rStr[i];
            // 두 숫자가 같음
            if (iCurrent == rCurrent)
            {
                // 숫자가 8이라면 8의 개수 증가
                // (앞에서부터 계속 숫자가 같기때문에 해당 자릿수까지는 숫자가 변경될 수가 없음)
                if (iCurrent == '8')
                {
                    answer++;
                }
            }
            else
            {
                break;
            }
        }
    }
    cout << answer;
}