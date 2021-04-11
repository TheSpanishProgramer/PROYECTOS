<?php
// Este archivo contiene distintqs lineas de codigo que pueden ser utiles 
// Y tenerlas todas en un mismo lugar y copiar y pegar cuando sea necesario


// Desactivar el boton submit  (cambiar enviar por la ID correspondiente)
echo '<script>document.getElementById("enviar").disabled=true</script>';

// Boton de recargar pagina
echo '<button onclick ="document.location.href = document.location.href;">Recargar</button><br>';

// Es una funcion que devuelve True or False dependiendo de si la palabra esta en el array
in_array($variable, $array);

//  Esta funcion para arrays asociativos devuelve la clave a partir de un valor 
array_search($valor, $array);

//  Esta funcion para arrays asociativos devuelve true o false dependiendo de si la variable
// introducida existe como clave en el array
array_key_exists($variable, $array)

?>