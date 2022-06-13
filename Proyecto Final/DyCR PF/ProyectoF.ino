#include <string.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define RELE 2

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);

unsigned int pos0=172; // ancho de pulso en cuentas para posicion 0°
unsigned int pos180=565; // ancho de pulso en cuentas para la posicion 180°

void setup() {
  Serial.begin(9600);
  delay(30);
  pinMode(RELE, OUTPUT);
  digitalWrite(RELE,0);
  servos.begin();  
  servos.setPWMFreq(60); //Frecuecia PWM de 60Hz o T=16,66ms
}
void setServo(uint8_t n_servo, int angulo) {
  int duty;
  duty=map(angulo,0,180,pos0, pos180);
  servos.setPWM(n_servo, 0, duty);  
}
int poserv1=0;
int poserv2=0;
int poserv3=0;
int pos,pos2,pos3;
int relei;
String cad,Sserv1,Sserv2,Sserv3,reles;

void loop() {
  if(Serial.available()){
    cad = Serial.readString();
    pos = cad.indexOf(',');
    pos2 = cad.indexOf(',',pos+1);
    pos3 = cad.indexOf(',',pos2+1);
    Sserv1= cad.substring(0,pos);
    Sserv2= cad.substring(pos+1,pos2);
    Sserv3= cad.substring(pos2+1,pos3);
    reles= cad.substring(pos3+1);

    if(poserv1 != Sserv1.toInt()){
      poserv1 = Sserv1.toInt();
      setServo(0,poserv1);
      }

    if(poserv2 != Sserv2.toInt()){
      poserv2 = Sserv2.toInt();
      setServo(1,poserv2);
      }

    if(poserv3 != Sserv3.toInt()){
      poserv3 = Sserv3.toInt();
      setServo(2,poserv3);
      }
    
    if(relei != reles.toInt()){
      relei = reles.toInt();
      digitalWrite(RELE, relei);
      }
      
    }
    
}
