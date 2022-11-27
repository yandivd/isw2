const $seleccionArchivos = document.querySelector("#id_img"),
  $imagenPrevisualizacion = document.querySelector(
    "#imagenPrevisualizacion"
  );

$seleccionArchivos.addEventListener("change", () => {
  const archivos = $seleccionArchivos.files;
  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }
  const primerArchivo = archivos[0];
  const objectURL = URL.createObjectURL(primerArchivo);
  $imagenPrevisualizacion.src = objectURL;
});
