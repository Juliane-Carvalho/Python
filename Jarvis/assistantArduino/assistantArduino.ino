String inputString = "";  // a string to hold incoming data
bool stringComplete = false;  // wheter the string is complete

#define pinoLampada 8

void setup() {
  // initialize serial:
  Serial.begin(115200);
  //reverse 200 bytes for the inputString:
  inputString.reserve(200);

  pinMode(pinoLampada, OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  if(stringComplete){
    //clear the string:
    if(inputString.startsWith("ligar")){
      //digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      digitalWrite(pinoLampada, HIGH);
      Serial.print("Assistant Called. Lights On.: ");
    }else if(inputString.startsWith("desligar")){
      digitalWrite(pinoLampada, LOW);
      Serial.print("Assistant Called. Lights Off.");
      }
      inputString = "";
      stringComplete = false;
    }
}

void serialEvent(){
  while(Serial.available()){
    //get the new byte:
    char inChar = (char)Serial.read();
    //add it to the inputString:
    inputString += inChar;
    //if the incoming character is a newline, get a flag so the main loop can
    //do something about it
    if(inChar == '\n'){
      stringComplete = true;
      }
    }
  }
