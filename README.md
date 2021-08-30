# BasicApi-Fastapi-mongo

## Con docker-compose

Tienes que crear un archivo .env en el root y en este archivo asignarle un valor a la variable MONGO_INITDB_ROOT_PASSWORD

Luuego tienes que conseguir los datos: https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo, crear una base de datos "olimpiadas" y dos colecciones 
"Athletes" y "User". Cargar los datos del archivo csv en Athletes y crear un usuario con email y contraseña. Me hubiera gustado incluir la base de datos en el 
repositorio pero generaba muchos errores y por eso la exclui.

En el archivo traefik.toml cambia la linea 20 y usa tu correo.
En el archivo docker-compose.yml cambia la linea 13 e introduce tu el nombre de tu dominio (recomendable api.tudominio.com)

Ejecuta:
```
docker-compose up --build
```

Ahora ve al dominio que pusiste en el docker-compose, puedes ir a tudominio.com/docs para ver la documentacion. Tienes que autenticarte con tu correo y contraseña.
