function seleccionarBoton(boton) {
    boton.classList.toggle('btnhoraselected')
    boton.classList.toggle('btnhora')
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