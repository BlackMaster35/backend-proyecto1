-- =====================================================================
-- Evaluación 3 - Programación Backend | Proyecto 26: Sistema de Hotel
-- Script 2/3: CREACIÓN DEL USUARIO DE APLICACIÓN (MySQL 8)
-- Ejecutar como root:  mysql -u root -p < sql/02_crear_usuario.sql
-- La contraseña debe coincidir con DB_PASSWORD del archivo .env
-- =====================================================================

DROP USER IF EXISTS 'hotel_user'@'localhost';

CREATE USER 'hotel_user'@'localhost'
    IDENTIFIED BY 'Hotel2026!';

SELECT user, host FROM mysql.user WHERE user = 'hotel_user';
