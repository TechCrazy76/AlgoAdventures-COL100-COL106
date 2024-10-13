#include <stdio.h>
#include <math.h>
// function encrypt 
// Input parameters: the number and the key
int encrypt(int n,int key)
{
  int bit_n,bit_key;
  if(n==0||key==0)
    return 0;
  else{
    bit_n = n%2;
  bit_key = key%2;
  return encrypt(floor(n/2),floor(key/2))*2+ (bit_n ^ bit_key);
  }
}
int main() {
    // Take the number and key as input
    // Encrypt the number
    // Print the encrypted value
int n, key;
  scanf("%d%d", &n,&key);
  printf("%d", encrypt(n,key));
    return 0;
}
