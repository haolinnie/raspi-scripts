#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define MAXTIMINGS    85

static int dht11_dat[5] = { 0, 0, 0, 0, 0 };

// TODO: Write data struct that read function returns
// Only returns after successful read
// Print humidity to stdout
typedef struct {
    float temperature;
    float humidity;
} dht_data;
 
dht_data read_dht11_dat(int DHTPIN) {
    dht_data data;
    while (1) {
       uint8_t laststate = HIGH;
       uint8_t counter = 0;
       uint8_t j = 0, i;
       data.temperature = 0;
       data.humidity = 0;
    
       dht11_dat[0] = dht11_dat[1] = dht11_dat[2] = dht11_dat[3] = dht11_dat[4] = 0;
    
       pinMode( DHTPIN, OUTPUT );
       digitalWrite( DHTPIN, LOW );
       delay( 18 );
       digitalWrite( DHTPIN, HIGH );
       delayMicroseconds( 40 );
       pinMode( DHTPIN, INPUT );
 
       for ( i = 0; i < MAXTIMINGS; i++ ) {
           counter = 0;
           while ( digitalRead( DHTPIN ) == laststate ) {
               counter++;
               delayMicroseconds( 1 );
               if ( counter == 255 ) {
                   break;
               }
           }
           laststate = digitalRead( DHTPIN );
    
           if ( counter == 255 )
               break;
    
           if ( (i >= 4) && (i % 2 == 0) ) {
               dht11_dat[j / 8] <<= 1;
               if ( counter > 16 )
                   dht11_dat[j / 8] |= 1;
               j++;
           }
       }
    
       if ((j >= 40) && (dht11_dat[4] == ((dht11_dat[0] + dht11_dat[1] + dht11_dat[2] + dht11_dat[3]) & 0xFF))) {
           /*printf( "Humidity = %d.%d %% Temperature = %d.%d C\n",*/
               /*dht11_dat[0], dht11_dat[1], dht11_dat[2], dht11_dat[3]);*/
           data.humidity = dht11_dat[0] + 0.1 * dht11_dat[1];
           data.temperature = dht11_dat[2] + 0.1 * dht11_dat[3];
           break;
       } else  {
           /*printf( "Data not good, skip\n" );*/
       }

        delay(1000); 
    }
    return data;
}
 
int main(int argc, char** argv) {
    /*printf( "Raspberry Pi wiringPi DHT11 Temperature test program\n" );*/
 
    if ( wiringPiSetupGpio() == -1 )
        exit(1);

    int DHTPIN;
    if (argc == 1) {
        DHTPIN = 14;
    } else {
        DHTPIN = atoi(argv[1]);
    }
    /*printf("%d",DHTPIN);*/

    dht_data data = read_dht11_dat(DHTPIN);
    /*printf("Temperature = %.1f%\n", data.temperature);*/
    /*printf("Humidity = %.1f%\n", data.humidity);*/
    printf("%.1f\n", data.temperature);
    printf("%.1f\n", data.humidity);
 
    return 0;
}
