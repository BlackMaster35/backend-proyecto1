-- =====================================================================
-- Evaluación 2 - Programación Backend (Django + Django REST Framework)
-- Proyecto 26: Sistema de Hotel
-- Autor: Sebastián Valderrama Concha - INACAP, Analista Programador
-- Motor: MySQL 8
--
-- 1) Creación de la base de datos
-- 2) Creación de un usuario específico para la base de datos
-- 3) Asignación de permisos de esa base de datos a ese usuario
-- 4) Creación de las tablas del modelo de datos
-- =====================================================================


-- ---------------------------------------------------------------------
-- 1) CREACIÓN DE LA BASE DE DATOS
-- ---------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS sistema_hotel
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;


-- ---------------------------------------------------------------------
-- 2) CREACIÓN DEL USUARIO ESPECÍFICO
-- ---------------------------------------------------------------------
CREATE USER IF NOT EXISTS 'hotel_user'@'localhost'
    IDENTIFIED BY 'Hotel2026!';


-- ---------------------------------------------------------------------
-- 3) ASIGNACIÓN DE PERMISOS
--    El usuario solo tiene permisos sobre la base sistema_hotel.
-- ---------------------------------------------------------------------
GRANT ALL PRIVILEGES ON sistema_hotel.* TO 'hotel_user'@'localhost';

FLUSH PRIVILEGES;


-- ---------------------------------------------------------------------
-- 4) TABLAS DEL MODELO DE DATOS (equivalentes a hotel/models.py)
-- ---------------------------------------------------------------------
USE sistema_hotel;

CREATE TABLE IF NOT EXISTS hotel_hotel (
    id         BIGINT            NOT NULL AUTO_INCREMENT,
    nombre     VARCHAR(100)      NOT NULL,
    direccion  VARCHAR(200)      NOT NULL,
    ciudad     VARCHAR(100)      NOT NULL,
    telefono   VARCHAR(20)       NOT NULL,
    estrellas  SMALLINT UNSIGNED NOT NULL DEFAULT 3,
    PRIMARY KEY (id),
    CONSTRAINT chk_hotel_estrellas CHECK (estrellas BETWEEN 1 AND 5)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_tipohabitacion (
    id           BIGINT            NOT NULL AUTO_INCREMENT,
    nombre       VARCHAR(50)       NOT NULL,
    descripcion  LONGTEXT          NOT NULL,
    capacidad    SMALLINT UNSIGNED NOT NULL,
    precio_noche INT UNSIGNED      NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_tipohabitacion_nombre (nombre)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_habitacion (
    id       BIGINT            NOT NULL AUTO_INCREMENT,
    hotel_id BIGINT            NOT NULL,
    tipo_id  BIGINT            NOT NULL,
    numero   VARCHAR(10)       NOT NULL,
    piso     SMALLINT UNSIGNED NOT NULL DEFAULT 1,
    estado   VARCHAR(15)       NOT NULL DEFAULT 'disponible',
    PRIMARY KEY (id),
    UNIQUE KEY habitacion_unica_por_hotel (hotel_id, numero),
    CONSTRAINT fk_habitacion_hotel FOREIGN KEY (hotel_id)
        REFERENCES hotel_hotel (id) ON DELETE CASCADE,
    CONSTRAINT fk_habitacion_tipo FOREIGN KEY (tipo_id)
        REFERENCES hotel_tipohabitacion (id),
    CONSTRAINT chk_habitacion_estado
        CHECK (estado IN ('disponible', 'ocupada', 'mantencion'))
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_huesped (
    id             BIGINT       NOT NULL AUTO_INCREMENT,
    rut            VARCHAR(12)  NOT NULL,
    nombres        VARCHAR(100) NOT NULL,
    apellidos      VARCHAR(100) NOT NULL,
    email          VARCHAR(254) NOT NULL,
    telefono       VARCHAR(20)  NOT NULL,
    fecha_registro DATETIME(6)  NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_huesped_rut (rut),
    UNIQUE KEY uq_huesped_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_recepcionista (
    id        BIGINT       NOT NULL AUTO_INCREMENT,
    hotel_id  BIGINT       NOT NULL,
    rut       VARCHAR(12)  NOT NULL,
    nombres   VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email     VARCHAR(254) NOT NULL,
    activo    BOOLEAN      NOT NULL DEFAULT TRUE,
    PRIMARY KEY (id),
    UNIQUE KEY uq_recepcionista_rut (rut),
    UNIQUE KEY uq_recepcionista_email (email),
    CONSTRAINT fk_recepcionista_hotel FOREIGN KEY (hotel_id)
        REFERENCES hotel_hotel (id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_reserva (
    id                 BIGINT            NOT NULL AUTO_INCREMENT,
    huesped_id         BIGINT            NOT NULL,
    habitacion_id      BIGINT            NOT NULL,
    recepcionista_id   BIGINT            NULL,
    fecha_entrada      DATE              NOT NULL,
    fecha_salida       DATE              NOT NULL,
    cantidad_huespedes SMALLINT UNSIGNED NOT NULL DEFAULT 1,
    estado             VARCHAR(15)       NOT NULL DEFAULT 'pendiente',
    total              INT UNSIGNED      NOT NULL DEFAULT 0,
    creada_en          DATETIME(6)       NOT NULL,
    actualizada_en     DATETIME(6)       NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_reserva_huesped FOREIGN KEY (huesped_id)
        REFERENCES hotel_huesped (id),
    CONSTRAINT fk_reserva_habitacion FOREIGN KEY (habitacion_id)
        REFERENCES hotel_habitacion (id),
    CONSTRAINT fk_reserva_recepcionista FOREIGN KEY (recepcionista_id)
        REFERENCES hotel_recepcionista (id) ON DELETE SET NULL,
    CONSTRAINT chk_reserva_fechas CHECK (fecha_salida > fecha_entrada),
    CONSTRAINT chk_reserva_estado
        CHECK (estado IN ('pendiente', 'confirmada', 'checkin', 'checkout', 'cancelada'))
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS hotel_pago (
    id         BIGINT       NOT NULL AUTO_INCREMENT,
    reserva_id BIGINT       NOT NULL,
    monto      INT UNSIGNED NOT NULL,
    metodo     VARCHAR(15)  NOT NULL,
    fecha_pago DATETIME(6)  NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_pago_reserva FOREIGN KEY (reserva_id)
        REFERENCES hotel_reserva (id) ON DELETE CASCADE,
    CONSTRAINT chk_pago_metodo
        CHECK (metodo IN ('efectivo', 'debito', 'credito', 'transferencia'))
) ENGINE=InnoDB;


-- ---------------------------------------------------------------------
-- VERIFICACIÓN
-- ---------------------------------------------------------------------
SHOW GRANTS FOR 'hotel_user'@'localhost';
SHOW TABLES;
