#include <stdio.h>
#include "utils.h"
int main() {
  int chessboard[8][8] = {0};

  for (int i = 0; i < 8; i++) { //taking input of chessboard
    for (int j = 0; j < 8; j++) {
      scanf("%d", &chessboard[i][j]);
    }
  }
  printBoard(chessboard); //printing the chessboard
  int calc = analyseScore(chessboard); //analysing the chessboard
  if (calc == 0)
    printf("0 BALANCED\n");
  else if (calc > 0)
    printf("%d WHITE\n", calc);
  else if (calc < 0)
    printf("%d BLACK\n", -calc);

  return 0;
}
// 21 31 41 51 61 41 31 21
// 11 11 11 11 11 11 11 11
// 00 00 00 00 00 00 00 00
// 00 00 00 00 00 00 00 00
// 00 00 00 00 00 00 00 00
// 00 00 00 00 00 00 00 00
// 12 12 12 12 12 12 12 12
// 22 32 42 52 62 42 32 22
