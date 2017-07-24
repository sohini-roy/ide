#include <stdio.h>
#include <string.h>

int s,part[100],height[100][100];
int min(int a, int b)
{
    int res = a;
    if(b < a)
        res = b;
    return res;
}

void findLongestPalindromicString(int k)
{
    printf("inside func");
    int text[100];
    int N = sizeof(height[k]);
    printf("line 18");
    for(int i=0; i<N; i++){
      text[i]= height[k][i];
      printf("for executing\n");
    }
    printf("line 22");
    N = 2*N + 1;
    int L[N];
    L[0] = 0;
    L[1] = 1;
    int C = 1;
    int R = 2;
    int i = 0;
    int iMirror;
    int maxLPSLength = 0;
    int maxLPSCenterPosition = 0;
    int start = -1;
    int end = -1;
    int diff = -1;
    printf("line37\n");
    for (i = 2; i < N; i++)
    {
        iMirror  = 2*C-i;
        L[i] = 0;
        diff = R - i;
        if(diff > 0)
            L[i] = min(L[iMirror], diff);

        while ( ((i + L[i]) < N && (i - L[i]) > 0) &&
            ( ((i + L[i] + 1) % 2 == 0) ||
            (text[(i + L[i] + 1)/2] == text[(i - L[i] - 1)/2] )))
        {
            L[i]++;
        }

        if(L[i] > maxLPSLength)
        {
            maxLPSLength = L[i];
            maxLPSCenterPosition = i;
        }

        if (i + L[i] > R)
        {
            C = i;
            R = i + L[i];
        }
        printf("64\n");
    }
    start = (maxLPSCenterPosition - maxLPSLength)/2;
    end = start + maxLPSLength-1;
    printf("68\n");
    if(start==-1 && end==sizeof(height[k])-1){
       printf("yes\n");
    }
    else{
       printf("no\n");
    }

}
int main()
{
  int k=1,i,j;
  scanf("%d", &s);
  printf("ass1");
  if(s>=1 && s<=100){
    for(i=1; i<=s; i++){
      scanf("%d", &part[i]);
      printf("ass2");
      // printf("\n");
      for(j=1; j<=part[i]; j++){
        printf("ass3");
        scanf("%d", &height[i][j]);
        printf("ass0");
      }
    }
    while(k<=s){
      printf("while loop ");
      if(part[k]%2==0 || part[k]<3){
        printf("no\n");
      } else {
        printf("went to func");
        findLongestPalindromicString(k);
        k++;
      }
    }
  }
    return 0;
}
