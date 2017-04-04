
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Pixels {
    int r; 
    int g;
    int b;
} Pixel;

long okno(int x, int y, int n, int visina, int sirina, Pixel **t) {
    long sumR = 0, sumG = 0, sumB = 0;
    
    for(int i = x; i <= x + (n-1); i++) {
        for(int j = y; j <= y + (n-1); j++) {
            sumR += t[i][j].r;
            sumG += t[i][j].g;
            sumB += t[i][j].b;
        }
    }
    
    return (sumR + sumG + sumB)/(3 * (n * n));
}

int main(){

    FILE *file, *dest;
    int n;
    char vhodna[100000], izhodna[100000];
    scanf("%s %s %d", vhodna, izhodna, &n);
    
    file = fopen(vhodna, "rb");
    dest = fopen(izhodna, "w");
    
    if(file == NULL) return 0;
    
    int sirina, visina;
    fscanf(file, "P6 %d %d 255\n", &sirina, &visina);
    char Z[] = {' ', '.', '\'', ':',  'o', '&', '8', '#', '@'};
    int	 S[] = {230, 200, 180, 160, 130, 100, 70 , 50};
    
    Pixel **tab = malloc(visina * sizeof(Pixel*));
    for(int i = 0; i < visina; i++) tab[i] = malloc(sirina * sizeof(Pixel));
    
    for(int i = 0; i < visina; i++) {
        for(int j = 0; j < sirina; j++) {
            tab[i][j].r = fgetc(file);
            tab[i][j].g = fgetc(file);
            tab[i][j].b = fgetc(file);
        }
    }
    
    for(int i = 0; i < visina; i += n) {
        for(int j = 0; j < sirina; j += n) {
            long sivina = okno(i, j, n, visina, sirina, tab);
            if(sivina >= 50) {
                for(int i = 0; i < 8; i++) {
                    if(sivina >= S[i]) {
                        fprintf(dest, "%c", Z[i]);
                        break;
                    }
                }
            } else {
                fprintf(dest, "%c", Z[8]);
            }
        }
        fprintf(dest, "\n");
    }
    
    for(int i = 0; i < visina; i++) free(tab[i]);
    free(tab);
    
    fclose(file);
    fclose(dest);
    
    return 0;
}
