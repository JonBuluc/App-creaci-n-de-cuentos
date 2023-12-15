from openai import OpenAI
from .models import db, Historia



def generar_cuento(titulo, categoria, duracion, modelo="gpt-3.5-turbo"):
    client = OpenAI(api_key="")
    # Mapear las opciones de duración a longitud aproximada en tokens
    duracion_a_tokens = {"corto": 100, "normal": 200, "largo": 300}

    # Construir el prompt
    prompt = f"Escribe un cuento con el título '{titulo}', que pertenezca a la categoría '{categoria}' y con una duración {duracion}."
    

    # Hacer la solicitud a la API
    respuesta = client.chat.completions.create(
        model=modelo,
        messages=[
        {"role": "user", "content": prompt}
        ],
        max_tokens=duracion_a_tokens[duracion]
    )

    return respuesta.choices[0].message.content


def crearHistoria(titulo,categoria,duracion):

    contenido=generar_cuento(titulo=titulo,categoria=categoria,duracion=duracion)


    # Agregar historia a la base de datos
    nueva_historia = Historia(titulo=titulo, categoria=categoria, duracion=duracion,contenido=contenido)
        
    # Agregar la historia a la base de datos
    db.session.add(nueva_historia)
    db.session.commit()

    return contenido



