import wikipedia

def pedia(url, sentences=1):
    
    raw_title = url.split("/wiki/")[-1]
    

    title = raw_title.replace("_", " ")
    
    return wikipedia.summary(title, sentences=sentences)

print(pedia("https://en.wikipedia.org/wiki/USB_flash_drive"))