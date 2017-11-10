#include <math.h>

int MAPA[4][5] = {
  
  {0, 1, 0, 1, 0},     //Read Coil 
  {1, 0, 1, 0, 1},   //Read Input
  {10, 20, 30, 40, 50},   //Read Holding Registers
  {1, 2, 3, 4, 5},     //Read Input Registers
 
};

int FILES = 0;
int COLUMNES = 0;

String comanda = ""; //variable on en guarda la comanda
boolean comanda_enviada = false; //s'activa quan s'envia la comanda (pulsació ENTER)

void setup() 
{
    FILES = sizeof(MAPA);
    COLUMNES = sizeof(MAPA[0]);

    Serial.begin(9600);  
    pinMode(13, OUTPUT);
}

void loop() 
{
  lectura_port_serie(); //lectura del que s'envia per port sèrie/usb a l'Arduino
  if (comanda_enviada == true)
  {
    //Serial.println(comanda);
    String resposta = Tractar_Trama(comanda);
    Serial.println(resposta);   //per a que la rebi el PC

    Actuadors();
    
    comanda = ""; //netejar les variables
    comanda_enviada = false;
  }
} 

String Tractar_Trama(String trama)
{    
    String funcio = trama.substring(2, 4);

    String s = "ERROR";

    if ((funcio == "01") || (funcio == "02"))
        s = Read_Coils_Discrete(trama);
    
    if ((funcio == "03") || (funcio == "04"))
        s = Read_Holdings_Input_Registers(trama);

    if (funcio == "05")
        s = Write_Coils(trama);

    if (funcio == "06")
        s = Write_Holdings_Registers(trama);             

    return s;
}

void Actuadors()
{
  /*if (MAPA[2][0] >= 100)
      digitalWrite(13, HIGH);
  if (MAPA[2][0] < 100)
      digitalWrite(13, LOW);*/
      
  digitalWrite(13, MAPA[0][0]);   //coil 0
}

void lectura_port_serie()
{
  while (Serial.available() > 0)
  {
    char inChar = (char)Serial.read();
    comanda += inChar;
    if (inChar == '\n')  //detecta ENTER
    {
      comanda_enviada = true;
      comanda.replace("\n","");
    }
  }
}



