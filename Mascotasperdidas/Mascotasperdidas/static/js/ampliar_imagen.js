function AmpliarImagen('{{ publicacion.imagen.url }}') {
    Swal.fire({
        imageUrl: '{{ publicacion.imagen.url }}',
        imageHeight: 800,
        imageAlt: 'Imagen de la Publicacion'
      })
}