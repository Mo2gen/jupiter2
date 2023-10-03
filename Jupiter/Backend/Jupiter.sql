DROP DATABASE IF EXISTS Jupiter;
CREATE DATABASE IF NOT EXISTS Jupiter CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE Jupiter;

create table if not exists request
(
    PK_timestamp int,
    CurrentTemperature int NOT NULL,
    PRIMARY KEY (PK_timestamp)
);

create table if not exists forecast_hour
(
    PK_timestamp int,
    timestamphour int, 
    Temperature int NOT NULL,
    PRIMARY KEY (PK_timestamp, timestamphour),
    FOREIGN KEY (PK_timestamp) references request(PK_timestamp)
);