#include <FastLED.h>

FASTLED_USING_NAMESPACE

// Adapted from the FastLED "100-lines-of-code" demo reel, showing just a few 
// of the kinds of animation patterns you can quickly and easily 
// compose using FastLED.  

// -Mark Kriegsman, December 2014

#if defined(FASTLED_VERSION) && (FASTLED_VERSION < 3001000)
#warning "Requires FastLED 3.1 or later; check github for latest code."
#endif

#define DATA_PIN    8
//#define CLK_PIN   4
#define LED_TYPE    WS2811
#define COLOR_ORDER RGB
#define NUM_LEDS    236
CRGB leds[NUM_LEDS];

#define BRIGHTNESS          98
#define FRAMES_PER_SECOND  120

void setup() {
  delay(3000); // 3 second delay for recovery
  
  // tell FastLED about the LED strip configuration
  FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  //FastLED.addLeds<LED_TYPE,DATA_PIN,CLK_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);

  // set master brightness control
  FastLED.setBrightness(BRIGHTNESS);
  FastLED.setMaxPowerInVoltsAndMilliamps( 5, 500); //Add some Power management magic...
}

uint8_t gHue = 0; // rotating "base color" used by many of the patterns
  
void loop()
{
  //Create the rainbow with builtin animation
  fill_rainbow( leds, NUM_LEDS, gHue, 7);
  // send the 'leds' array out to the actual LED strip
  FastLED.show();  
  // insert a delay to keep the framerate modest
  FastLED.delay(1000/FRAMES_PER_SECOND); 

  // do some periodic updates
  EVERY_N_MILLISECONDS( 100 ) { gHue++; } // slowly cycle the "base color" through the rainbow
}
