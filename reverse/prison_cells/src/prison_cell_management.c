#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <curl/curl.h>
#include <sys/ptrace.h>

// INFO : Commande pour compiler : `gcc -s -o prison_cell_management prison_cell_management.c -lcurl -masm=intel`

// #define DEBUG 1

const char* server_url = "http://localhost:1337/"; // TODO : CHANGER POUR PROD LORSQUE DOCKER DISPONIBLE
unsigned char url_path[] = "\x88\x95\xa0\x56\xad\x8a\x2a\x57\xe5\x6a\xe7\x60\x13\xeb\xde\x5b\xaf\xa3\x43\x06\xe0\x0c\xc7\xdf\x48\x1b\x06\xab\x73\x3b\xa5\xcf\x5b\x81\xf1\x94\x41\xb5\x9a\x8e\x62";
unsigned char initial_greeting_text[] = "\x53\x61\x68\x67\x6b\x69\x61\x24\x66\x65\x67\x6f\x28\x24\x40\x65\x72\x61\x7d\x2a\x24\x53\x61\x24\x73\x61\x76\x61\x24\x73\x65\x6d\x70\x6d\x6a\x63\x24\x62\x6b\x76\x24\x7d\x6b\x71\x2a\x24\x4c\x71\x76\x76\x7d\x24\x71\x74\x24\x6a\x6b\x73\x28\x24\x70\x6c\x61\x24\x66\x6b\x77\x77\x24\x6c\x65\x77\x24\x77\x74\x61\x6a\x70\x24\x61\x6a\x6b\x71\x63\x6c\x24\x69\x6b\x6a\x61\x7d\x24\x6b\x6a\x24\x63\x61\x70\x70\x6d\x6a\x63\x24\x7d\x6b\x71\x24\x6b\x71\x70\x2a";
unsigned char first_check_text[] = "\x02\x35\x34\x60\x26\x29\x32\x33\x34\x60\x30\x32\x2f\x36\x25\x60\x2d\x25\x60\x39\x2f\x35\x67\x32\x25\x60\x21\x23\x34\x35\x21\x2c\x2c\x39\x60\x04\x21\x36\x25\x39\x7a\x60";
unsigned char last_check_text[] = "\x48\x65\x7b\x60\x6e\x61\x7d\x25\x29\x66\x62\x68\x70\x25\x29\x7d\x61\x68\x7d\x2e\x7a\x29\x6e\x66\x66\x6d\x27\x29\x4b\x7c\x7d\x25\x29\x70\x66\x7c\x29\x7a\x7d\x60\x65\x65\x29\x6a\x66\x7c\x65\x6d\x29\x61\x68\x7f\x6c\x29\x6e\x7c\x6c\x7a\x7a\x6c\x6d\x29\x7d\x61\x6c\x29\x79\x68\x7a\x7a\x7e\x66\x7b\x6d\x27\x29\x45\x68\x7a\x7d\x29\x6a\x61\x6c\x6a\x62\x33\x29\x7d\x61\x6c\x29\x7b\x6c\x68\x65\x29\x4d\x68\x7f\x6c\x70\x29\x7e\x66\x7c\x65\x6d\x29\x6b\x6c\x29\x68\x6b\x65\x6c\x29\x7d\x66\x29\x7b\x6c\x7d\x7b\x6c\x60\x7f\x6c\x29\x7d\x61\x6c\x29\x6f\x65\x68\x6e\x29\x7e\x6c\x29\x7a\x6c\x67\x7d\x27";
char server_response_buffer[255];

void xorEncrypt(char *password, size_t length, char key) {
    for (size_t i = 0; i < length; ++i) {
        password[i] ^= key;
    }
}

void prevent_debug() {
    pid_t ppid = getppid();

    char procPath[256];
    snprintf(procPath, sizeof(procPath), "/proc/%d/cmdline", ppid);
    FILE *procFile = fopen(procPath, "r");

    if (procFile == NULL) {
        return;
    }

    char processName[256];
    if (fscanf(procFile, "%255s", processName) != 1) {
        fclose(procFile);
        return;
    }

    fclose(procFile);

    if (strcmp(processName, "gdb") == 0) {
        exit(99);
    }
}

int check() {
    // Correct password is XUQWeHDQaCbBZZcQ
    char intendedPassword[] = "\x51\x5c\x58\x5e\x6c\x41\x4d\x58\x68\x4a\x6b\x4b\x53\x53\x6a\x58\0";

    int password_length = 16;
    char xorKey1 = 0x40;
    xorEncrypt(first_check_text, strlen(first_check_text), xorKey1);
    printf("%s", first_check_text);
    char enteredPassword[password_length + 1];
    fgets(enteredPassword, sizeof(enteredPassword), stdin);

    size_t len = strlen(enteredPassword);
    if (len > 0 && enteredPassword[len - 1] == '\n') {
        enteredPassword[len - 1] = '\0';
    }

    char xorKey2 = 0x09;
    xorEncrypt(enteredPassword, strlen(enteredPassword), xorKey2);

    char* enteredPasswordTmp = enteredPassword;
    char* intendedPasswordTmp = intendedPassword;
    while (*enteredPasswordTmp != '\0' && *intendedPasswordTmp != '\0') {
        if (*enteredPasswordTmp != *intendedPasswordTmp) {
            return 0;
        }
        enteredPasswordTmp++;
        intendedPasswordTmp++;
    }

    return (*enteredPasswordTmp == '\0' && *intendedPasswordTmp == '\0');
}

void swap(unsigned char * a, unsigned char * b) {
  unsigned char temp = * a;* a = * b;* b = temp;
};
void rc4Cipher(unsigned char * input, int length, unsigned char * key, int key_length) {
  unsigned char S[(0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)];
  int i, j = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00), k;
  for (i = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);
    (i < (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)) & !!(i < (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)); i++) {
    S[i] = i;
  };
  for (i = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);
    (i < (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)) & !!(i < (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)); i++) {
    j = (j + S[i] + key[i % key_length]) % (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00);
    swap( & S[i], & S[j]);
  };
  i = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);
  j = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);
  for (k = (0x0000000000000000 + 0x0000000000000200 + 0x0000000000000800 - 0x0000000000000A00);
    (k < length) & !!(k < length); k++) {
    i = (i + (0x0000000000000002 + 0x0000000000000201 + 0x0000000000000801 - 0x0000000000000A03)) % (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00);
    j = (j + S[i]) % (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00);
    swap( & S[i], & S[j]);
    unsigned char keystream = S[(S[i] + S[j]) % (0x0000000000000200 + 0x0000000000000300 + 0x0000000000000900 - 0x0000000000000D00)];
    input[k] ^= keystream;
  };
};

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    size_t realsize = size * nmemb;
    char* data = (char*)contents;

    
    char xorKey = 0x09;
    xorEncrypt(last_check_text, strlen(last_check_text), xorKey);

    printf("%s\n", last_check_text);

    int i;
    for (i = 0; i < 254; i++) {
        server_response_buffer[i] = data[i];
    }
    server_response_buffer[i+1] = '\0';

    #ifdef DEBUG
    printf("%s", server_response_buffer);
    #endif

    return realsize;
}

void performHttpGet(const char* url) {
    prevent_debug();
    if (!check()) {
        return;
    }
    prevent_debug();

    CURL* curl;
    CURLcode res;

    curl = curl_easy_init();

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            printf("Error: %s\n", curl_easy_strerror(res));
        }

        curl_easy_cleanup(curl);
    }
}

void get_flag() {
    unsigned char key[] = "flag";
    int key_length = strlen(key);
    int url_path_length = strlen(url_path);
    int server_url_length = strlen(server_url);

    rc4Cipher(url_path, url_path_length, key, key_length);

    #ifdef DEBUG
    printf("decrypted_url is %s\n", url_path);
    #endif

    char *complete_url = (char *)malloc(url_path_length + server_url_length + 1);

    int i;
    for (i = 0; i < server_url_length; i++) {
        complete_url[i] = server_url[i];
    }

    for (int j = 0; j < url_path_length; j++) {
        complete_url[i + j] = url_path[j];
    }

    #ifdef DEBUG
    printf("complete url is %s\n", complete_url);
    #endif

    performHttpGet(complete_url);
}

void print_state_of_cells(unsigned char* prison_cells) {
    printf("----------------------------\nCURRENT STATE OF CELLS\n");
    char* state = "";
    for (int i = 0; i < 32; i++) {
        if (prison_cells[i] == 1) {
            state = "open";
        } else {
            state = "closed";
        }
        printf("Cell %d is %s\n", i, state);
    }
    printf("\n");
}

int main(int argc, char **argv) {
    prevent_debug();

    printf("\n██   ██ ██ ██    ██ ███████ ██   ██ ███████ ██   ██\n");
    printf("██   ██ ██ ██    ██ ██      ██   ██ ██       ██ ██ \n");
    printf("███████ ██ ██    ██ █████   ███████ █████     ███  \n");
    printf("██   ██ ██  ██  ██  ██      ██   ██ ██       ██ ██ \n");
    printf("██   ██ ██   ████   ███████ ██   ██ ███████ ██   ██\n");

    printf("\nHIVEHEX PENITENTIARY'S CELLS MANAGEMENT SYSTEM\n");

    unsigned char prison_cells[32] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    while (1) {
        print_state_of_cells(prison_cells);
        printf("Enter a cell to open/close: ");
        char cell_number[8];
        fgets(cell_number, sizeof(cell_number), stdin);

        if (strcmp(cell_number, "flag\n") == 0) {
            char xorKey = 0x04;

            xorEncrypt(initial_greeting_text, strlen(initial_greeting_text), xorKey);
            printf("\n%s\n", initial_greeting_text);

            get_flag();
            return 0;
        }

        int cell_number_int = atoi(cell_number);
        if (0 <= cell_number_int && cell_number_int < 32) {
            int current_state = prison_cells[cell_number_int];
            if (current_state == 1) {
                prison_cells[cell_number_int] = 0;
            } else {
                prison_cells[cell_number_int] = 1;
            }
        }
    }

    return 0;
}
