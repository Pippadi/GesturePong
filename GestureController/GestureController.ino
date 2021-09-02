#include <LSM303AGR_ACC_Sensor.h>
//#include <LSM303AGR_MAG_Sensor.h>

LSM303AGR_ACC_Sensor acc(&Wire);
//LSM303AGR_MAG_Sensor mag(&Wire);

void setup() {
  Serial.begin(9600);
  Wire.begin();
  acc.begin();
  acc.Enable();
  //mag.begin();
  //mag.Enable();
}

void loop() {
  int32_t accelVals[3];
  acc.GetAxes(accelVals);
  Serial.print(accelVals[2] / 100);
  Serial.print('\n');
  delay(10);
}
