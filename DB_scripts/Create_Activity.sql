CREATE TABLE `activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `skill` int(11) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `duration` int(11) DEFAULT NULL,
  `numplayers` int(11) NOT NULL,
  `private` tinyint(1) NOT NULL,
  `available` tinyint(1) NOT NULL,
  `category` int(11) NOT NULL,
  `leader` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `category_idx` (`category`),
  KEY `leader_idx` (`leader`),
  CONSTRAINT `category` FOREIGN KEY (`category`) REFERENCES `activitytype` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `leader` FOREIGN KEY (`leader`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
