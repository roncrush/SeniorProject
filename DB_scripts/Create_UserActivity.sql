CREATE TABLE IF NOT EXISTS `mydb`.`UserActivity` (
  `userid` INT NOT NULL,
  `activityid` INT NOT NULL,
  `private_application` TINYINT(1) NULL,
  PRIMARY KEY (`userid`, `activityid`))
ENGINE = InnoDB
COMMENT = 'This is a Association entity, since Activity - User is a man' /* comment truncated */ /*y to many relationship, use this to find activities and users matching.
To find activities for a user, do something like: SELECT FROM UserActivity WHERE USER.id = X
To find users on a specific activity, do something like: SELECT FROM UserActivity WHERE Activity.id = X*/