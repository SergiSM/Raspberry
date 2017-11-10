String Zeros(String v, int n_digits) 
{
    int n_zeros = n_digits - v.length();
    String s = v;
    for (int i=0; i < n_zeros; i++)
    {
          s = "0" + s;
    }
    return s;
}

int HexToInt(char str[])
{
  return (int) strtol(str, 0, 16);
}

char* string2char(String command){
    if(command.length()!=0){
        char *p = const_cast<char*>(command.c_str());
        return p;
    }
}
