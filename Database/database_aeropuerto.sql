-- CREAR TABLAS DE LA BASE DE DATOS
---------------------------------------------------------
-- Tabla avión
create table avion 
(id_avion varchar, tipo_avion varchar, capacidad float);
alter table avion add cod_modelo varchar;

-- Tabla modelo
create table modelo
(tipo_propulsion varchar, peso_nominal float, descripcion text);

alter table modelo add cod_modelo varchar;

-- Tabla vuelo
create table vuelo
(tipo_vuelo varchar, fecha_vuelo date, hora_vuelo time);

alter table vuelo add id_vuelo varchar;
alter table vuelo add id_avion varchar;
alter table vuelo add nit_aerolinea varchar;
alter table vuelo add id_piloto float;

-- Tabla aerolinea
create table aerolinea
(nom_aerolinea varchar, dir_aerolinea varchar);

alter table aerolinea add nit_aerolinea varchar;

-- Tabla telefono y correo aerolinea
create table tel_aerolinea
(telef_aerolinea integer);

alter table tel_aerolinea add nit_aerolinea varchar;

create table cor_aerolinea
(correo_aerolinea varchar);

alter table cor_aerolinea add nit_aerolinea varchar;

-- Tabla piloto
create table piloto
(id_licencia varchar, nom_piloto varchar, ape_piloto varchar,  horas_vuelo integer, fecha_revmed date);

alter table piloto add id_piloto float;

-- Tablas telefono y correo de piloto
create table tel_piloto
(telef_piloto integer);

alter table tel_piloto add id_piloto float;

create table cor_piloto
(correo_piloto varchar);

alter table cor_piloto add id_piloto float;

-- Tabla alquiler 
create table alquiler 
(hora_alquiler time, fecha_alquiler date, costo_base integer);

alter table alquiler add id_avion varchar;
alter table alquiler add cod_hangar varchar;

-- Tabla hangar
create table hangar 
(ubicacion_hg varchar, capacidad_hg float);

alter table hangar add cod_hangar varchar;

-- Tabla factura
create table factura
(fecha_entrada date, hora_entrada time, fecha_salida date, hora_salida time, valor_total integer);

alter table factura add num_factura varchar;
alter table factura add cod_hangar varchar;

-- Tabla Usuario 
create table Usuario
(nom_usuario varchar, ape_usuario varchar, correo_usu varchar, contraseña_usu varchar, tel_usuario integer, tipo_cuenta integer);

alter table Usuario add id_usuario float;

-- ======================================================================================================
-- RESTRICCIONES DE LA TABLA
-------------------------------------------------------------
-- PRIMARY KEY
-------------------------------------------------------------
alter table aerolinea add primary key (nit_aerolinea);
alter table alquiler add primary key (id_avion, cod_hangar);
alter table avion add primary key (id_avion);
alter table cor_aerolinea add primary key (nit_aerolinea);
alter table cor_piloto add primary key (id_piloto);
alter table factura add primary key (num_factura);
alter table hangar add primary key (cod_hangar);
alter table modelo add primary key (cod_modelo);
alter table piloto add primary key (id_piloto);
alter table tel_aerolinea add primary key (nit_aerolinea);
alter table tel_piloto add primary key (id_piloto);
alter table usuario add primary key (id_usuario);
alter table vuelo add primary key (id_vuelo);
-------------------------------------------------------------------
-- FOREIGN KEY
alter table avion add foreign key (cod_modelo) references modelo; 
alter table vuelo add foreign key (id_piloto) references piloto; 
alter table vuelo add foreign key (id_avion) references avion; 
alter table vuelo add foreign key (nit_aerolinea) references aerolinea; 
alter table factura add foreign key (cod_hangar) references hangar; 
alter table aerolinea drop dir_aerolinea;




