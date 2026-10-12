#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into digital pin 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire device
OneWire oneWire(ONE_WIRE_BUS);

// Pass oneWire reference to DallasTemperature library
DallasTemperature sensors(&oneWire);

int deviceCount = 0;
float tempC;
float analogPin2mFwd = A0;
float Fwd2m = 0.0;
float analogPin2mRev = A1;
float Rev2m = 0.0;
float analogPin6mFwd = A2;
float Fwd6m = 0.0;
float analogPin6mRev = A3;
float Rev6m = 0.0;

void setup(void) {
  sensors.begin();  // Start up the library
  Serial.begin(9600);

  // locate devices on the bus
  Serial.print("Locating devices...");
  Serial.print("Found ");
  deviceCount = sensors.getDeviceCount();
  Serial.print(deviceCount, DEC);
  Serial.println(" 1 wire temperature devices.");
  Serial.println("");
}

void loop(void) {
  // Send command to all the sensors for temperature conversion
  sensors.requestTemperatures();

  // Display temperature from each sensor
  for (int i = 0; i < deviceCount; i++) {
  //  Serial.print("T");
    Serial.print(i + 1);
    Serial.print(" : ");
    tempC = sensors.getTempCByIndex(i);
    Serial.print(tempC);
    Serial.print(" ");
 
  }

  float Fwd2m = analogRead(analogPin2mFwd) / 2.0;
  float Rev2m = analogRead(analogPin2mRev);
  float Fwd6m = analogRead(analogPin6mFwd);
  float Rev6m = analogRead(analogPin6mRev);
  Serial.print(" : ");
  Serial.print(Fwd2m);
  Serial.print(" : ");
  Serial.print(Rev2m);
  Serial.print(" : ");
  Serial.print(Fwd6m);
  Serial.print(" : ");
  Serial.print(Rev6m);
  Serial.println("");
  
  delay(100);
}
