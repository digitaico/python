
# flappy bird:
 #   elementos:
 #       pajaro
  #      tubos
  #      decoracion
  #         - arboles
  #         - montañas
  #         - pajaros
  #         - nubes
  #     score : cuando pasa tuberi, logra 10 pts

  #     // acciones
  #     pajaro:
  #          salta (desplaza verticalmente en eje j), respondiendo a accion de usuario en taclado.
   #         gira 45°en dirccion de salto.


  # // Estados
   #     pajaro
   #         - volando
   #         - caido
   #         . tuberia se mueve segun destreza (puntaje) jugador.
   #         . pajaro.posicion(x,y)
   #    tubos
    #       - coordenadas
    
    #    // 1. Montar escena: pajaro, tubos, montañas, nubes, pajartitos, estaticos.
    #    // 2. Molver escena: pajaro se ve volando,  entre y sobre tubos, y paisaje pasa.
    #    // 3. agregar acciones (movimientos) al pajaro: salto arriba y salto abajo.
    #    // 4. pegar acciones del pajaro a teclas: sunbir y bajar.
    #    // 5. modificar estado segun si pasa por tuberias o se estrella:
    #        //-score aumenta 10 pts si pasa tuberia.
    #        // - pajaro deja de volar si se estrella.
    #    // 6. Iniciar, pausar y terminar,  binded al teclado.
    #    // 7. game over, segun cantidad estrelladas.

import math
import pygame



