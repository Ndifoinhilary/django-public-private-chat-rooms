#include<stdio.h>
#include<string.h>
int main()
{
	char num[100];
	int i;
	printf("enter your character or numbere\n");
	gets(num);
	for(i=0;i<=strlen(num)-1;i++)
	{
		if(num[0+i]==num[strlen(num)-i-1])
		{
			printf("palindrom");
			break;
		}
		else
		printf("not");
		break;
	}
	return 0;
}
