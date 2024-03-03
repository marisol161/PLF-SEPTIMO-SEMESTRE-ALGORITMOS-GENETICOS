# SEPTIMO-SEMESTRE-ALGORITMOS-GENETICOS
Los algorimos genéticos o algoritmos evolutivos se inspiran en la teorias evolutivas de Darwin sobre la selección natural. En grandes poblaciones de seres vivos, los individuos tienden a entrar en competencia por los recursos disponibles como alimneto, agua o refugio. Los mejor adaptados y los más fuertes tenderán a vivir más tiempo y a dejar una mayor descendencia mientras, que aquellos menos adaptados tendrán una descendencia menor. Con el tiempo, los genes de aquellos individuos mejor adaptados serán más abundantes y, por lo tanto, es de esperar una mejora global de la especie. Cuando dos individuos tienen descendencia, los genes de ambos se combinan logrando dar a lugar a un individuo con caracteristicas geneticas superiores a los de sus procreadores. Evidentemente, esto no siempre será así, ya que se podría encontrar descendientes menos adaptados; sin embargo, es de esperar que a mejor calidad genetica de los procreadores, mayor será la probabilidad de que las caracteristicas genéticas del descendiente sean buenas.

Por lo tanto el mecanismo permite la mejora de la especie gracias al intercambio de genes entre individuos; sin embargo, no es lo único. De vez en cuando surgen mutaciones accidentales en los genes. Estas mutaciones sulen ser negativas en la mayoria de los casos, pero de vez en cuando, se da una mutación que mejora las caracteristicas géneticas del individuo. Por lo tanto, se tiene dos mecanismos básicos de mejora de la especie: el entrecruzamiento de genes y la mutación de genes.

Los algoritmos genéticos, estan inspirados en los mecanismos de evolución natural, que parten de una gran población de indiviuos (soluciones) y va generando descendencia basándose en las características de los mejores individuos, siempre según la función de avaluación. La nuevas soluciones van distribuyendose, según las antiguas de forma que, con el tiempo, la población tienda a converger hacia la solución global del problema.

Al igual que ocurre con los algoritmos de búsqueda local examinados anteriormente, garantiza que se acaba encontrando la solución óptima, aunque si el algoritmo esta bien diseñado y parametrizado, se puede tener cierto grado de confianza en la que la solución alcanzada será, al menos, suficientemente buena.

Es necesario definir algunos conceptos antes de continuar.

Individuo: Es una solución válida para el problema, independientemente de lo buena que sea. Debe cumplir con las restricciones impuestas por el problema.
	Población: Conjunto de individuos(soluciones).
	Función de Adaptación: Indica con que grado se adapta el individuo a la solución. Es sinónimo de la función de evaluación que se ha venido usando hasta ahora.
	Genes:  Conjunto de parámetros o características que describen al individuo (solución). Por ejemplo, en el problema TSP, una ruta valida se correspondería con un gen. En el caso del problema SAT, el conjunto de valores asignados a las variables serían un gen. Por ejemplo (1, 0, 0, 1, 1).
	Cromosoma:  Cada uno de los parámetros o características que conforman un gen. Por ejemplo, si se tiene un gen que representa una ruta del problema TSP, cualquiera de las ciudades que conforman esa ruta sería un cromosoma.
	Convergencia de la población:  No se trata de conseguir que una de las soluciones sea muy buena, sino que la población, en general, sea buena. Dicho de otro modo, si la población en general converge hacia características similares, cuya función de adaptación sea buena, esto servirá de piedra de toque para poder afirmar que se converge a una solución óptima. Se dice que una población ha convergido si hay un gran porcentaje de individuos cuya función de adaptación es igual o muy similar. A ese porcentaje se le llamará factor de convergencia y se denotará como la letra griega  γ. Un valor habitual que permite afirmar que la población ha convergido suele ser γ = 95%. Es decir, que el 95% de población tiene genes similares.

En general, un algoritmo génetico esta compuesto por cuatro fases bien diferenciadas.

Selección: Se eligen las mejores soluciones(individuos) de toda la población. Dichas soluciones tendrán más probabilidad de dejar descendencia.
	Cruce: En esta fase se combinan los genes de los mejores individuos, seleccionados en la fase anterior.
	Mutación: Con cierta probabilidad, se mutará un cromosoma de algunos de los individuos. Hay que hacer notar que la probabilidad de que se dé una mutación, ha de mantenerse lo suficientemente baja, para que no se degrade el potencial de mejora del cruce genético.
	Eliminación: Si no se elimina individuos, la población crecerá indefinidamente hasta hacerse inmanejable. Es por ello que hay que eliminar a aquellos individuos (soluciones) peor adaptados.

 Alternativamente, puede usarse un limite en el número de iteraciones en vez de una condición de convergencia. O pueden usarse ambos criterios a la vez: el que se cumpla primero.

Se han descrito las cuatro fases del algoritmo genético. Ahora se profundizará un poco más en cada una de ellas.

La fase de selección, es la que permite escoger aquellas soluciones más cercanas a la solución optima. El criterio que se sigue para puntuar las soluciones es la función de adaptación. Básicamete, lo que se hace es dar una puntuación a cada individuo, basandose en el valor devuelto por la función de adaptación y según sea dicho valor, el individuo tendrá más o menos probabilidades de ser seleccionado.

Una estrategia alternativa, podria ser directamente la de tomar a los dos mejores individus para cruzarlos, pero esta estrategia ha demostrado ser poco eficiente, ya que la falta de diversidad genética puede hacer que la evolución sea lenta e incluso que se detenga.


