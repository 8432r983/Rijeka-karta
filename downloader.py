import requests

def nextImages(zoom, xcomp, ycomp):
    new_zoom = zoom+1
    xcomps = [xcomp*2, xcomp*2 + 1]
    ycomps = [ycomp*2, ycomp*2 + 1]
    for i in range(2):
        for j in range(2):
            yield (new_zoom, xcomps[i], ycomps[j])


def downloadImage(data):
    path = "/".join(list(map(str, data)))

    url = "https://tiles.stadiamaps.com/tiles/osm_bright/"+ path + ".png?api_key=6b25d6d7-056b-4364-a0f7-252eda0b96c4"
    res = requests.get(url)

    if res.status_code != 200:
        print("Failed to download image!")
        exit()

    filename = "img_" + "_".join(list(map(str, data))) + ".png"
    with open("C:/Users/Adrian/Documents/JS_projects/ZOOmapa-lokal/images/" + filename, 'wb') as file:
        file.write(res.content)

start_zoom = 9
start_x = 276
start_y = 183

buffer = [(start_zoom, start_x, start_y)] 

downloadImage(buffer[0])

for i in range(6):
    new_buffer = []
    for b in buffer:
        for j in nextImages(b[0], b[1], b[2]):
            new_buffer.append(j)
    buffer = new_buffer

    #for j in buffer:
     #   downloadImage(j)
    

