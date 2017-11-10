// Compute the MODBUS RTU CRC
String ModRTU_CRC(String raw_msg_data) {
  //Calc raw_msg_data length
  byte raw_msg_data_byte[raw_msg_data.length()/2];
  //Convert the raw_msg_data to a byte array raw_msg_data
  for (int i = 0; i < raw_msg_data.length() / 2; i++) {
    raw_msg_data_byte[i] = StrtoByte(raw_msg_data.substring(2 * i, 2 * i + 2));
  }

  //Calc the raw_msg_data_byte CRC code
  uint16_t crc = 0xFFFF;
  String crc_string = "";
  for (int pos = 0; pos < raw_msg_data.length()/2; pos++) {
    crc ^= (uint16_t)raw_msg_data_byte[pos];          // XOR byte into least sig. byte of crc
    for (int i = 8; i != 0; i--) {    // Loop over each bit
      if ((crc & 0x0001) != 0) {      // If the LSB is set
        crc >>= 1;                    // Shift right and XOR 0xA001
        crc ^= 0xA001;
      }
      else                            // Else LSB is not set
        crc >>= 1;                    // Just shift right
    }
  }
  // Note, this number has low and high bytes swapped, so use it accordingly (or swap bytes)

  //Become crc byte to a capital letter String 
  crc_string = String(crc, HEX);
  crc_string.toUpperCase();
  
  //The crc should be like XXYY. Add zeros if need it
  if(crc_string.length() == 1){
    crc_string = "000" + crc_string;
  }else if(crc_string.length() == 2){
    crc_string = "00" + crc_string;
  }else if(crc_string.length() == 3){
    crc_string = "0" + crc_string;
  }else{
    //OK
  }

  //Invert the byte positions
  crc_string = crc_string.substring(2, 4) + crc_string.substring(0, 2);
  return crc_string;  
}

//String to byte --> Example: String = "C4" --> byte = {0xC4}
byte StrtoByte (String str_value){
  char char_buff[3];
  str_value.toCharArray(char_buff, 3);
  byte byte_value = strtoul(char_buff, NULL, 16);
  return byte_value;  
}
