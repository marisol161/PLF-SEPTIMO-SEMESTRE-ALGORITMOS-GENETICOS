from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/algoritmo_genetico', methods=['POST'])
def algoritmo_genetico():
    max_iter = int(request.form['max_iter'])
    max_poblacion = int(request.form['max_poblacion'])
    num_vars = int(request.form['num_vars'])

    solucion = poblacion_inicial(1, num_vars)[0]
    poblacion = poblacion_inicial(max_poblacion, num_vars)

    iteraciones = 0
    while iteraciones < max_iter:
        iteraciones += 1
        for i in range((len(poblacion))//2):
            gen1, gen2 = seleccion(poblacion, solucion)
            nuevo_gen1, nuevo_gen2 = cruce(gen1, gen2)
            nuevo_gen1 = mutacion(0.1, nuevo_gen1)
            nuevo_gen2 = mutacion(0.1, nuevo_gen2)
            poblacion.append(nuevo_gen1)
            poblacion.append(nuevo_gen2)
            elimina_peores_genes(poblacion, solucion)

    mejor = mejor_gen(poblacion, solucion)
    resultado = {
        'solucion': solucion,
        'mejor_gen': mejor,
        'funcion_adaptacion': adaptacion_3sat(mejor, solucion)
    }

    print("Solución:", solucion)
    print("Mejor gen Encontrado:", mejor)

    return jsonify(resultado)

def poblacion_inicial(max_poblacion, num_vars):
    poblacion = []
    for _ in range(max_poblacion):
        gen = [random.choice([0, 1]) for _ in range(num_vars)]
        poblacion.append(gen)
    return poblacion

def adaptacion_3sat(gen, solucion):
    n = 3
    cont = 0
    clausula_ok = True
    for i in range(len(gen)):
        n -= 1
        if gen[i] != solucion[i % len(solucion)]:
            clausula_ok = False
            if n == 0:
                if clausula_ok:
                    cont += 1
                n = 3
                clausula_ok = True
        if n == 0:
            if clausula_ok:
                cont += 1
    return cont

def evalua_poblacion(poblacion, solucion):
    adaptacion = []
    for i in range(len(poblacion)):
        adaptacion.append(adaptacion_3sat(poblacion[i], solucion))
    return adaptacion

def seleccion(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    total = sum(adaptacion)
    val1 = random.randint(0, total)
    val2 = random.randint(0, total)
    sum_sel = 0
    for i in range(len(adaptacion)):
        sum_sel += adaptacion[i]
        if sum_sel >= val1:
            gen1 = poblacion[i]
            break
    sum_sel = 0
    for i in range(len(adaptacion)):
        sum_sel += adaptacion[i]
        if sum_sel >= val2:
            gen2 = poblacion[i]
            break
    return gen1, gen2

def cruce(gen1, gen2):
    corte = random.randint(0, len(gen1))
    nuevo_gen1 = gen1[0:corte] + gen2[corte:]
    nuevo_gen2 = gen2[0:corte] + gen1[corte:]
    return nuevo_gen1, nuevo_gen2

def mutacion(prob, gen):
    if random.random() < prob:
        cromosoma = random.randint(0, len(gen)-1)
        gen[cromosoma] = 1 if gen[cromosoma] == 0 else 0
    return gen

def elimina_peores_genes(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    for _ in range(2):
        i = adaptacion.index(min(adaptacion))
        del poblacion[i]
        del adaptacion[i]

def mejor_gen(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    return poblacion[adaptacion.index(max(adaptacion))]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
