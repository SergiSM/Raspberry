String Read_Holdings_Input_Registers(String trama)
{
    String s = "ERROR";
    if (trama.length() == 12)   //all the request have 12 bytes (slave(2) function(2) offset(4) n_registers(4)) 11 04 0008 0001 B298 (in this case I omit CRC)
    {
      int funcio = trama.substring(2, 4).toInt() - 1;
      int offset = trama.substring(4, 8).toInt();
      int n_registres = trama.substring(8, 12).toInt();
  
      String n_bytes = Zeros( String((n_registres * 2), HEX), 2);                       
      s = trama.substring(0, 4) + n_bytes;            
  
      if (n_registres < COLUMNES)
      {
          for (int i = 0; i < n_registres; i++)
          {
            int aux = MAPA[funcio][offset + i];
            s += Zeros(String(aux, HEX), 2);                    
          }
      }
      else
          s = "ERROR";
    }
    
    return s;
}

String Read_Coils_Discrete(String trama)
{
  String s = "ERROR";
  if (trama.length() == 12)
  {
    int funcio = trama.substring(2, 4).toInt() - 1;
    int offset = trama.substring(4, 8).toInt();
    String n_registres_hex = trama.substring(8, 12);  
    int n_registres = HexToInt(string2char(n_registres_hex)); //hex a int
  
    int n_bytes = ceil((double)n_registres / 8);
  
    s = trama.substring(0, 4) + Zeros(String(n_bytes, HEX), 2);
  
    //llista amb tots els bits demanats
    String bits = "";            
    for (int i = offset; i < n_registres; i++)
        bits = String(MAPA[funcio][i]) + bits;
  
    bits = Zeros(bits, 8); 
  
    //fer n_bytes paquets de 8 bits amb la llista de bits demanats
    for (int i = 0; i < n_bytes; i++)
    {
        bits = Zeros(bits, 8);    //ensure that bits is at least 8 bits long
        String aux = bits.substring(bits.length() - 8, bits.length());   //take last 8 characters/bits                
        bits = bits.substring(0, bits.length() - 8);      //remove last 8 bits for the next iteration           
        int aux2 = strtol(string2char(aux), (char**) NULL, 2);       //binary to integer
        String hex = Zeros(String(aux2, HEX), 2);               //integer to hexadecimal (2 bytes)
        s += hex;
    }
  }

  return s;
}

String Write_Holdings_Registers(String trama)
{     
    if (trama.length() == 12)
    {
      int offset = trama.substring(4, 8).toInt();            
      String valor = trama.substring(8, 12); //en hexa
       
      MAPA[2][offset] = HexToInt(string2char(valor));  //2 = row holdings                      
  
      return trama; 
    }  
    else
       return "ERROR";
}

String Write_Coils(String trama)
{
    if (trama.length() == 12)
    {
      int offset = trama.substring(4, 8).toInt();
      String valor = trama.substring(8, 12);
      valor.toUpperCase();  //no retorna res, per tant no assigno a variable
      
      if (valor == "FF00")
          MAPA[0][offset] = 1;     //0 = row coils
      else
          MAPA[0][offset] = 0;
      
      return trama;
    }  
    else
       return "ERROR";
}
