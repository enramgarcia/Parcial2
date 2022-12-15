# Parcial 2


Script de python para poder generar un API REST sencillo que usa un archivo JSON con la data requerida de vacunación contra el sarampión en niños entre 12-23 meses en Panamá.


## Endpoints

| Endpoint         |Metodo| Descripcion                                                                                                           |
|------------------| ------ |-----------------------------------------------------------------------------------------------------------------------|
| /                |GET| Index principal que muestra un JSON de todos los años.                                                                |
| /{year}          |GET| Busca un año especifico y retorna la información en un JSON, de no encontrarse se retorna un JSON vació con HTTP 404. |
