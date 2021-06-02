def domain_name(url):
    url = url.replace("//", ".")    
    arr = url.split(".")
    if arr[0] == "http:" or arr[0] == "https:":
        if arr[1] == "www":
            return arr[2]
        return arr[1]
    elif arr[0] == "www":
        return arr[1]
    else:
        return arr[0]

print (domain_name("https://youtube.com"))