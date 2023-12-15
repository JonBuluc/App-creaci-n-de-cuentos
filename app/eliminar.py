from .models import db, Historia  # Asegúrate de tener los nombres correctos

# Obtén los primeros cuatro elementos de la base de datos
historias_a_eliminar = Historia.query.limit(4).all()

# Elimina cada uno de los elementos
for historia in historias_a_eliminar:
    db.session.delete(historia)

# Confirma los cambios
db.session.commit()
