#include <algorithm>
#include <deque>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    int T;

    cin >> T;

    while (T--)
    {
        int num;
        string function, arr, temp;
        // 숫자 저장할 덱
        deque<int> arrNum;
        // 배열의 뒤집힘과 에러발생 여부 저장하는 변수
        bool isReverse = true, check = true;
        cin >> function;
        cin >> num;
        cin >> arr;
        for (auto elem : arr)
        {
            if (elem == '[')
            {
                continue;
            }
            // 현재 원소가 숫자라면 temp에 원소 더함
            // (숫자가 두자리이거나 세자리일 수도 있으므로)
            else if ('0' <= elem && elem <= '9')
            {
                temp += elem;
            }
            // 현재 원소가 ']'이거 ','일 경우
            else
            {
                // temp에 숫자가 저장되어 있다면
                if (!temp.empty())
                {
                    // 덱에 해당 숫자 저장
                    arrNum.push_back(stoi(temp));
                    // temp는 초기화
                    temp.clear();
                }
            }
        }
        // 함수 수행
        for (auto elem : function)
        {
            // 현재 원소가 'R'이라면
            if (elem == 'R')
            {
                // 뒤집힘 여부 저장
                isReverse = !isReverse;
            }
            // 현재 원소가 'D'라면
            else
            {
                // 덱에 남은 원소가 없다면 check false로 변경하고 에러 출력
                if (arrNum.empty())
                {
                    check = false;
                    cout << "error" << '\n';
                    break;
                }
                //덱에 남은 원소가 있다면
                else
                {
                    // 배열의 뒤집힘에 따라 덱의 앞이나 뒤에서 원소 제거함
                    if (isReverse)
                    {
                        arrNum.pop_front();
                    }
                    else
                    {
                        arrNum.pop_back();
                    }
                }
            }
        }
        // 에러가 발생하지 않았다면
        if (check)
        {
            // 배열의 뒤집힘에 따라 덱의 앞이나 뒤에서 원소 차례로 출력함
            cout << "[";
            if (isReverse)
            {
                while (!arrNum.empty())
                {
                    cout << arrNum.front();
                    arrNum.pop_front();
                    if (!arrNum.empty())
                    {
                        cout << ',';
                    }
                }
            }
            else
            {
                while (!arrNum.empty())
                {
                    cout << arrNum.back();
                    arrNum.pop_back();
                    if (!arrNum.empty())
                    {
                        cout << ',';
                    }
                }
            }
            cout << "]" << '\n';
        }
    }

    return 0;
}