# Referencia de Combate

## Secuencia de Combate Por Ronda
1. **Declarar** conjuros y movimiento cuerpo a cuerpo (los conjuros y el movimiento deben declararse antes de la iniciativa)
2. **Iniciativa**: Cada bando tira 1d6; el más alto actúa primero. Empate = simultáneo o volver a tirar.
3. El bando ganador actúa: moral del monstruo → movimiento → ataques con proyectiles → lanzamiento de conjuros → ataques cuerpo a cuerpo
4. Los demás bandos actúan en orden de iniciativa.

## Iniciativa
- **Estándar**: Cada *bando* tira 1d6. El más alto gana.
- **Individual (opcional)**: Cada combatiente tira 1d6, modificado por el bonificador de DES.
- **Armas lentas**: Las armas cuerpo a cuerpo de dos manos siempre actúan *al final*, independientemente de la iniciativa.

| DES | Mod. CA | Proyectiles | Iniciativa |
|-----|---------|-------------|------------|
| 3 | –3 | –3 | –2 |
| 4–5 | –2 | –2 | –1 |
| 6–8 | –1 | –1 | –1 |
| 9–12 | — | — | — |
| 13–15 | +1 | +1 | +1 |
| 16–17 | +2 | +2 | +1 |
| 18 | +3 | +3 | +2 |

## Tiradas de Ataque (CA Descendente)
1. Tirar 1d20
2. Aplicar modificadores (FUE para cuerpo a cuerpo; DES + distancia para proyectiles)
3. Consultar el resultado en la tabla de ataque para la fila THAC0 del atacante → encontrar qué CA es golpeada
4. Si la CA golpeada ≤ CA del oponente, el ataque impacta

**Atajo**: Tirada necesaria = THAC0 − CA del objetivo (p. ej., THAC0 17 vs CA 4 → necesita 13+)

**CA Ascendente (opcional)**: Tirar 1d20 + Bono de Ataque; si el resultado ≥ CA ascendente del oponente, impacta.

| Tirada de Ataque | 1 Natural | 20 Natural |
|------------------|-----------|------------|
| Siempre falla | Siempre impacta |

## Tabla de Ataque (Filas Clave)
| THAC0 | [Bonificación] | Golpea CA: –3 | 0 | 2 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|----------------|---------------|---|---|---|---|---|---|---|---|
| 19 | [0] | 20 | 19 | 17 | 15 | 14 | 13 | 12 | 11 | 10 |
| 18 | [+1] | 20 | 18 | 16 | 14 | 13 | 12 | 11 | 10 | 9 |
| 17 | [+2] | 20 | 17 | 15 | 13 | 12 | 11 | 10 | 9 | 8 |
| 16 | [+3] | 19 | 16 | 14 | 12 | 11 | 10 | 9 | 8 | 7 |
| 15 | [+4] | 18 | 15 | 13 | 11 | 10 | 9 | 8 | 7 | 6 |
| 14 | [+5] | 17 | 14 | 12 | 10 | 9 | 8 | 7 | 6 | 5 |
| 13 | [+6] | 16 | 13 | 11 | 9 | 8 | 7 | 6 | 5 | 4 |
| 12 | [+7] | 15 | 12 | 10 | 8 | 7 | 6 | 5 | 4 | 3 |

## Referencia de Clase de Armadura
| Armadura | CA (desc.) | CA (asc.) |
|----------|------------|-----------|
| Sin armadura | 9 | [10] |
| Cuero | 7 | [12] |
| Cota de malla | 5 | [14] |
| Armadura de placas | 3 | [16] |
| + Escudo | –1 | +1 |

## Daño
- **Por defecto**: Todas las armas hacen 1d6.
- **Variable (opcional)**: Usar dados de daño específicos del arma (ver equipment).
- El modificador de FUE aplica al daño cuerpo a cuerpo.
- Mínimo 1 de daño en un impacto, incluso tras penalizaciones.

## Movimiento en Combate
- **Movimiento de encuentro**: ⅓ de la tasa base de movimiento por ronda.
- **Retirada de combate**: Moverse hacia atrás hasta la mitad de la tasa de encuentro; requiere camino despejado.
- **Huida**: Tasa de encuentro completa; no puede atacar; el oponente obtiene +2 a golpear e ignora la bonificación de CA del escudo esa ronda.
- **Correr**: Tasa base de movimiento en pies por ronda. Tras 30 rondas: –2 a ataques, daño y CA.

## Ataques con Proyectiles
| Distancia | Modificador |
|-----------|-------------|
| Corta | +1 a golpear |
| Media | Ninguno |
| Larga | –1 a golpear |
| Más allá del largo | No puede atacar |

- Posible cuando los oponentes están a más de 5' de distancia.
- Cobertura: –1 a –4 a golpear (parcial); imposible (total).

## Lanzamiento de Conjuros en Combate
- Debe declararse antes de la iniciativa.
- No puede moverse y lanzar en la misma ronda.
- Debe poder hablar y mover las manos.
- Si es golpeado o falla una tirada de salvación *antes* de actuar tras perder la iniciativa: el conjuro se interrumpe y se pierde.
- Los conjuros deben tener línea de visión al objetivo.

## Moral (Opcional)
- Los monstruos tiran 2d6 vs su puntuación de moral.
- Si la tirada **supera** la moral: se rinden o huyen.
- Si la tirada **≤** la moral: siguen combatiendo.
- Verificar al: primer muerto del grupo, cuando la mitad del grupo está incapacitada.
- Dos verificaciones de moral exitosas = lucha hasta la muerte.

| Tipo de Tropa | Moral |
|---------------|-------|
| Milicia sin entrenamiento | 6 |
| Horda bárbara | 7 |
| Guerreros entrenados | 8 |
| Montados | +1 |
| Tropas de élite | +1 |
| Fanáticos/berserkers | +2 |

## Ataques Especiales

### Ataque por la Espalda (Ladrón)
- Atacar por detrás a un oponente desprevenido.
- **+4 a golpear**, **×2 daño**.
- En nivel 6: multiplicador de daño ×2.

### Repeler No-Muertos (Clérigo)
- Tirar 2d6; comparar con la Tabla de Repulsión vs DG del no-muerto.
- Éxito: tirar 2d6 para determinar el total de DG afectados (repelidos o destruidos).
- Los no-muertos repelidos huyen y no contactarán al clérigo.
- Destruido (D): aniquilado instantáneamente.
- Al menos 1 no-muerto siempre es afectado en un éxito.
- Grupos mixtos: los de menor DG son afectados primero.

*Ver cleric.md para la tabla completa de repulsión.*

### Oponentes Paralizados/Indefensos
- Impactados automáticamente en cuerpo a cuerpo; solo se tira el daño.

### Carga
- Requiere una carrera despejada de 20 yardas; daño doble en el impacto (lanza u arma apropiada).

### Sometimiento (Opcional)
- Declarar la intención; usar solo armas contundentes.
- Rastrear el daño de sometimiento por separado.
- A 0 PG por sometimiento: rendición.

## Muerte y Curación
- **Muerte**: Reducido a 0 PG o menos.
- **Destrucción de objetos**: Si es matado por rayo, arma de aliento, etc., el equipo puede ser destruido.
- **Curación natural**: 1d3 PG por día completo de descanso total. Descanso interrumpido = sin curación.
- **Curación mágica**: Instantánea; se acumula con la curación natural.
- **Descanso en mazmorra**: Se requiere 1 turno (10 min) de descanso por hora o sufrir –1 a ataque y daño.
- **Descanso en exteriores**: 1 día completo por cada 6 días de viaje o sufrir –1 a golpear y daño.

## Sorpresa
- Tirar 1d6 por cada bando que no espera el encuentro.
- **1 o 2**: Ese bando es sorprendido.
- El bando sorprendido pierde su acción durante una ronda; el otro bando obtiene una ronda libre.
- Portar luz en la oscuridad: generalmente no puede sorprender a los oponentes.
