CREATE TABLE Country (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(255) NOT NULL,
    Capital VARCHAR(255),
    Population BIGINT,
    Area FLOAT,
    OfficialLanguage VARCHAR(255),
    Currency VARCHAR(255),
    Continent VARCHAR(255),
    GDP BIGINT,
    CallingCode VARCHAR(20),
    FlagURL VARCHAR(1024),
);
