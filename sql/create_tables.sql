CREATE TABLE labdatabase."album" (
    uuid VARCHAR2(40) PRIMARY KEY UNIQUE NOT NULL,
    title VARCHAR2(25) NOT NULL,
    card_count  NUMBER NOT NULL,
    page_number NUMBER NOT NULL,
    description VARCHAR2(255),
    CONSTRAINT album_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."user" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    username VARCHAR2(50) NOT NULL,
    "password"  VARCHAR(255) NOT NULL,
    access_type NUMBER NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."card" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "number" NUMBER NOT NULL,
    "image"  VARCHAR2(155) NOT NULL,
    "name" VARCHAR2(20) NOT NULL,
    CONSTRAINT card_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."border" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "image"  VARCHAR2(155),
    "name" VARCHAR2(20),
    CONSTRAINT border_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."background" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "image"  VARCHAR2(155),
    "name" VARCHAR2(20),
    CONSTRAINT background_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."tag" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "name" VARCHAR2(15) NOT NULL,
    CONSTRAINT tag_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."rarity" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "name" VARCHAR2(15) NOT NULL,
    "tier" NUMBER NOT NULL,
    CONSTRAINT rarity_pk PRIMARY KEY ( uuid )
);

CREATE TABLE labdatabase."rarity" (
    uuid VARCHAR2(40) PRIMARY KEY NOT NULL,
    "name" VARCHAR2(15) NOT NULL,
    "tier" NUMBER NOT NULL,
    CONSTRAINT rarity_pk PRIMARY KEY ( uuid )
);