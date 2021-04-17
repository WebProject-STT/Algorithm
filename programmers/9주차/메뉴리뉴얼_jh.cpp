// 1번 코드
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

map<string, int> courseCnt;
string currentMenu;
// 메뉴 조합 모두 구함
void dfs(string str, int total, int idx)
{
    if (str.length() == total)
    {
        courseCnt[str]++;
        return;
    }
    for (int i = idx; i < currentMenu.length(); i++)
    {
        dfs(str + currentMenu[i], total, i + 1);
    }
}

vector<string> solution(vector<string> orders, vector<int> course)
{
    vector<string> answer;

    for (auto elem : course)
    {
        courseCnt.clear();
        for (auto order : orders)
        {
            // 메뉴명 알파벳순으로 정렬
            sort(order.begin(), order.end());
            currentMenu = order;
            dfs("", elem, 0);
        }
        int maxCnt = 0;
        // 가장 많이 주문된 메뉴 횟수 구함
        for (auto it = courseCnt.begin(); it != courseCnt.end(); it++)
        {
            int cnt = it->second;
            if (cnt >= 2)
            {
                maxCnt = max(maxCnt, cnt);
            }
        }
        // 만일, 2번 이상 주문된 메뉴가 없다면 continue
        if (maxCnt == 0)
        {
            continue;
        }
        // 많이 주문된 메뉴 answer배열에 넣음
        for (auto it = courseCnt.begin(); it != courseCnt.end(); it++)
        {
            if (maxCnt == it->second)
            {
                answer.push_back(it->first);
            }
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}

//2번 코드
// #include <string>
// #include <vector>
// #include <algorithm>
// #include <iostream>
// #include <map>
// using namespace std;

// map<string, int> courseCnt;
// string currentMenu;

// void dfs(string str, int total, int cnt, int idx) {
//     if(total == cnt) {
//         courseCnt[str]++;
//         return;
//     }
//     for(int i = idx; i < currentMenu.length(); i++) {
//         dfs(str + currentMenu[i], total, cnt + 1, i + 1);
//     }
// }

// vector<string> solution(vector<string> orders, vector<int> course) {
//     vector<string> answer;
//     vector<vector<string>> bestCourse;
//     bestCourse.resize(11);
//     for(auto order : orders) {
//         sort(order.begin(), order.end());
//         currentMenu = order;
//         for(auto elem : course) {
//             if(elem <= currentMenu.length()) {
//                 dfs("", elem, 0, 0);
//             }
//         }
//     }
//     for(auto it = courseCnt.begin(); it != courseCnt.end(); it++) {
//         string menu = it -> first;
//         int cnt = it -> second;
//         int length = menu.length();
//         if(cnt < 2) {
//             continue;
//         }
//         for(auto elem : course) {
//             if(elem == length) {
//                 if(bestCourse[elem].size() == 0 ||
//                    courseCnt[bestCourse[elem][0]] < cnt) {
//                     bestCourse[elem].clear();
//                     bestCourse[elem].push_back(menu);
//                 }
//                 else if(courseCnt[bestCourse[elem][0]] == cnt) {
//                     bestCourse[elem].push_back(menu);
//                 }
//             }
//         }
//     }
//     for(auto elem : bestCourse) {
//         if(elem.size() == 0) {
//             continue;
//         }
//         for(auto elem2 : elem) {
//             answer.push_back(elem2);
//         }
//     }
//     sort(answer.begin(), answer.end());
//     return answer;
// }
