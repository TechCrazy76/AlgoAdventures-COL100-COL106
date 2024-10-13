#include <stdio.h>
void querry1() { //defining a function for querry 1
  int n, k, temp, p, sum = 0;
  scanf("%d%d", &n, &k); // enter array size
  int array[n];
  for (int i = 0; i < n; i++) 
    scanf("%d", &array[i]); //enter array elements
  int small = array[0];
  for (int j = 0; j < n - 1; j++) { //sorting the array elements in ascending order
    for (int k = j; k < n; k++) {
      if (array[k] < small) {
        small = array[k];
        p = k;
      }
    }
    if (small != array[j]) {
      temp = array[j];
      array[j] = small;
      array[p] = temp;
    }
    small = array[j + 1];
  }
  for (int l = n - 1; l >= n - k; l--) //calcutate the maximum possible value of sum of the required no. of array elements
    sum = sum + array[l];
  printf("%d\n", sum);
}

void querry2() { //defining a function for querry 2
  int n1, n2, temp, p;
  scanf("%d%d", &n1, &n2); //enter size of two arrays
  int n3 = n1 + n2; //size of the merged array
  int array[n3];
  for (int i = 0; i < n3; i++)
    scanf("%d", &array[i]); //enter array elements directly into the merged array
  int small = array[0];
  for (int j = 0; j < n3 - 1; j++) { //sorting the array elements in ascending order
    for (int k = j; k < n3; k++) {
      if (array[k] < small) {
        small = array[k];
        p = k;
      }
    }
    if (small != array[j]) {
      temp = array[j];
      array[j] = small;
      array[p] = temp;
    }
    small = array[j + 1];
  }
  for (int l = 0; l < n3; l++) //display the sorted array in ascending order
    printf("%d ", array[l]);
  printf("\n");
}

void querry3() { //defining a function for querry 3
  int n, count = 0, temp, large = 0, r, x = 0, y = 0;
  scanf("%d", &n); //enter array size
  int array[n];
  for (int i = 0; i < n; i++) {
    scanf("%d", &array[i]); //enter array elements
    int num = array[i];
    while (num != 0) { //for finding the longest length of binary representation of the array elements
      num = num / 2;
      count++;
    }
    if (large < count)
      large = count;
    count = 0;
  }
  int matrix[large][n], b[large];
  for (int j = 0; j < n; j++) {
    int num = array[j];
    while (num != 0) { //finding the length of binary representation and the digits of binary
      b[x] = num % 2;
      num = num / 2;
      x++;
    }
    for (int k = 0; k < large; k++) { //filling the matrix 
      if (k <= (large - 1 - x))
        matrix[j][k] = 0;
      else
        matrix[j][k] = b[large - 1 - k];
    }
    x = 0;
  }

  for (int l = 0; l < large; l++) { //display the final output
    for (int m = 0; m < n; m++)
      printf("%d ", matrix[m][l]);
    printf("\n");
  }
}

int main(void) { 
  // Write your code here
  int queries, qno;
  scanf("%d", &queries); //enter number of querries
  for (int i = 1; i <= queries; i++) {
    scanf("%d", &qno); //enter querry no. 
    if (qno == 1)
      querry1(); //querry 1
    if (qno == 2)
      querry2(); //querry 2
    if (qno == 3)
      querry3(); //querry 3
  }
  return 0;
}
