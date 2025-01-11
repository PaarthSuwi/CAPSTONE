#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> seen;

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                char current = board[i][j];
                if (current != '.') {
                    string rowKey = "row" + to_string(i) + current;
                    string colKey = "col" + to_string(j) + current;
                    string boxKey = "box" + to_string(i / 3) + to_string(j / 3) + current;
                    if (seen.count(rowKey) || seen.count(colKey) || seen.count(boxKey)) {
                        return false;
                    }
                    seen.insert(rowKey);
                    seen.insert(colKey);
                    seen.insert(boxKey);
                }
            }
        }
        return true;
    }
};

int main() {
    Solution solution;

    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    if (solution.isValidSudoku(board)) {
        printf("The Sudoku board is valid.\n");
    } else {
        printf("The Sudoku board is invalid.\n");
    }

    return 0;
}