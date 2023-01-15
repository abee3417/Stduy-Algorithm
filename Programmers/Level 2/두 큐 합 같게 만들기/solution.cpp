#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0, q1ptr = 0, q2ptr = 0;
    int size = queue1.size();
    long long int sum1 = accumulate(queue1.begin(), queue1.end(), 0);
    long long int sum2 = accumulate(queue2.begin(), queue2.end(), 0);
    
    while(answer <= (size - 1) * 4){
        if (sum1 > sum2){
            sum1 -= queue1[q1ptr];
            sum2 += queue1[q1ptr];
            queue2.push_back(queue1[q1ptr++]);
        }
        else if (sum1 < sum2){
            sum1 += queue2[q2ptr];
            sum2 -= queue2[q2ptr];
            queue1.push_back(queue2[q2ptr++]);
        }
        else{
            return answer;
        }
        answer++;
    }
    return -1;
}