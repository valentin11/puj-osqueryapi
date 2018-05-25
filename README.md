
# OsQueryApi

> Para el 2do proyecto de la materia Desarrollo y Servicios Web de la carrera de Ingeniería en Sistemas y Computación, de la Pontificia Universidad Javeriana Cali, se implementa una API en Flask que a través de Osquery permite hacer consultas especificas sobre el sistema operativo Linux.

## 1. Build Setup

``` bash
# Run bash.sh
$ bash bash.sh
```

## 2. Queries

#### Consultas a nivel de usuarios

 - Permitir consultar que usuarios están logueados en el sistema.
 - Permitir crear un usuario en el sistema.
 - Permitir eliminar un usuario en el sistema.

#### Consultas a nivel de procesos

 - Consultar los procesos que se encuentran ejecutándose en la maquina.
 - Eliminar un proceso.

#### Consultas a nivel de sistema operativo
 - Conocer la versión del sistema operativo.
 - Conocer la versión del Kernel instalado.
 - Conocer la cantidad de memoria que tiene.


#### Consultas a nivel de paquetes instalados
 - Conocer los paquetes instalados en una maquina.
 - Permitir instalar un paquete.
 - Permitir eliminar un paquete.


## 3. Request and Response

### 3.1 A nivel de usuarios

#####  Consultar usuarios logueados.
Método: GET <br/>
URL: http://localhost:5000/api/users/ <br/>
Response:
```json
{
  "users": [
    {
      "description": "root", 
      "directory": "/root", 
      "gid": "0", 
      "gid_signed": "0", 
      "shell": "/bin/bash", 
      "uid": "0", 
      "uid_signed": "0", 
      "username": "root", 
      "uuid": ""
    }, 
    {
      "description": "", 
      "directory": "/nonexistent", 
      "gid": "101", 
      "gid_signed": "101", 
      "shell": "/usr/sbin/nologin", 
      "uid": "101", 
      "uid_signed": "101", 
      "username": "messagebus", 
      "uuid": ""
    }
  ]
}
```

#####  Consultar usuarios logueado por id.
Método: GET <br/>
URL: http://localhost:5000/api/users/0 <br/>
Response:
```json
{
  "users": [
    {
      "description": "root", 
      "directory": "/root", 
      "gid": "0", 
      "gid_signed": "0", 
      "shell": "/bin/bash", 
      "uid": "0", 
      "uid_signed": "0", 
      "username": "root", 
      "uuid": ""
    }
  ]
}
```

#####  Crear usuario.
Método: POST <br/>
URL: http://localhost:5000/api/users <br/>
Request:
```json
{
    "userName":"Valentin",
    "userPass":"666666"
}
```
Response:
```json
{ "result":"Se creó el usuario exitosamente"}
```

##### Eliminar usuario.
Método: DELETE <br/>
URL: http://localhost:5000/api/users/Valentin <br/>
Response:
```json
{ "result":"Se eliminó el usuario exitosamente"}
```

### 3.2 A nivel de procesos

#####  Consultar procesos activos.
Método: GET <br/>
URL: http://localhost:5000/api/processes/ <br/>
Response:
```json
{
  "processes": [
    {
      "cmdline": "python app.py", 
      "cwd": "/app", 
      "disk_bytes_read": "2043904", 
      "disk_bytes_written": "8192", 
      "egid": "0", 
      "euid": "0", 
      "gid": "0", 
      "name": "python", 
      "nice": "0", 
      "on_disk": "1", 
      "parent": "0", 
      "path": "/usr/bin/python2.7", 
      "pgroup": "1", 
      "pid": "1", 
      "resident_size": "21452000", 
      "root": "/", 
      "sgid": "0", 
      "start_time": "29724", 
      "state": "S", 
      "suid": "0", 
      "system_time": "6", 
      "threads": "1", 
      "total_size": "59700000", 
      "uid": "0", 
      "user_time": "16", 
      "wired_size": "0"
    }, 
    {
      "cmdline": "/usr/bin/python app.py", 
      "cwd": "/app", 
      "disk_bytes_read": "12984320", 
      "disk_bytes_written": "0", 
      "egid": "0", 
      "euid": "0", 
      "gid": "0", 
      "name": "python", 
      "nice": "0", 
      "on_disk": "1", 
      "parent": "1", 
      "path": "/usr/bin/python2.7", 
      "pgroup": "1", 
      "pid": "12", 
      "resident_size": "22688000", 
      "root": "/", 
      "sgid": "0", 
      "start_time": "29725", 
      "state": "S", 
      "suid": "0", 
      "system_time": "199", 
      "threads": "2", 
      "total_size": "142528000", 
      "uid": "0", 
      "user_time": "204", 
      "wired_size": "0"
    }
  ]
}
```

#####  Consultar proceso por id.
Método: GET <br/>
URL: http://localhost:5000/api/processes/1 <br/>
Response:
```json
{
  "processes": [
    {
      "cmdline": "python app.py", 
      "cwd": "/app", 
      "disk_bytes_read": "2043904", 
      "disk_bytes_written": "8192", 
      "egid": "0", 
      "euid": "0", 
      "gid": "0", 
      "name": "python", 
      "nice": "0", 
      "on_disk": "1", 
      "parent": "0", 
      "path": "/usr/bin/python2.7", 
      "pgroup": "1", 
      "pid": "1", 
      "resident_size": "21456000", 
      "root": "/", 
      "sgid": "0", 
      "start_time": "29724", 
      "state": "S", 
      "suid": "0", 
      "system_time": "6", 
      "threads": "1", 
      "total_size": "59700000", 
      "uid": "0", 
      "user_time": "16", 
      "wired_size": "0"
    }
  ]
}
```

##### Eliminar proceso.
Método: DELETE <br/>
URL: http://localhost:5000/api/processes/1 <br/>
Response:
```json
{ "result":"Se eliminó el proceso exitosamente"}
```

### 3.3 A nivel de sistema operativo

### 3.4 A nivel de paquetes instalados