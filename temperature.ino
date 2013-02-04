int temperaturePin = 0;

void setup(){
 Serial.begin(9600); 
}

void loop(){
 float temperature = getVoltage(temperaturePin);

temperature = (((temperature - .5) * 100) * 1.8) +32;

Serial.println(temperature);
delay(100);
}

float getVoltage(int pin){
  return (analogRead(pin) * .004882814);
}