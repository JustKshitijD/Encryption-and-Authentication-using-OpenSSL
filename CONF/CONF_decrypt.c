#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>

void handleErrors(void)
{
    ERR_print_errors_fp(stderr);
    abort();
}


int decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
            unsigned char *iv, unsigned char *plaintext, int keylen)
{
    EVP_CIPHER_CTX *ctx; //EVP_CIPHER_CTX_set_padding() ;

    int len;

    int plaintext_len;

    /* Create and initialise the context */
    if(!(ctx = EVP_CIPHER_CTX_new()))
    {
        printf("Error in EVP_CIPHER_CTX_new()\n");
        handleErrors();
    }

    /*
     * Initialise the decryption operation. IMPORTANT - ensure you use a key
     * and IV size appropriate for your cipher
     * In this example we are using 256 bit AES (i.e. a 256 bit key). The
     * IV size for *most* modes is the same as the block size. For AES this
     * is 128 bits
     */
    if(keylen==32)
        if(1 != EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv))
        {
            printf("Error in EVP_DecryptInit_ex\n");
            handleErrors();
        }
    else if(keylen==21)
        if(1 != EVP_DecryptInit_ex(ctx, EVP_des_ede3_cbc(), NULL, key, iv))
        {
            printf("Error in EVP_DecryptInit_ex\n");
            handleErrors();
        }        

    /*
     * Provide the message to be decrypted, and obtain the plaintext output.
     * EVP_DecryptUpdate can be called multiple times if necessary.
     */
    if(1 != EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len))
    {
        printf("Error in EVP_DecryptUpdate\n");
        handleErrors();
    }
    plaintext_len = len;

    /*
     * Finalise the decryption. Further plaintext bytes may be written at
     * this stage.
     */
    int len2;

    if(1 != EVP_DecryptFinal_ex(ctx, plaintext + len, &len2))
    {
        printf("Error in EVP_DecryptFinal_ex\n");
        handleErrors();
    }
    plaintext_len += len2;

    /* Clean up */
    EVP_CIPHER_CTX_free(ctx);

    return plaintext_len;
}

int main (void)
{
    /*
     * Set up the key and iv. Do I need to say to not hard code these in a
     * real application? :-)
     */

    /* A 256 bit key */
    unsigned char *key; //= (unsigned char *)"01234567890123456789012345678901";
    key=(char*)malloc(sizeof(char)*32);
    // for(int i=0;i<32;i++)
    // {
    //   int num=rand()%10;
    //   key[i]=num;
    // }


    /* A 128 bit IV */
    unsigned char *iv; //= (unsigned char *)"0123456789012345";
    iv=(char*)malloc(sizeof(char)*16);
    // for(int i=0;i<16;i++)
    // {
    //   int num=rand()%10;
    //   iv[i]=num;
    // }

    FILE *fptr; FILE* fptr2;
    fptr = fopen("session_key_RECV.txt","r");
    fptr2 = fopen("iv.txt","r");

    fscanf(fptr,"%s",key);
    fscanf(fptr2,"%s",iv);

    // for(int i=0;i<32;i++)
    // {
    //   fprintf(fptr,"%c",key[i]);
    // }
    // fprintf(fptr,"\n");

    // for(int i=0;i<16;i++)
    //   {
    //     fprintf(fptr,"%c",iv[i]);
    //   }    

    fclose(fptr);
    fclose(fptr2);

    printf("key: %s\n",key);
    printf("iv: %s\n",iv);

    /* Message to be encrypted */
    unsigned char *ciphertext; //= (unsigned char *)"The quick brown fox jumps over the lazy dog";
    unsigned char* temp;

    ciphertext=(char*)malloc(sizeof(char)*256);
    temp=(char*)malloc(sizeof(char)*256);

    fptr = fopen("session_key_encrypted_message_RECV","rb+");

    //fscanf(fptr,"%s\n",ciphertext);

    unsigned char c;         
    unsigned long  newline_count = 0;

        /* count the newline characters */
    int j=0;
    //do
    while(c!=EOF)
    {
        c=fgetc(fptr);    // STILL READING 50, though actual ciphertext len is 64
        if(c!=EOF&& (int)(c)!=255) //&& (int)(c)!=255)
        {
            ciphertext[j]=c;
            j++;
            printf("\n%c %d",c,c);
        }
        else if((int)(c)==255)
        {
            printf("\nC- %c %d",c,c);
            unsigned char c2=fgetc(fptr); 
            printf("\nC2- %c %d",c2,c2);
            if((int)(c2)!=255)
            {
               ciphertext[j]=c; j++; 
               ciphertext[j]=c2; j++; 
            }
            else
                break;
        }

    }
    
 

    fclose(fptr);

    //printf("ciphertext: %s\n",ciphertext);

    //printf("len(ciphertext):%d \n",strlen(ciphertext)); 


    /* Buffer for the decrypted text */
    unsigned char decryptedtext[128];

    int decryptedtext_len, ciphertext_len;
    //ciphertext_len=strlen(ciphertext);
    ciphertext_len=j;
    printf("\nj: %d, strlen(ciphertext): %zu\n",j,strlen(ciphertext));
    
    decryptedtext_len = decrypt(ciphertext, ciphertext_len, key, iv,
                               decryptedtext,strlen(key));

    /* Add a NULL terminator. We are expecting printable text */
    decryptedtext[decryptedtext_len] = '\0';

    /* Show the decrypted text */
    printf("Decrypted text is:\n");
    printf("%s\n", decryptedtext);

    FILE* f4;
    f4=fopen("decrypted_plaintext","w");
    fprintf(f4, "%s\n",decryptedtext );

    fclose(f4);

    return 0;
}