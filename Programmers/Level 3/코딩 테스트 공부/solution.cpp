#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int alp, int cop, vector<vector<int>> problems) {
    int max_alp = 0, max_cop = 0;
    for (auto temp: problems){
        if (max_alp < temp[0]){
            max_alp = temp[0];
        }
        if (max_cop < temp[1]){
            max_cop = temp[1];
        }
    }
    
    problems.push_back({0, 0, 1, 0, 1});
    problems.push_back({0, 0, 0, 1, 1});
    
    if (alp > max_alp){
        alp = max_alp;
    }
    if (cop > max_cop){
        cop = max_cop;
    }
    
    int test[151][151];
    for (int i = 0; i < 151; i++){
        for (int j = 0; j < 151; j++){
            test[i][j] = 9999;
        }
    }
    
    test[alp][cop] = 0;
    
    for (int i = alp; i <= max_alp; i++){
        for (int j = cop; j <= max_cop; j++){
            for (auto temp : problems){
                if (i >= temp[0] && j >= temp[1]){
                    int x = min(i + temp[2], max_alp);
                    int y = min(j + temp[3], max_cop);
                    test[x][y] = min(test[i][j] + temp[4], test[x][y]);
                }
            }
        }
    }
    return test[max_alp][max_cop];
}