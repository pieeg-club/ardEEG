#include <WiFi.h>
#include <WiFiUdp.h>
#include <SPI.h>

// =====================
// PIN DEFINITIONS
// =====================
const int button_pin  = 7;     // Button pin (HIGH -> LOW on press)
const int chip_select = 10;    // SPI CS pin
const int test_DRDY   = 5;

// =====================
// DATA BUFFER
// =====================
const int size_of_data = 675;
byte output[size_of_data];
int sc = 0;

// =====================
// WIFI SETTINGS
// =====================
char ssid[] = "your Wi-Fi";
char pass[] = "your Password";
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
  pinMode(button_pin, INPUT_PULLUP);  // HIGH = released, LOW = pressed
  pinMode(chip_select, OUTPUT);
  digitalWrite(chip_select, HIGH);

  // ---------- SPI ----------
  SPI.begin();
  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE1));

  sendCommand(0x02); // wakeup
  sendCommand(0x0A); // stop
  sendCommand(0x06); // reset
  sendCommand(0x11); // sdatac

  // ---------- ADC CONFIG ----------
  writeByte(0x01, 0x96);
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

  sendCommand(0x10); // start
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

  // Falling edge: HIGH -> LOW
  if (lastButtonState == HIGH && currentButtonState == LOW)
  {
    captureEnabled = !captureEnabled; // toggle capture
    sc = 0;                            // reset buffer
  }

  lastButtonState = currentButtonState;

  // ---------- DATA CAPTURE ----------
  if (captureEnabled)
  {
    for (int i = 0; i < 27; i++)
    {
      output[sc++] = SPI.transfer(0xFF);
    }

    // ---------- SEND UDP ----------
    if (sc >= size_of_data)
    {
      udp.beginPacket("192.168.1.241", 13900);  // replace for your ip 192.168.1.241"
      udp.write(output, size_of_data);
      udp.endPacket();
      sc = 0;
    }
  }
}
