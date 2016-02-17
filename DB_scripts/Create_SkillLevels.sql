CREATE TABLE IF NOT EXISTS `mydb`.`SkillLevels` (
  `id` INT NOT NULL,
  `skill` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB
COMMENT = 'This is the table containing the codes for the skill levels,' /* comment truncated */ /* adding or removing a skill level should be as simple as updating this table.*/