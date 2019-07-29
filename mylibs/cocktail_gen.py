#!/usr/bin/env python

class Cocktail_Generator:
    def __init__ (self, cocktail_name, volume):
        
        self.volume = volume
        self.ct_name = cocktail_name
        
        # percentage liquid of total volume
        mix1 = [0.2, 0.0, 0.5, 0.3]
        mix2 = [0.0, 0.3, 0.5, 0.2]
        mix3 = [0.1, 0.3, 0.5, 0.1]
        assert (sum(mix1), sum(mix2), sum(mix3))  == (1, 1, 1)
        
        self.mixtures = dict(mix1, mix2, mix3)
        
    def cocktail_composition ( self ):

        if self.cocktail_name in self.mixtures:
            print("Your cocktail will be prepared!")
        else:
            print("This cocktail is not aviable, please choose anonther one")
            return
        
        for i in self.mixtures:
            ct_volume = []
            ct_volume.append( self.volume * self.mixtures['self.ct_name'] )
            
        return ct_volume
        
    
    
 
