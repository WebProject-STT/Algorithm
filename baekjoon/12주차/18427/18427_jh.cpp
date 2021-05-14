#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
#define studentMAX 51
#define heightMAX 1001
#define MOD 10007

int N, M, H, cnt = 0;
// dp[i][j] => i번째 학생까지 검사했을때 j높이의 블록을 쌓을 수 있는 경우의 수
// 크기는 최대입력값 + 1씩으로 지정
int dp[studentMAX][heightMAX];
// 각 학생이 가진 블록의 높이를 저장
vector<vector<int>> studentBlockHeight;

int main()
{
    string blockHeight;

    cin >> N >> M >> H;
    studentBlockHeight.resize(N + 1);
    // 위에서 N, M, H, \n를 입력 받게됨
    // 이후 블록 높이 입력받을 때 '\n'를 기준으로 입력값이 구분되기 때문에
    // 여기서 '\n'는 무시해줘야함 => ignore함수를 사용 => 입력 버퍼를 비움
    cin.ignore(1);

    for (int i = 1; i <= N; i++)
    {
        getline(cin, blockHeight, '\n');
        stringstream temp(blockHeight);
        string num;
        // 입력받은 블록 높이를 공백을 기준으로 구분해서 저장
        while (temp >> num)
        {
            studentBlockHeight[i].push_back(stoi(num));
        }
    }
    // dp의 0번째 원소들은 모두 1로 지정
    // => 이후 dp를 진행할때 만드려는 블록의 높이가 k일때
    //    (이전 학생이 만든 블록 높이가 0 + 현재 학생이 가진 블록 높이 k)
    //    => k가 되는 경우도 더해주기 위해
    //    => 즉, 이전 학생이 블록을 사용하지 않은 경우도 검사해야 하기 때문!!
    for (int i = 0; i <= N; i++)
    {
        dp[i][0] = 1;
    }

    for (int i = 1; i <= N; i++)
    {
        // 현재 만드려는 블록의 높이 지정
        for (int j = 1; j <= H; j++)
        {
            int size = studentBlockHeight[i].size();
            // 현재 학생이 가진 블록 높이 모두 검사
            for (int k = 0; k < size; k++)
            {
                int currentHeight = studentBlockHeight[i][k];
                // 만드려는 블록 높이가 현재 학생의 블록 높이보다 높거나 같다면
                if (j >= currentHeight)
                {
                    // 모든 경우의 수를 더해줌
                    dp[i][j] += dp[i - 1][j - currentHeight];
                    dp[i][j] %= MOD;
                }
            }
            // 직전의 경우의 수도 더해줘야됨
            dp[i][j] += dp[i - 1][j];
            dp[i][j] %= MOD;
        }
    }

    cout << dp[N][H];

    return 0;
}