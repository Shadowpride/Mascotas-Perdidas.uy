function AmpliarImagen(id) {
    Swal.fire({
        imageUrl: "/"+id+"/",
        imageHeight: 500,
        imageAlt: 'Imagen de la Publicacion'
      })
}