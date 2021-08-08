# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int main()
{
	unsigned char *key; //= (unsigned char *)"01234567890123456789012345678901";
	srand(time(0));
    key=(char*)malloc(sizeof(char)*21);
    for(int i=0;i<21;i++)
    {
      int num=rand()%10;
      key[i]=(char)(num+(int)('0'));
    }


    /* A 128 bit IV */
    unsigned char *iv; //= (unsigned char *)"0123456789012345";
    iv=(char*)malloc(sizeof(char)*8);
    for(int i=0;i<8;i++)
    {
      int num=rand()%10;
      iv[i]=(char)(num+(int)('0'));
    }

    FILE *fptr; FILE *fptr2;
    fptr = fopen("session_key.txt","w");
    fptr2 = fopen("iv.txt","w");

    for(int i=0;i<21;i++)
    {
    	fprintf(fptr,"%c",key[i]);
    }
    //fprintf(fptr,"\n");

	for(int i=0;i<8;i++)
    {
    	fprintf(fptr2,"%c",iv[i]);
    } 
    //fprintf(fptr2,"\n");   

    fclose(fptr);
    fclose(fptr2);

	return 0;
}