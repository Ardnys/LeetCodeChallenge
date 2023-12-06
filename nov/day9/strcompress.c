#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#define SIZE 14 

int compress(char* chars, int charsSize);
char* createCompressedStr(char current, int ctr);

int main() {
    char str[SIZE] = "aaaaaabbcdefgg";

    int compressedSize = compress(str, SIZE);

    printf("original: %s -> size: %d\n compressed: %s -> size: %d\n", str, SIZE, str, compressedSize);

    return 0;
}

char* createCompressedStr(char current, int ctr) {
    // printf("current: %c, next: %c, ctr: %d\n", current, next, ctr);

    char *compressedStr;
    int len = 0;

    if (ctr == 1) {
        compressedStr = &current;
    } else {
        len = snprintf(NULL, 0, "%d", ctr);
        compressedStr = (char*)malloc((size_t)len+2);
        assert(compressedStr != NULL);

        snprintf(compressedStr, len+2, "%c%d", current, ctr);
    }
    printf("compressed to: %s\nwith size: %d\n", compressedStr, len+2);

    return compressedStr;

}

int compress(char* chars, int charsSize) {
    if (charsSize == 0) {
        return 0;
    }
    int yetanothercounter = 0;
    int size = 0;
    int ctr = 1;
    for (int i = 0; i < charsSize-1; ++i) {
        char current = chars[i];
        char next = chars[i+1];

        if (current == next) {
            ++ctr;
            printf("current: %c, next: %c, ctr: %d\n", current, next, ctr);
            if (i == charsSize-2) {
                printf("this should be the last\n");
                char* compressedStr = createCompressedStr(current, ctr);
                // TODO figure out the indexes and take this out to a function 
                int start = i - ctr + 1;
                int len = i+1 - start;
                int strIdx = 0;
                printf("start: %d to: %d\n", yetanothercounter, len);

                for (int j = yetanothercounter; j < len; ++j) {
                    if (compressedStr[strIdx] == 0) {
                        printf("HOL UP!!! at %d\n", strIdx);
                    }
                       printf("old: %c -> new: %c at %d\n", chars[j], 
                                compressedStr[strIdx], j);
                        chars[j] = compressedStr[strIdx++];
                    
                }
                yetanothercounter += len;
                free(compressedStr);
                size += ctr;
                printf("edited arr: %s\n", chars);
            }
        } else {
            printf("------ char changed ------\n");

            char* compressedStr = createCompressedStr(current, ctr);

            int start = i - ctr + 1;


            int len = i+1 - start;
            int strIdx = 0;

            printf("start: %d to: %d\n", yetanothercounter, len);
            for (int j = yetanothercounter; j < len; ++j) {
                printf("old: %c -> new: %c at %d\n", chars[j],
                        compressedStr[strIdx], j);
                chars[j] = compressedStr[strIdx++];
            }

            yetanothercounter += len;
            printf("edited arr: %s\n", chars);
            size += ctr;

            ctr = 1;
        }
    }
    int uh = 0;
    for (int i = 0; i < charsSize; ++i) {
        if (chars[i] == NULL) {
            break;
        }
        // printf("c: %c\n", chars[i]);
        uh++;
    }
    return uh;
}
