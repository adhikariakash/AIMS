create_table = '''CREATE TABLE if not exists `login` (
                                                    `username`	TEXT NOT NULL UNIQUE,
                                                    `password`	TEXT NOT NULL,
                                                    `role_name`	TEXT NOT NULL,
                                                    `role_id`	TEXT NOT NULL,
                                                    `created_at`	TEXT NOT NULL,
                                                    `updated_at`	TEXT,
                                                    `delete_value`	TEXT,
                                                    PRIMARY KEY(`role_id`,`username`)
                                                );
                 CREATE TABLE if not exists `employee` (
                                                    `role_id`	TEXT NOT NULL,
                                                    `working_zone`	TEXT,
                                                    `name`	TEXT,
                                                    `phone_number`	INTEGER,
                                                    `deleted`	TEXT
                                                );
                CREATE TABLE if not exists `complains` (
                                                    `complain_id`	TEXT NOT NULL,
                                                    `description`	TEXT,
                                                    `working_zone`	TEXT NOT NULL,
                                                    `role_id`	TEXT NOT NULL,
                                                    `status`	TEXT,
                                                    `created_at`	TEXT NOT NULL,
                                                    `delete_value`	TEXT,
                                                    `verdict`	TEXT,
                                                    `complain_type`	TEXT,
                                                    PRIMARY KEY(`complain_id`)
                                                );
                CREATE TABLE if not exists  `supervising_team` (
                                                    `team_id`	TEXT NOT NULL,
                                                    `role_ids`	TEXT NOT NULL,
                                                    `complain_id`	TEXT NOT NULL,
                                                    `created_at`	TEXT NOT NULL,
                                                    `updated_at`	TEXT,
                                                    `delete_value`	TEXT,
                                                    `password`	TEXT NOT NULL,
                                                    `team_name`	TEXT NOT NULL UNIQUE
                                                );
                CREATE TABLE if not exists `final_report` (
                                                    `report_id`	TEXT NOT NULL,
                                                    `complain_id`	TEXT NOT NULL,
                                                    `date_of_accident`	TEXT,
                                                    `injured_people`	INTEGER,
                                                    `dead_people`	INTEGER,
                                                    `short_description`	TEXT,
                                                    `root_cause`	TEXT,
                                                    `feedback`	TEXT,
                                                    `created_at`	TEXT NOT NULL,
                                                    PRIMARY KEY(`report_id`)
                                                );'''
