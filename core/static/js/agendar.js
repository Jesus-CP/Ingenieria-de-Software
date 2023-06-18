function seleccionarBoton(boton) {
    boton.classList.toggle('btnhoraselected')
    boton.classList.toggle('btnhora')
    const btnhoraSelected = 'btnhoraselected';
    if (boton.classList.contains(btnhoraSelected)) {
        // Se ha seleccionado el botón
        const horaInicio = boton.innerText.trim().split(' - ')[0];
        document.getElementById('horaInicio').value = horaInicio;
    } else {
        // Se ha deseleccionado el botón
        document.getElementById('horaInicio').value = '';
    }
}


function mostrarModal(modal) {
    modal.classList.toggle('hide')
}

const citas = [
    {
        dia: 'miercoles',
        fecha: '17/06/2023',
        hora: '15:00'
    },
    {
        dia: 'miercoles',
        fecha: '17/06/2023',
        hora: '16:00'
    },
    {
        dia: 'miercoles',
        fecha: '18/06/2023',
        hora: '12:00'
    }
]

for (var i = 0; i < citas.length; i++) {
    
}