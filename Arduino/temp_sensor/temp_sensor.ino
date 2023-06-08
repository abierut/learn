const int sensorPin = A0;
const float baselineTemp = 24.0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int pinNum = 2; pinNum <5; pinNum++){
    pinMode(pinNum, OUTPUT);
    digitalWrite(pinNum, LOW);
    }
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensVal = analogRead(sensorPin);
  Serial.print("Sensor Value: ");
  Serial.print(sensVal);
  float voltage  = (sensVal/1024.0)*5.0;
  Serial.print(". Volts: ");
  Serial.print(voltage);
  float temp = (voltage - 0.5)*100;
  Serial.print(". Temperature: ");
  Serial.print(temp);
  Serial.println();

  if(temp < baselineTemp+2){
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
  }else if(temp >= baselineTemp+2 && temp < baselineTemp+4){
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,LOW);
  }else if(temp >= baselineTemp+4 && temp < baselineTemp+6){
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
  }else if(temp >= baselineTemp+6) {
    digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
    digitalWrite(4,HIGH);
  }
  delay(1);
}
