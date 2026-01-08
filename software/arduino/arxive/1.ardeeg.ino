#include <WiFi.h>
#include <WiFiUdp.h>
#include <SPI.h>

// =====================
// PIN DEFINITIONS
// =====================
const int button_pin  = 7;
const int chip_select = 10;
const int DRDY_pin    = 5;  // CRITICAL: Must monitor this!

// =====================
// DATA BUFFER
// =====================
const int size_of_data = 675;  // 27 bytes × 25 samples
byte output[size_of_data];
int sc = 0;

// =====================
// WIFI SETTINGS




char ssid[] = "BT-P7CPQC";
char pass[] = "CRQuTXGfkf4g3a";


WiFiUDP udp;

// =====================
// BUTTON STATE
// =====================
int lastButtonState = HIGH;
bool captureEnabled = false;

// =====================
// SPI HELPERS
// =====================
void sendCommand(byte command)
{
  digitalWrite(chip_select, LOW);
  SPI.transfer(command);
  digitalWrite(chip_select, HIGH);
}

void writeByte(byte reg, byte data)
{
  byte tx[3];
  tx[0] = 0x40 | reg;
  tx[1] = 0x00;
  tx[2] = data;

  digitalWrite(chip_select, LOW);
  SPI.transfer(tx, 3);
  digitalWrite(chip_select, HIGH);
}

// =====================
// SETUP
// =====================
void setup()
{
  // ---------- PINS ----------
  pinMode(button_pin, INPUT_PULLUP);
  pinMode(chip_select, OUTPUT);
  pinMode(DRDY_pin, INPUT);  // ADDED: Configure DRDY as input
  digitalWrite(chip_select, HIGH);

  // ---------- SPI ----------
  SPI.begin();
  SPI.beginTransaction(SPISettings(4000000, MSBFIRST, SPI_MODE1)); // Increased to 4MHz

  sendCommand(0x02); // wakeup
  delay(1);
  sendCommand(0x0A); // stop
  sendCommand(0x06); // reset
  delay(1);
  sendCommand(0x11); // sdatac

  // ---------- ADC CONFIG ----------
  writeByte(0x01, 0x96);  // 250 SPS (0x96), verify this matches your desired rate
  writeByte(0x02, 0xD4);
  writeByte(0x03, 0xFF);
  writeByte(0x04, 0x00);
  writeByte(0x0D, 0x00);
  writeByte(0x0E, 0x00);
  writeByte(0x0F, 0x00);
  writeByte(0x10, 0x00);
  writeByte(0x11, 0x00);
  writeByte(0x15, 0x20);
  writeByte(0x17, 0x00);
  writeByte(0x05, 0x00);
  writeByte(0x06, 0x00);
  writeByte(0x07, 0x00);
  writeByte(0x08, 0x00);
  writeByte(0x09, 0x00);
  writeByte(0x0A, 0x00);
  writeByte(0x0B, 0x00);
  writeByte(0x0C, 0x00);
  writeByte(0x14, 0x80);

  delay(1);
  sendCommand(0x10); // start
  delay(1);
  sendCommand(0x08); // rdatac

  // ---------- WIFI ----------
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
  }

  udp.begin(13900);
}

// =====================
// LOOP
// =====================
void loop()
{
  // ---------- BUTTON EDGE DETECTION ----------
  int currentButtonState = digitalRead(button_pin);

  if (lastButtonState == HIGH && currentButtonState == LOW)
  {
    captureEnabled = !captureEnabled;
    sc = 0;
  }

  lastButtonState = currentButtonState;

  // ---------- DATA CAPTURE ----------
  if (captureEnabled)
  {
    // CRITICAL FIX: Wait for DRDY to go LOW (new data ready)
    if (digitalRead(DRDY_pin) == LOW)
    {
      // Read one complete sample (27 bytes: 3 status + 8 channels × 3 bytes)
      digitalWrite(chip_select, LOW);
      for (int i = 0; i < 27; i++)
      {
        output[sc++] = SPI.transfer(0xFF);
      }
      digitalWrite(chip_select, HIGH);

      // ---------- SEND UDP ----------
      if (sc >= size_of_data)
      {
        udp.beginPacket("192.168.1.241", 13900);
        udp.write(output, size_of_data);
        udp.endPacket();
        sc = 0;
      }
    }
  }
}
