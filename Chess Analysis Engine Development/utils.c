#include <stdio.h>
char whitepiece(int w) //defining a function for displaying the white pieces 
{
  if(w==0)
    return '.';
   else if(w==1)
    return 'P';
   else if(w==2)
    return 'R';
   else if(w==3)
    return 'N';
   else if(w==4)
    return 'B';
   else if(w==5)
    return 'Q';
   else if(w==6)
    return 'K';
  else
     return '?';
  }
char blackpiece(int w) //defining a function for displaying the black pieces 
{
  if(w==0)
    return '.';
   else if(w==1)
    return 'p';
   else if(w==2)
    return 'r';
   else if(w==3)
    return 'n';
   else if(w==4)
    return 'b';
   else if(w==5)
    return 'q';
   else if(w==6)
    return 'k';
  else
     return '?';
  }
void printBoard(int chessboard[8][8]) //defining a function for displaying the chessboard position
{
  for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
           if(chessboard[i][j] % 10 == 1) //white pieces
             printf("%c ", whitepiece(chessboard[i][j]/10));
          else  if(chessboard[i][j] % 10 == 2) //black pieces
             printf("%c ", blackpiece(chessboard[i][j]/10));
          else if(chessboard[i][j]%10==0 && chessboard[i][j]/10==0) 
             printf(". ");
          else
            printf("? ");
           }
    printf("\n");
}
}
