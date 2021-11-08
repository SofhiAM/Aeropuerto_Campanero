-- Borrar de la tabla avión
-- cod_modelom propulsión, peso, num_motores

-- Borrar columna descripción
alter table modelo add descripcion varchar;

-- Agregar columna num_motores en modelo
alter table modelo add num_motores integer;
-- Borrar columna num_motores en avion
alter table avion drop num_motores;

-- Consultar avión
select
id_avion, tipo_avion, descripcion, tipo_propulsion, capacidad, peso_nominal, num_motores
from
(avion join modelo on avion.cod_modelo = modelo.cod_modelo)

-- Seleccionar avión (De donde se hace la consulta se manda el id como texto)
select
id_avion, tipo_avion, descripcion, tipo_propulsion, capacidad, peso_nominal, num_motores
from 
(avion join modelo on avion.cod_modelo = modelo.cod_modelo)
where
id_avion = '890'

-- Los modelos de los aviones van a estar guardados por defecto.
-- Buscar código de avión
select
cod_avion
from modelo
where descripcion = 'Boing 345'



