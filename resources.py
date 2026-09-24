def hangrend(szo):
    mely=["a", "á", "u", "ú", "o", "ó"]
    magas=["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    van_magas=False
    van_mely=False
    
    for betu in szo:
        if betu in magas:
            van_magas=True  
        elif betu in mely:
            van_mely=True
            
    if van_magas and van_mely:
        return "vegyes"
    elif van_magas:
        return "magas"
    elif van_mely:
        return "mely"
    
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

def ragozas (szo, drag, hrag):
    odrag = drag
    ohrag = hrag
    hr = hangrend(szo)
    utolso = szo[-1]

    if not drag[0] in ("v", "V"):
        if hr in ("mely", "vegyes"):
            return szo + odrag
        else:
            return szo + ohrag
        
    elif drag[0] in ("v", "V"):
        drag = drag[1:] #val -> al
        hrag = hrag[1:] #vel -> el

        ragok_mely_vegyes = {
            "b": f"b{drag}", 
            "c": f"c{drag}", 
            "d": f"d{drag}", 
            "f": f"f{drag}", 
            "g": f"g{drag}", 
            "h": f"h{drag}", 
            "j": f"j{drag}", 
            "k": f"k{drag}", 
            "l": f"l{drag}", 
            "m": f"m{drag}", 
            "n": f"n{drag}", 
            "p": f"p{drag}", 
            "q": f"q{drag}", 
            "r": f"r{drag}", 
            "s": f"s{drag}", 
            "t": f"t{drag}", 
            "v": f"v{drag}", 
            "w": f"w{drag}", 
            "x": f"x{drag}", 
            "y": f"y{drag}", 
            "z": f"z{drag}", 
        }
        ragok_magas = {
            "b": f"b{hrag}", 
            "c": f"c{hrag}", 
            "d": f"d{hrag}", 
            "f": f"f{hrag}", 
            "g": f"g{hrag}", 
            "h": f"h{hrag}", 
            "j": f"j{hrag}", 
            "k": f"k{hrag}", 
            "l": f"l{hrag}", 
            "m": f"m{hrag}", 
            "n": f"n{hrag}", 
            "p": f"p{hrag}", 
            "q": f"q{hrag}", 
            "r": f"r{hrag}", 
            "s": f"s{hrag}", 
            "t": f"t{hrag}", 
            "v": f"v{hrag}", 
            "w": f"w{hrag}", 
            "x": f"x{hrag}", 
            "y": f"y{hrag}", 
            "z": f"z{hrag}", 
        }


        if hr in ("mely", "vegyes"):
            ragok = ragok_mely_vegyes
            fallback = odrag
        else:
            ragok = ragok_magas
            fallback = ohrag

        if utolso == "a":
            return szo[:-1] + "á" + fallback
        
        if utolso == "e":
            return szo[:-1] + "é" + fallback
        
        return szo + ragok.get(utolso, fallback)