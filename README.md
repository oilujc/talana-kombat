
# Talana Kombat

## Build

To build the project, run the following command

```bash
  docker-compose build
```

## Run

To run the project, run the following command

```bash
  docker-compose up
```
    
## Usage/Examples

To use the project, run the following command

```bash
  curl -X POST -H "Content-Type: application/json" -d '	{
    		"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},
    		"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}
    }' http://localhost:8100
```


## Running Tests

To run tests, run the following command

```bash
  docker-compose run --rm app pytest
```


## FAQ

#### Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 

Si ya se hizo push le notifica al equipo que se hizo un commit sin el archivo, se agrega el archivo y se hace un nuevo commit, si se desea se puede hacer un rebase para que el commit que falta el archivo se agregue al commit anterior.

Y si no se ha hecho push, se agrega el archivo y se hace un commit.


#### Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado? 

He trabajado con flujo basado en ramas, usando branches para cada feature, y haciendo merge a una rama dev y/o qa y luego a master.

#### ¿Cuál ha sido la situación más compleja que has tenido con esto?  

Cuando se trabaja con un equipo grande, y se tienen muchos features en desarrollo, es difícil mantener el código actualizado y evitar conflictos.

#### Qué experiencia has tenido con los microservicios?   

He migrado un proyecto de monolito a microservicios extendiendo las funcionalidades de este, y he creado algunos microservicios desde cero.

#### ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?   

AWS, es el que más he usado, me parece que tiene una buena documentación y una comunidad muy grande. 
