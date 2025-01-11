#include <vector>
#include <unordered_set>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        // Check rows
        for (int i = 0; i < 9; ++i) {
            std::unordered_set<char> rowSet;
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    if (rowSet.find(board[i][j]) != rowSet.end()) {
                        return false;
                    }
                    rowSet.insert(board[i][j]);
                }
            }
        }

        // Check columns
        for (int j = 0; j < 9; ++j) {
            std::unordered_set<char> colSet;
            for (int i = 0; i < 9; ++i) {
                if (board[i][j] != '.') {
                    if (colSet.find(board[i][j]) != colSet.end()) {
                        return false;
                    }
                    colSet.insert(board[i][j]);
                }
            }
        }

        // Check 3x3 sub-boxes
        for (int block = 0; block < 9; ++block) {
            std::unordered_set<char> boxSet;
            for (int i = block / 3 * 3; i < block / 3 * 3 + 3; ++i) {
                for (int j = block % 3 * 3; j < block % 3 * 3 + 3; ++j) {
                    if (board[i][j] != '.') {
                        if (boxSet.find(board[i][j]) != boxSet.end()) {
                            return false;
                        }
                        boxSet.insert(board[i][j]);
                    }
                }
            }
        }

        return true;
    }
};