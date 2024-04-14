#include "DHT.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 14      // Set the pin connected to the DHT11 data pin
#define DHTTYPE DHT11  // DHT 11

DHT dht(DHTPIN, DHTTYPE);

// Initialize the LCD object with I2C address 0x27, 16 columns, and 2 rows
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // Begin serial communication at 115200 baud
  Serial.begin(115200);

  // Initialize the dht11
  dht.begin();

  // Initialize the LCD
  lcd.init();
  lcd.backlight();

  // Clear the LCD
  lcd.clear();
}

void loop() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (it's a very slow sensor)
  float humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float temperatureCelsius = dht.readTemperature();
  // Convert Celsius to Fahrenheit
  float temperatureFahrenheit = (temperatureCelsius * 9 / 5) + 32;

  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temperatureCelsius)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Get the current time and format it
  unsigned long currentMillis = millis();   // Get the current time
  unsigned long currentSeconds = currentMillis / 1000;
  int hours = currentSeconds / 3600;
  int minutes = (currentSeconds % 3600) / 60;
  int seconds = currentSeconds % 60;

  // Display temperature and humidity on the LCD
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperatureFahrenheit);
  lcd.write(223);  // Degree symbol
  lcd.print("F");

  lcd.setCursor(0, 1);
  lcd.print("Humi: ");
  lcd.print(humidity);
  lcd.print("%");

  // Serial output with timestamp
  Serial.print(hours);
  Serial.print(":");
  if (minutes < 10) {
    Serial.print("0");
  }
  Serial.print(minutes);
  Serial.print(":");
  if (seconds < 10) {
    Serial.print("0");
  }
  Serial.print(seconds);
  Serial.print(" ,");
  Serial.print(temperatureFahrenheit);
  Serial.print(",");
  Serial.println(humidity);

  delay(3000);  // Wait 3 seconds before reading again
}
