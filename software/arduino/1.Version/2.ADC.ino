#include <SPI.h>
const int button_pin = 26;
const int chip_select = 10; // Assuming SPI chip select pin
int test_DRDY = 5; 


void setup() {

  Serial.begin(9600);
  //pinMode(button_pin, INPUT);
  pinMode(chip_select, OUTPUT);
  //pinMode(reset_pin, OUTPUT);
  //pinMode(start_pin, OUTPUT);

  digitalWrite(chip_select, LOW);
  //digitalWrite(reset_pin, LOW);
  //digitalWrite(start_pin, LOW);

  SPI.begin();
  SPI.beginTransaction(SPISettings(600000, MSBFIRST, SPI_MODE1)); // Assuming 1 MHz SPI clock



    // Send commands
  sendCommand(0x02); // wakeup
  sendCommand(0x0A); // stop
  sendCommand(0x06); // reset
  sendCommand(0x11); // sdatac

  // Write configurations
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

  sendCommand(0x10); // rdatac
  sendCommand(0x08); // start

}

void loop() {


}


void sendCommand(byte command) {
  SPI.transfer(command);
}

void writeByte(byte registers, byte data) {
    char spi_data = 0x40 | registers;
    char spi_data_array[3]; 
    spi_data_array[0] = spi_data;
    spi_data_array[1] = 0x00;
    spi_data_array[2] = data;
    SPI.transfer(spi_data_array, 3);
				
				 
			//	 HAL_SPI_Transmit(&hspi1, (uint8_t*)&adress, 1, 0x1000);
			//	 HAL_SPI_Transmit(&hspi1, (uint8_t*)&test, 1, 0x1000);
			//	 HAL_SPI_Transmit(&hspi1, (uint8_t*)&val_hex, 1, 0x1000);
			//	 HAL_GPIO_WritePin(GPIOA, CS_Pin, GPIO_PIN_SET);

}
