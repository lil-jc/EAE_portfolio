#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }

    //allocate buffer with 512 bytes to read to
    BYTE buffer[512];
    //count the number of jpeg & make a file for them
    int jpeg_num = -1;
    char jpeg_files [sizeof(file)];
    FILE *written_jpeg;

    //loop through the whole deleted card
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        //check if its the start of jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            jpeg_num++;
            //check if its the first jpeg
            if (jpeg_num == 0)
            {
                sprintf(jpeg_files, "%03i.jpg", jpeg_num);
                written_jpeg = fopen(jpeg_files, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, written_jpeg);
            }
            //else close the previous file and open new file for new jpeg
            else
            {
                fclose(written_jpeg);
                sprintf(jpeg_files, "%03i.jpg", jpeg_num);
                written_jpeg = fopen(jpeg_files, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, written_jpeg);
            }
        }
        //if not the start of jpeg then continue to write data
        else
        {
            if (!(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff))
            {
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, written_jpeg);
            }
        }
    }
    //close all file
    fclose(written_jpeg);
    fclose(file);
}