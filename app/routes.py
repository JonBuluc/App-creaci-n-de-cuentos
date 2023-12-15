from flask import Blueprint, render_template
from flask import request, jsonify
from .models import db, Usuario, Historia
from app.accionesChatGPT import crearHistoria

main = Blueprint('main',__name__)

@main.route('/')
def index():
    # Aquí deberías obtener las historias de tu base de datos
    # Supongamos que tienes una clase Historia que representa tu modelo en la base de datos
    historias = Historia.query.order_by(Historia.id.desc()).all()

    # Luego pasas las historias al template
    return render_template('index.html', historias=historias)



  
@main.route('/mandar_a_crear_historia', methods=['POST'])
def mandar_a_crear_historia():
    
    # Obtener los datos del formulario
    data = request.json  # Obtén los datos del cuerpo JSON

    # Obtén los valores de los campos del formulario
    titulo = data.get('titulo')
    categoria = data.get('categoria')
    duracion = data.get('duracion')
    

    # Crear una nueva historia
    contenido=crearHistoria(titulo=titulo,categoria=categoria,duracion=duracion)
        # Devolver la historia creada como respuesta
    
    return jsonify({
        'titulo': titulo,
        'categoria': categoria,
        'duracion': duracion,
        'contenido': contenido
    })




@main.route("/crear-ia")
def crear_ia():
    return render_template("crear-ia.html")