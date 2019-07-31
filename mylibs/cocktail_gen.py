#!/usr/bin/env python
import time
class Cocktail_Generator:
    def __init__ (self, cocktail_name, volume, pumps):
        
        self.volume = volume
        self.ct_name = cocktail_name
        self.pumps = pumps
        
        # percentage liquid of total volume
        woap = [0.6, 0.4, 0, 0]
        baap = [0.7, 0.0, 0.3, 0]
        wowa = [0, 0.3, 0, 0.7]
        ba = [0, 0, 0.33, 0]
        
        self.mixtures = dict(woap, baap, wowa, ba)
        
    def cocktail_composition ( self ):

        if self.cocktail_name in self.mixtures:
            print("Your cocktail will be prepared!")
        else:
            print("This cocktail is not aviable, please choose anonther one")
            return
        
        ct_composition = []
        for i in self.mixtures:
            ct_composition.append( self.volume * self.mixtures['self.ct_name'] )
        self.ct_composition = ct_composition
            
    def pump_time( self ):
        
        speed = 350/240 #ml/sec
        self.pumptimes = [i * speed for i in self.ct_composition]

    
    def make_cocktail( self ):
        self.cocktail_composition()
        self.pump_time()
        
        for i in range(len(self.pump_times)):
            self.pumps[i].on()
            time.sleep(self.pumptime[i])
            self.pumps[i].off()
        
        
        
        
        
        
    
    
 
