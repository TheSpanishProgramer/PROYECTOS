// Funcion Random entre un minimo y un maximo
function randomRange(min, max) {
    
    var resultado = (Math.random() * (max - min)) + min;
    
	/* Si queremos numeros enteros con esta formula conseguimos que todos los numeros tengan la misma probabilidad de salir
	var resultado = Math.floor((Math.random() * (max - min + 1)) + min);
	
	*/
	
    return resultado;
    
}


// Funcion contains manual. Dado que no he encontrado niongun metodo para arrays similar 
// Parametros: array (array que se quiere comprobar).
//					   obj (objeto que se quiere comprobar si esta en el array)
// return: True or false.
function contains(array, obj) {
	// Bucle for para recorrer el array
    for (var i = 0; i < array.length; i++) {
		// Si se encuentra el objeto
        if (array[i] == obj) {
			// Retorna true
            return true;
        }
    }
	
	// Si no encuentra el objeto retorna false.
    return false;
}


// Funcion que borra el elemento objeto que se pasa como parametro
function borrar(elemento) {
    
    elemento.parentNode.removeChild(elemento);
    
}

// Funcion para borrar todos los elementos de un contenedor
function borrarTodo (contenedorId) {

	// Buscamos el contenedor donde se encuentra todo lo que queremos borrar
	var contenedor = document.getElementById(contenedorId);
                
	// Mientras el contenedor tenga nodos hijos, los borrara.
	while (contenedor.firstChild) {
		contenedor.removeChild(contenedor.firstChild);
    }

}


// Funcion para mover un elemento a la izquierda o derecha
// Si ponemos distancia negativa nos moveremos hacia la izquierda
// Si ponemos distancia positiva nos moveremos hacia la derecha
function moverHorizontal(elementoId, distancia) {
 
    var elemento = document.getElementById(elementoId);
    
    elemento.style.left = (elemento.offsetLeft + distancia) + "px";
    
}


// Funcion para mover un elemento hacia arriba o hacia abajo
// Si ponemos distancia negativa nos moveremos hacia arriba
// Si ponemos distancia positiva nos moveremos hacia abajo
function moverVertical(elementoId, distancia) {
 
    var elemento = document.getElementById(elementoId);
    
    elemento.style.top = (elemento.offsetTop + distancia) + "px";
    
}

