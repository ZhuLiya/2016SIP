#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void setup() {
  servoLeft.attach(12); //pin number
  servoRight.attach(11); 
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);  
}
void loop() {
  turnright();
  delay(300);
  turnleft();
  delay(300);
  turnleft();
  delay(250);
  
}

void stopmove(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);  
}


void forward(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);  
}

void backward(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}

void turnright(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
}

void turnleft(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
}




