CREATE TABLE IF NOT EXISTS `mydb`.`Activity` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `skill` INT NOT NULL,
  `datetime` DATETIME NOT NULL,
  `duration` INT NULL,
  `numplayers` INT NOT NULL,
  `private` TINYINT(1) NOT NULL,
  `available` TINYINT(1) NOT NULL,
  `category` INT NOT NULL,
  `leader` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `category_idx` (`category` ASC),
  INDEX `skill_idx` (`skill` ASC),
  INDEX `leader_idx` (`leader` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  CONSTRAINT `category`
    FOREIGN KEY (`category`)
    REFERENCES `mydb`.`ActivityType` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `skill`
    FOREIGN KEY (`skill`)
    REFERENCES `mydb`.`SkillLevels` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `leader`
    FOREIGN KEY (`leader`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB