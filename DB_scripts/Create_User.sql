CREATE TABLE IF NOT EXISTS `mydb`.`User` (
  `id` INT NOT NULL,
  `uname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  `passwd` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(12) NULL,
  `fn` VARCHAR(45) NULL,
  `ln` VARCHAR(45) NULL,
  `admin` TINYINT(1) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `uname_UNIQUE` (`uname` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB
COMMENT = 'The Table for user info'