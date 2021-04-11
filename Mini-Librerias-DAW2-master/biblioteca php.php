<?php
// Devuelve true si es primo o false si no lo es
function esPrimo($numero) {
 
    $primo = true;
    
    if ($numero == 0 || $numero == 1) {
        
        $primo = true;
        
    } else {
    
        for ($i = 2; $i < $numero; $i++) {
            
            if (($numero % $i) == 0) {
                $primo = false;
            }
        }
    }
    return $primo;
}
?>
