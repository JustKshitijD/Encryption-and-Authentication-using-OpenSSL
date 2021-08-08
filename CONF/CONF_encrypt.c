#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>

void handleErrors(void)
{
    ERR_print_errors_fp(stderr);
    abort();
}

int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
            unsigned char *iv, unsigned char *ciphertext, int keylen)
{
    EVP_CIPHER_CTX *ctx; //EVP_CIPHER_CTX_set_padding() ;

    int len;

    int ciphertext_len;

    /* Create and initialise the context */
    if(!(ctx = EVP_CIPHER_CTX_new()))
    {
        printf("NEW ERROR\n");
        handleErrors();
    }

    printf("keylen: %d\n",keylen);
    printf("key: %s\n",key);
    printf("iv: %s\n", iv);
    /*
     * Initialise the encryption operation. IMPORTANT - ensure you use a key
     * and IV size appropriate for your cipher
     * In this example we are using 256 bit AES (i.e. a 256 bit key). The
     * IV size for *most* modes is the same as the block size. For AES this
     * is 128 bits
     */
    if(keylen==32)
        if(1 != EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv))
            handleErrors();
    else if(keylen==21)
        if(1 != EVP_EncryptInit_ex(ctx, EVP_des_ede3_cbc(), NULL, key, iv))
        {
            printf("DES issue!\n");
            handleErrors();    
        }

    /*
     * Provide the message to be encrypted, and obtain the encrypted output.
     * EVP_EncryptUpdate can be called multiple times if necessary
     */
     printf("1\n");   
    if(1 != EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len))
    {
        printf("Update issue!\n");
        handleErrors();
    }

    printf("2\n");
    ciphertext_len = len;

    /*
     * Finalise the encryption. Further ciphertext bytes may be written at
     * this stage.
     */
    if(1 != EVP_EncryptFinal_ex(ctx, ciphertext + len, &len))
    {
        printf("final issue\n");
        handleErrors();
    }
    ciphertext_len += len;

    /* Clean up */
    EVP_CIPHER_CTX_free(ctx);

    return ciphertext_len;
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
    fptr = fopen("session_key.txt","r");
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
    unsigned char *plaintext; //= (unsigned char *)"The quick brown fox jumps over the lazy dog";
    plaintext=(char*)malloc(sizeof(char)*60);

    fptr = fopen("plaintext","r");

    fscanf(fptr,"%s",plaintext);
    printf("plaintext: %s\n",plaintext);

    printf("len(plaintext):%zu \n",strlen(plaintext));  

    fclose(fptr);

    /*
     * Buffer for ciphertext. Ensure the buffer is long enough for the
     * ciphertext which may be longer than the plaintext, depending on the
     * algorithm and mode.
     */
    unsigned char ciphertext[128]; int ciphertext_len;

    

    /* Encrypt the plaintext */
    ciphertext_len = encrypt (plaintext, strlen ((char *)plaintext), key, iv,
                              ciphertext,strlen(key));

    /* Do something useful with the ciphertext here */
    printf("Ciphertext is:\n");
    //BIO_dump_fp (stdout, (const char *)ciphertext, ciphertext_len);

    ciphertext[ciphertext_len]='\0';
    printf("ciphertext: %s\n",ciphertext);
    printf("ciphertext in ASCII: \n");
    // for(int i=0;i<ciphertext_len;i++)
    // {
    //   printf("ciphertext[%d]: %c  %d\n",i,ciphertext[i],ciphertext[i]);
    // }
    printf("\n");
    printf("ciphertext_len: %zu = %d\n",strlen(ciphertext),ciphertext_len);

    /* Decrypt the ciphertext */
    

    FILE* fptr3;
    fptr3 = fopen("session_key_encrypted_message","w");
    int z=0;

    int flag=0;

    do{
        if(flag!=0)
        {
            fputc('\0',fptr3);
            //fprintf(fptr3, '%c',ciphertext+z);
            ciphertext[z]='\0';
            z++;
        }

        int y=fprintf(fptr3, "%s",ciphertext+z);
        printf("y: %d\n",y );
        printf("z: %d\n",z);
        printf("strlen(ciphertext): %zu\n",strlen(ciphertext));
        printf("ciphertext_len: %d\n",ciphertext_len);
        for(int i=0;i<ciphertext_len;i++)
        {
          printf("ciphertext[%d]: %c  %d\n",i,ciphertext[i],ciphertext[i]);
        }
        z+=y;
        //ciphertext[z]='\0';
        printf("\n");
        flag=1;
        //z++;

    }while(z!=ciphertext_len);


    fclose(fptr3);

    printf("Encryption successful!!\n");

    //decryptedtext_len = decrypt(ciphertext, ciphertext_len, key, iv,
    //                            decryptedtext);

    /* Add a NULL terminator. We are expecting printable text */
    //decryptedtext[decryptedtext_len] = '\0';

    /* Show the decrypted text */
    //printf("Decrypted text is:\n");
    //printf("%s\n", decryptedtext);


    return 0;
}