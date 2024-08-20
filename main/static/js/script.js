function filtrar_comunas () {
    // Obtener cod de la región
    const cod_region = $(this).val() 
    // Iteramos sobre todas las comunas y mostramos solo aquellas cuyo prefijo tenga el cod_region
    $('#comuna_cod').val('')
    $('#comuna_cod option').each(function() {
        const comuna = $(this)
        const cod_comuna = comuna.val()
        if (cod_region == cod_comuna.substring(0,2)) {
            comuna.show()
        } else {
            comuna.hide()
        }
    })
}

// Ejecuta la función filtrar_comuna al detectar cambios
$('#region_cod').on('change', filtrar_comunas)