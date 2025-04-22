def facultyfiter(faculty:list):
    return list(filter(lambda x: True if(len(x)>8) else False,faculty))
faculty=["scicusgdi","svbh","sidsgadagghh","jirtjyrh","ohk"]
print(facultyfiter(faculty))