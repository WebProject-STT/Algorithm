#include <stack>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    string input;
    // 막대기 저장하는 스택
    stack<char> inputStack;
    // 조각 개수 저장하는 변수
    int piece = 0;

    cin >> input;

    for (int i = 0; i < input.length(); i++)
    {
        char current = input[i];
        if (current == '(')
        {
            inputStack.push(current);
        }
        else
        {
            inputStack.pop();
            // 레이저일 경우
            if (input[i - 1] == '(')
            {
                // 조각 개수를 막대기 개수만큼 증가
                piece += inputStack.size();
            }
            // 막대기의 오른쪽 끝일 경우
            else
            {
                // 조각 개수 1 증가
                piece++;
            }
        }
    }
    cout << piece;
}