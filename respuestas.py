import pandas as pd
df_races = pd.read_csv('Datasets/races.csv', index_col='raceId')
df_results = pd.read_json('Datasets/results.json', lines=True)
df_drivers = pd.read_json('Datasets/drivers.json', lines = True)
df_circuits = pd.read_csv('Datasets/circuits.csv', index_col='circuitId')
df_constructors = pd.read_json('Datasets/constructors.json', lines = True)
df_drivers = pd.read_json('Datasets/drivers.json', lines = True)
df_pit_stops = pd.read_json('Datasets/pit_stops.json')

def responder(int):
    if int=='1':
        df_test = df_races.groupby(['year']).agg('count').reset_index().max()
        #return f'Año con mas carreras es {df_test[0]} con {df_test[1]} carreras'
        return ({'Anio': df_test[0].tolist(), 'Carreras': df_test[1].tolist()})
    elif int=='2':
        df_resdri = df_results.merge(df_drivers, on='driverId', how='left')
        df_resdri = df_resdri[['driverRef' , 'positionOrder']]

        resultado = df_resdri[df_resdri['positionOrder']==1].groupby(['driverRef']).agg('count')
        resultado = resultado.sort_values(by='positionOrder',ascending=False).reset_index()
        ganador = resultado['driverRef'][0]
        victorias = resultado['positionOrder'][0]
        #return f'{ganador} es el piloto con mayor cantidad de primeros puestos, con {victorias} primeros puestos'
        return {'ganador':ganador, 'victorias':victorias.tolist()}
    elif int=='3':
        circuito_popular = df_results[['raceId']]
        circuito_popular = circuito_popular.merge(df_races, on='raceId', how='left')
        circuito_popular = circuito_popular[['raceId', 'circuitId']].drop_duplicates()

        circuito_popular = circuito_popular.groupby(['circuitId']).agg('count')
        circuito_popular = circuito_popular.sort_values(by='raceId', ascending=False).reset_index()
        circuito_popular = circuito_popular.merge(df_circuits, on='circuitId', how='left')
        circuito_popular = circuito_popular[['raceId','circuitRef','name']]
        circuito_ganador = circuito_popular['name'][0]
        cantidad_carreras = circuito_popular['raceId'][0]
        #print(f'Circuito mas popular: {circuito_ganador}')
        #print(f'Cantidad carreras realizadas en circuito: {cantidad_carreras}')
        return {'Circuito': circuito_ganador, 'Carreras': cantidad_carreras.tolist()}
    elif int=='4':
        puntos = df_results[['driverId','constructorId','points']]
        puntos = puntos.merge(df_constructors, on='constructorId', how='left')
        puntos = puntos[(puntos['nationality']=='American') | (puntos['nationality']=='British')]
        puntos = puntos[['driverId','points']]
        puntos = puntos.groupby(['driverId']).agg('sum')
        puntos = puntos.sort_values(by='points', ascending=False).reset_index()
        puntos = puntos.merge(df_drivers, on='driverId', how='left')
        piloto_ganador = puntos['name'][0]['forename'] + ' ' + puntos['name'][0]['surname']
        puntaje_ganador = puntos['points'][0]
        #print(f'{piloto_ganador} es el piloto con mayor puntaje, con {puntaje_ganador:.0f} puntos')
        return {'Piloto':piloto_ganador, 'Puntaje':puntaje_ganador}
    else:
        return 'Pregunta inexistente'