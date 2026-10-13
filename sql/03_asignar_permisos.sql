-- =====================================================================
-- Evaluación 3 - Programación Backend | Proyecto 26: Sistema de Hotel
-- Script 3/3: ASIGNACIÓN DE PERMISOS (MySQL 8)
-- Ejecutar como root:  mysql -u root -p < sql/03_asignar_permisos.sql
--
-- El usuario de aplicación solo tiene permisos sobre sistema_hotel
-- (principio de mínimo privilegio). Los permisos incluyen lo que Django
-- necesita para operar (CRUD) y para ejecutar migraciones (DDL).
-- =====================================================================

GRANT SELECT, INSERT, UPDATE, DELETE,
      CREATE, ALTER, DROP, INDEX, REFERENCES
    ON sistema_hotel.* TO 'hotel_user'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'hotel_user'@'localhost';
