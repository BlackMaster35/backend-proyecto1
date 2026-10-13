-- =====================================================================
-- Evaluación 3 - Programación Backend | Proyecto 26: Sistema de Hotel
-- Script 1/3: CREACIÓN DE LA BASE DE DATOS (MySQL 8)
-- Ejecutar como root:  mysql -u root -p < sql/01_crear_base_datos.sql
-- =====================================================================

DROP DATABASE IF EXISTS sistema_hotel;

CREATE DATABASE sistema_hotel
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

SHOW DATABASES LIKE 'sistema_hotel';
