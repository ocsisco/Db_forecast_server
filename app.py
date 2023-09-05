from flask import Flask,render_template,request
import os

from handler_s3_images import get_s3_imagelist_from,download_s3_images

os.makedirs('static/', exist_ok=True)

app = Flask(__name__)


@app.route('/')
def ayuda():
    return render_template("ayuda.html")

@app.route('/prevision')
def prevision():

    imagelist = get_s3_imagelist_from("static_images")
    for filename in imagelist:
        download_s3_images("static_images","static",filename)
    return render_template("prevision.html")

@app.route('/serie_actual')
def serie_actual():

    imagelist = get_s3_imagelist_from("static_images")
    for filename in imagelist:
        download_s3_images("static_images","static",filename)
    return render_template("serie_actual.html")

@app.route('/serie_antigua')
def serie_antigua():

    imagelist = get_s3_imagelist_from("static_images")
    for filename in imagelist:
        download_s3_images("static_images","static",filename)
    return render_template("serie_antigua.html")

@app.route('/historico_disponible')
def historico_disponible():

    lista_historico = get_s3_imagelist_from("images_color")
    lista_historico = sorted(lista_historico)

    return str(lista_historico)


@app.route('/historico')
def historico():

    image_name = request.args.get("date")

    if "imagen_seleccionada.png" in os.listdir("static"):    
        os.remove(os.path.join("static/imagen_seleccionada.png"))

    download_s3_images("images_color","static",image_name)
    os.rename("static/"+image_name, "static/imagen_seleccionada.png")
    
    print(image_name)
    
    return render_template("imagen_seleccionada.html",image_name=image_name)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=False)
