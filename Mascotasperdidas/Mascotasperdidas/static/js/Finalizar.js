function Finalizar(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "No podrás deshacer esta acción",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, finalizar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.value) {
            //Redirigir a la ruta de eliminar
            window.location.href = "/finalizar/"+id+"/";
        }
      })
}