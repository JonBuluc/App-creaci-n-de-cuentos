// script.js

function setDuracion(duracion) {
    document.getElementById('btnCorto').classList.remove('boton-activo');
    document.getElementById('btnNormal').classList.remove('boton-activo');
    document.getElementById('btnLargo').classList.remove('boton-activo');

    document.getElementById('btn' + duracion.charAt(0).toUpperCase() + duracion.slice(1)).classList.add('boton-activo');
    document.getElementById('duracionSeleccionada').value = duracion;

    // Habilitar el botón "Crear Historia" cuando se selecciona la duración
    document.getElementById('crearHistoriaBtn').disabled = false;
}

function validarFormulario() {
    var titulo = document.getElementById('titulo').value;
    var categoria = document.getElementById('categoria').value;
    var duracionSeleccionada = document.getElementById('duracionSeleccionada').value;

    if (!titulo || !categoria || !duracionSeleccionada) {
        alert('Por favor, complete todos los campos del formulario.');
        return false;
    }

    return true;
}

function crearHistoria() {
    var titulo = document.getElementById('titulo').value;
    var categoria = document.getElementById('categoria').value;
    var duracionSeleccionada = document.getElementById('duracionSeleccionada').value;

    // Hacer la petición POST al servidor
    fetch('/mandar_a_crear_historia', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            titulo: titulo,
            categoria: categoria,
            duracion: duracionSeleccionada
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Manejar la respuesta del servidor
        console.log(data);

        // Mostrar la historia creada
        var historiaCreadaDiv = document.getElementById('historiaCreada');
        historiaCreadaDiv.innerHTML = `
            <h3>Historia creada: ${data.titulo}</h3>
            <p>Categoría: ${data.categoria}</p>
            <p>Duración: ${data.duracion}</p>
            <p>Contenido: ${data.contenido}</p>
        `;

        // Mostrar el botón para ir a Index
        document.getElementById('irAIndexBtn').style.display = 'inline-block';
    })
    .catch(error => {
        console.error('Error:', error);
    });

    return false; // Evitar que el formulario se envíe
}

function irAIndex() {
    window.location.href = '/'; // Redirigir a la página principal (index.html)
}

