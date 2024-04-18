#include "WiFiS3.h"

char ssid[] = "BT-P7CPQC";
char pass[] = "CRQuTXGfkf4g3a";
int status = WL_IDLE_STATUS;
WiFiServer server(80);

void setup() {
  Serial.begin(9600);
  while (status != WL_CONNECTED) 
    {
    status = WiFi.begin(ssid, pass);
    }
  server.begin();
}
  int a = 0;
void loop() {

  WiFiClient client = server.available();
    client.println("HTTP/1.1 200 OK");
    client.println("Content-type:text/html");
  //  int c = 8;
  //  client.print(c);

    String currentLine = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println();
            a += 1;
            client.print(a);
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    client.stop();
    Serial.println("Client disconnected.");
}
