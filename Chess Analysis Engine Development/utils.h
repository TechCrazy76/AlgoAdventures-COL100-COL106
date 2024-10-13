#include <stdio.h>
int piecepoint(int piece) //defining a function for returning the piece points
{
  if(piece==0)
    return 0;
   else if(piece==1) //pawn
    return 1;
   else if(piece==2) //rook
    return 5;
   else if(piece==3) //knight
    return 3;
   else if(piece==4) //bishop
    return 3;
   else if(piece==5) //queen
    return 9;
   else if(piece==6) //king
    return 0;
  else
     return 0;
  }
int analyseScore(int chessboard[8][8]) //defining a function for analysing the position
{
  int wscore=0,bscore=0; 
   for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
          if(chessboard[i][j]%10==1) //calculating total piece points of white
            wscore=wscore+piecepoint(chessboard[i][j]/10);
           else if(chessboard[i][j]%10==2) //calculating total piece points of black
            bscore=bscore+piecepoint(chessboard[i][j]/10);               
} 
   }
  if(wscore!=bscore) //returning the net score as difference between the total points of white and black
  return (wscore-bscore);
  else 
    return 0;
}
