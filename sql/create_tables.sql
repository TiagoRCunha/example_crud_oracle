ALTER TABLE labdatabase."border" DROP CONSTRAINT border_rarity_id_fk;
ALTER TABLE labdatabase."background" DROP CONSTRAINT background_rarity_id_fk;
ALTER TABLE labdatabase."card" DROP CONSTRAINT card_rarity_id_fk;
ALTER TABLE labdatabase."card" DROP CONSTRAINT card_background_id_fk;
ALTER TABLE labdatabase."card" DROP CONSTRAINT card_border_id_fk;
ALTER TABLE labdatabase."card" DROP CONSTRAINT card_album_id_fk;
ALTER TABLE labdatabase."user" DROP CONSTRAINT user_album_id_fk;

ALTER TABLE labdatabase."user_card" DROP CONSTRAINT user_card_card_id_fk;
ALTER TABLE labdatabase."user_card" DROP CONSTRAINT user_card_user_id_fk;
ALTER TABLE labdatabase."card_tag" DROP CONSTRAINT card_tag_card_id_fk;
ALTER TABLE labdatabase."card_tag" DROP CONSTRAINT card_tag_tag_id_fk;
ALTER TABLE labdatabase."border_tag" DROP CONSTRAINT border_tag_border_id_fk;
ALTER TABLE labdatabase."border_tag" DROP CONSTRAINT border_tag_tag_id_fk;
ALTER TABLE labdatabase."background_tag" DROP CONSTRAINT background_tag_tag_id_fk;
ALTER TABLE labdatabase."background_tag" DROP CONSTRAINT background_tag_background_id_fk;

ALTER TABLE labdatabase."user_card" DROP CONSTRAINT card_user_pk;
ALTER TABLE labdatabase."card_tag" DROP CONSTRAINT card_tag_pk;
ALTER TABLE labdatabase."border_tag" DROP CONSTRAINT border_tag_pk;
ALTER TABLE labdatabase."background_tag" DROP CONSTRAINT background_tag_pk;

ALTER TABLE labdatabase."album" DROP CONSTRAINT album_pk;
ALTER TABLE labdatabase."user" DROP CONSTRAINT user_pk;
ALTER TABLE labdatabase."card" DROP CONSTRAINT card_pk;
ALTER TABLE labdatabase."border" DROP CONSTRAINT border_pk;
ALTER TABLE labdatabase."background" DROP CONSTRAINT background_pk;
ALTER TABLE labdatabase."tag" DROP CONSTRAINT tag_pk;
ALTER TABLE labdatabase."rarity" DROP CONSTRAINT rarity_pk;

DROP TABLE labdatabase."album";
DROP TABLE labdatabase."user";
DROP TABLE labdatabase."card";
DROP TABLE labdatabase."border";
DROP TABLE labdatabase."background";
DROP TABLE labdatabase."tag";
DROP TABLE labdatabase."rarity";
DROP TABLE labdatabase."card_tag";
DROP TABLE labdatabase."border_tag";
DROP TABLE labdatabase."background_tag";
DROP TABLE labdatabase."user_card";

DROP SEQUENCE labdatabase.album_id_seq;
DROP SEQUENCE labdatabase.user_id_seq;
DROP SEQUENCE labdatabase.card_id_seq;
DROP SEQUENCE labdatabase.border_id_seq;
DROP SEQUENCE labdatabase.background_id_seq;
DROP SEQUENCE labdatabase.tag_id_seq;
DROP SEQUENCE labdatabase.rarity_id_seq;

CREATE SEQUENCE labdatabase.album_id_seq;
CREATE SEQUENCE labdatabase.user_id_seq;
CREATE SEQUENCE labdatabase.card_id_seq;
CREATE SEQUENCE labdatabase.border_id_seq;
CREATE SEQUENCE labdatabase.background_id_seq;
CREATE SEQUENCE labdatabase.tag_id_seq;
CREATE SEQUENCE labdatabase.rarity_id_seq;

CREATE TABLE labdatabase."album" (
    id NUMBER DEFAULT labdatabase.album_id_seq.NEXTVAL NOT NULL,
    title VARCHAR2(40) NOT NULL,
    card_count  NUMBER NOT NULL,
    page_number NUMBER NOT NULL,
    "description" VARCHAR2(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT album_pk PRIMARY KEY (id)
);

CREATE TABLE labdatabase."user" (
    id NUMBER DEFAULT labdatabase.user_id_seq.NEXTVAL NOT NULL,
    username VARCHAR2(50) NOT NULL,
    "password"  VARCHAR(255) NOT NULL,
    access_type NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT user_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."card" (
    id NUMBER DEFAULT labdatabase.card_id_seq.NEXTVAL NOT NULL,
    "number" NUMBER NOT NULL,
    "image"  VARCHAR2(155) NOT NULL,
    "name" VARCHAR2(40) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT card_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."border" (
    id NUMBER DEFAULT labdatabase.border_id_seq.NEXTVAL NOT NULL,
    "image"  VARCHAR2(155),
    "name" VARCHAR2(40),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT border_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."background" (
    id NUMBER DEFAULT labdatabase.background_id_seq.NEXTVAL NOT NULL,
    "image"  VARCHAR2(155),
    "name" VARCHAR2(40),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT background_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."tag" (
    id NUMBER DEFAULT labdatabase.tag_id_seq.NEXTVAL NOT NULL,
    "name" VARCHAR2(40) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT tag_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."rarity" (
    id NUMBER DEFAULT labdatabase.rarity_id_seq.NEXTVAL NOT NULL,
    "name" VARCHAR2(40) NOT NULL,
    "tier" NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT rarity_pk PRIMARY KEY ( id )
);

CREATE TABLE labdatabase."border_tag" (
    border_id NUMBER NOT NULL,
    tag_id NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT border_tag_pk PRIMARY KEY ( border_id , tag_id ),
    CONSTRAINT border_tag_border_id_fk FOREIGN KEY ( border_id )
    REFERENCES labdatabase."border" (id) ON DELETE CASCADE,
    CONSTRAINT border_tag_tag_id_fk FOREIGN KEY ( tag_id )
    REFERENCES labdatabase."tag" (id) ON DELETE CASCADE
);

CREATE TABLE labdatabase."card_tag" (
    card_id NUMBER NOT NULL,
    tag_id NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT card_tag_pk PRIMARY KEY ( card_id, tag_id ),
    CONSTRAINT card_tag_card_id_fk FOREIGN KEY ( card_id )
    REFERENCES labdatabase."card" (id) ON DELETE CASCADE,
    CONSTRAINT card_tag_tag_id_fk FOREIGN KEY ( tag_id )
    REFERENCES labdatabase."tag" (id) ON DELETE CASCADE
);

CREATE TABLE labdatabase."background_tag" (
    background_id NUMBER NOT NULL,
    tag_id NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT background_tag_pk PRIMARY KEY ( background_id, tag_id ),
    CONSTRAINT background_tag_background_id_fk FOREIGN KEY ( background_id )
    REFERENCES labdatabase."background" (id) ON DELETE CASCADE,
    CONSTRAINT background_tag_tag_id_fk FOREIGN KEY ( tag_id )
    REFERENCES labdatabase."tag" (id) ON DELETE CASCADE
);

CREATE TABLE labdatabase."user_card" (
    card_id NUMBER NOT NULL,
    user_id NUMBER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT card_user_pk PRIMARY KEY ( card_id, user_id ),
    CONSTRAINT user_card_card_id_fk FOREIGN KEY ( card_id )
    REFERENCES labdatabase."card" (id) ON DELETE CASCADE,
    CONSTRAINT user_card_user_id_fk FOREIGN KEY ( user_id )
    REFERENCES labdatabase."user" (id) ON DELETE CASCADE
);

ALTER TABLE labdatabase."user" ADD album_id NUMBER DEFAULT NULL;
ALTER TABLE labdatabase."user" ADD CONSTRAINT user_album_id_fk
    FOREIGN KEY ( album_id ) REFERENCES labdatabase."album" (id) ON DELETE SET NULL;

ALTER TABLE labdatabase."card" ADD (
    background_id NUMBER,
    border_id NUMBER,
    rarity_id NUMBER,
    album_id NUMBER
);
ALTER TABLE labdatabase."card" ADD CONSTRAINT card_background_id_fk
    FOREIGN KEY ( background_id ) REFERENCES labdatabase."background" (id) ON DELETE CASCADE;
ALTER TABLE labdatabase."card" ADD CONSTRAINT card_border_id_fk
    FOREIGN KEY ( border_id ) REFERENCES labdatabase."border" (id) ON DELETE CASCADE;
ALTER TABLE labdatabase."card" ADD CONSTRAINT card_rarity_id_fk
    FOREIGN KEY ( rarity_id ) REFERENCES labdatabase."rarity" (id) ON DELETE CASCADE;
ALTER TABLE labdatabase."card" ADD CONSTRAINT card_album_id_fk
    FOREIGN KEY ( album_id ) REFERENCES labdatabase."album" (id) ON DELETE CASCADE;

ALTER TABLE labdatabase."border" ADD rarity_id NUMBER NOT NULL;
ALTER TABLE labdatabase."border" ADD CONSTRAINT border_rarity_id_fk
    FOREIGN KEY ( rarity_id ) REFERENCES labdatabase."rarity" (id) ON DELETE CASCADE;

ALTER TABLE labdatabase."background" ADD rarity_id NUMBER NOT NULL;
ALTER TABLE labdatabase."background" ADD CONSTRAINT background_rarity_id_fk
    FOREIGN KEY ( rarity_id ) REFERENCES labdatabase."rarity" (id) ON DELETE CASCADE;
