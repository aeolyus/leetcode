char* toLowerCase(char* str) {
    char* res = calloc(80, sizeof(char));
    char* ptr = res;
    while (*str) {
        if ('A' <=*str && *str<= 'Z') {
            *ptr = *str + 'a' - 'A';
        } else {
            *ptr = *str;
        }
        str++;
        ptr++;
    }
    return res;
}
