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

