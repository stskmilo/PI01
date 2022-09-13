from fastapi import FastAPI
#from tkinter import *
#from tkinter import ttk
from respuestas import responder
import uvicorn

app = FastAPI(title='PI01',
            description='Primer proyecto individual',
            version='1.0.0')


@app.get('/')
async def index():
    prueba = {'Pregunta 1': 'Año con más carreras',
            'Pregunta 2': 'Piloto con mayor cantidad de primeros puestos',
            'Pregunta 3': 'Nombre del circuito más corrido',
            'Pregunta 4': 'Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British'}
    return prueba


@app.get('/pregunta/{id}')
async def respuesta(id):
    return responder(id)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload