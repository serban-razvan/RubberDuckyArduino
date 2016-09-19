#include "Keyboard.h"
#include "extern.h"



void setup() {
  pinMode(9, INPUT_PULLUP);
  Keyboard.begin();
  //Serial.begin(9600);
}

int status=0;


void loop() {
  //Serial.println(digitalRead(9));
  if (digitalRead(9)==LOW){
    if (status==0){
      status=1;
      //@@@@@@@@@@@@@@@@@ PAYLOAD FROM FILE extern.h
      FUNCTIE();
      //@@@@@@@@@@@@@@@@@ END PAYLOAD
    }
  }
  else{
    status=0;
  }
  delay(10);
}
