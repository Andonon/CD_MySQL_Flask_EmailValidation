-- MySQL Script generated by MySQL Workbench
-- Thu Jun 15 06:25:46 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema emailvalidation
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `emailvalidation` ;

-- -----------------------------------------------------
-- Schema emailvalidation
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `emailvalidation` DEFAULT CHARACTER SET utf8 ;
USE `emailvalidation` ;

-- -----------------------------------------------------
-- Table `emailvalidation`.`emails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `emailvalidation`.`emails` ;

CREATE TABLE IF NOT EXISTS `emailvalidation`.`emails` (
  `id` INT NOT NULL,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;