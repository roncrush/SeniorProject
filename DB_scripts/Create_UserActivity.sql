CREATE TABLE `useractivity` (
  `userid` int(11) NOT NULL,
  `activityid` int(11) NOT NULL,
  `private_application` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`userid`,`activityid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This is a Association entity, since Activity - User is a many to many relationship, use this to find activities and users matching.\nTo find activities for a user, do something like: SELECT FROM UserActivity WHERE USER.id = X\nTo find users on a specific activity, do something like: SELECT FROM UserActivity WHERE Activity.id = X';
