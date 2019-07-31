#!/usr/bin/env python
import time
class Cocktail_Generator:
    def __init__ (self, cocktail_name, volume, pumps):
        
        self.volume = volume
        self.ct_name = str(cocktail_name)
        self.pumps = pumps
        
        # percentage liquid of total volume
        woap = [0.6, 0.4, 0, 0]
        baap = [0.7, 0.0, 0.3, 0]
        wowa = [0, 0.3, 0, 0.7]
        ba = [0, 0, 0.33, 0]
        
        self.mixtures = {'woap' : woap, 'baap' : baap, 'wowa' : wowa, 'ba': ba }
        
    def cocktail_composition ( self ):

        if self.ct_name in self.mixtures:
            print("Your cocktail will be prepared!")
            ct_composition = []
            for i in range(len(self.mixtures[self.ct_name])):
                ct_composition.append( self.volume * self.mixtures[self.ct_name][i] )
                self.ct_composition = ct_composition
            
        else:
            print("This cocktail is not aviable, please choose anonther one")
            return
        
        
            
    def pump_time( self ):
        
        speed = 350/240 #ml/sec
        self.pump_times = [i * speed for i in self.ct_composition]
        print(self.pump_times)

    
    def make_cocktail( self ):
        self.cocktail_composition()
        self.pump_time()
        
        for i in range(len(self.pump_times)):
            if self.pump_times[i] != 0:
                self.pumps[i].on()
                time.sleep(5)   #self.pumptimes[i])
                self.pumps[i].off()
        
        
        
        
        
        
    
    
 
