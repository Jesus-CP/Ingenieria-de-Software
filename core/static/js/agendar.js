document.addEventListener('DOMContentLoaded', function() {
    console.log(citas_doctor); // Verificar si contiene los datos esperados
  
    citas_doctor.forEach(function(cita) {
      console.log('Fecha de atención: ' + cita.fechaAtencion);
      console.log('Hora de inicio: ' + cita.horaInicio);
    });
  });
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

