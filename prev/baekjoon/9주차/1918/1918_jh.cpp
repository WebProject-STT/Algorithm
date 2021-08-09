#include <algorithm>
#include <string>
#include <stack>
#include <map>
#include <iostream>
using namespace std;
// 각 기호의 우선순위 저장
map<char, int> priority;
// 기호를 저장
stack<char> sign;

// 우선순위가 높은 기호들을 먼저 출력하는 것이 핵심!!

// 스택에 있는 기호와 입력으로 들어온 기호의 우선순위를 비교해 출력하는 함수
// (현재 입력값과 입력값이 ')'인지 확인하는 변수가 매개변수)
void check(char current, bool flag)
{
    while (!sign.empty())
    {
        char signTop = sign.top();
        // signTop이 '('라면 우선순위 높은 기호들은 모두 출력했으므로 break
        if (signTop == '(')
        {
            break;
        }
        else
        {
            // 입력값이 ')'이거나 signTop이 입력값의 우선순위보다 높거나 같다면 기호 출력
            if (flag || (!flag && priority[signTop] <= priority[current]))
            {
                cout << signTop;
                sign.pop();
            }
            else
            {
                break;
            }
        }
    }
}

int main()
{
    string input;
    // 기호에 맞는 우선순위 지정 (숫자가 낮을수록 우선순위가 높다는 의미)
    priority['('] = 1;
    priority[')'] = 1;
    priority['*'] = 2;
    priority['/'] = 2;
    priority['+'] = 3;
    priority['-'] = 3;

    cin >> input;

    for (auto elem : input)
    {
        // 알파벳은 바로 출력
        if (isalpha(elem))
        {
            cout << elem;
            continue;
        }
        switch (elem)
        {
        case '(':
            sign.push(elem);
            break;
        case ')':
            check(')', true);
            // 괄호 내의 기호는 모두 출력했으므로 '('을 pop해준다.
            sign.pop();
            break;
        default:
            // 스택이 비어있지 않거나 signTop이 입력값의 우선순위보다 높거나 같다면 check 함수 호출
            if (!sign.empty() && priority[sign.top()] <= priority[elem])
            {
                check(elem, false);
            }
            // 우선순위 높은 기호들 모두 출력한 뒤에 현재 입력값 스택에 push
            sign.push(elem);
        }
    }
    while (!sign.empty())
    {
        cout << sign.top();
        sign.pop();
    }

    return 0;
}