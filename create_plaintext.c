# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int main()
{
	unsigned char *msg; //= (unsigned char *)"01234567890123456789012345678901";
    srand(time(0));
    int sz=rand()%50+10;

    msg=(char*)malloc(sizeof(char)*(sz+1));

    for(int i=0;i<sz;i++)
    {
      int num=rand()%26;
      msg[i]=(char)(num+(int)('a'));
    }
    msg[sz]='\0';

    FILE *fptr; 
    fptr = fopen("Mail-sample.txt","w");

    for(int i=0;i<sz;i++)
    {
    	fprintf(fptr,"%c",msg[i]);
    }

    //printf("msg: %s\n",msg);

    fclose(fptr);

	return 0;
}