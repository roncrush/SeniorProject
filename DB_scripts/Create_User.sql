CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `passwd` varchar(45) NOT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `fn` varchar(45) DEFAULT NULL,
  `ln` varchar(45) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  `suspension` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `uname_UNIQUE` (`uname`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='The Table for user info';
