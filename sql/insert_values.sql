BEGIN
INSERT INTO LABDATABASE."album" (id, title, card_count, page_number, "description") VALUES(album_id_seq.NEXTVAL, 'Copa do Mundo 2022', 150, 15, 'Album copa do mundo 2022');
INSERT INTO LABDATABASE."album" (id, title, card_count, page_number, "description") VALUES(album_id_seq.NEXTVAL, 'Harry Potter', 15, 3, 'Album Harry Potter 2022');
INSERT INTO LABDATABASE."album" (id, title, card_count, page_number, "description") VALUES(album_id_seq.NEXTVAL, 'Pokemon', 50, 5, 'Album Pokemon 2022');


INSERT INTO LABDATABASE."rarity" (id, "name", "tier") VALUES(rarity_id_seq.NEXTVAL, 'common', '1');
INSERT INTO LABDATABASE."rarity" (id, "name", "tier") VALUES(rarity_id_seq.NEXTVAL, 'uncommon', '2');
INSERT INTO LABDATABASE."rarity" (id, "name", "tier") VALUES(rarity_id_seq.NEXTVAL, 'rare', '3');
INSERT INTO LABDATABASE."rarity" (id, "name", "tier") VALUES(rarity_id_seq.NEXTVAL, 'epic', '4');
INSERT INTO LABDATABASE."rarity" (id, "name", "tier") VALUES(rarity_id_seq.NEXTVAL, 'legendary', '5');
END;

--

DECLARE
    ID_SEARCH NUMBER;
    BACKGROUND_ID_SEARCH NUMBER;
    BORDER_ID_SEARCH NUMBER;
    RARITY_ID_SEARCH NUMBER;
    ALBUM_ID_SEARCH NUMBER;
BEGIN

SELECT id INTO ID_SEARCH FROM labdatabase."album" WHERE title = 'Copa do Mundo 2022';
INSERT INTO LABDATABASE."user" (id, username, "password", access_type, album_id) VALUES(user_id_seq.NEXTVAL, 'Henrique', '0001', 0, ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."album" WHERE title = 'Harry Potter';
INSERT INTO LABDATABASE."user" (id, username, "password", access_type, album_id) VALUES(user_id_seq.NEXTVAL, 'Victor', '0002', 0, ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."album" WHERE title = 'Pokemon';
INSERT INTO LABDATABASE."user" (id, username, "password", access_type, album_id) VALUES(user_id_seq.NEXTVAL, 'Tiago', '0003', 1, ID_SEARCH);


SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'common';
INSERT INTO LABDATABASE."border" (id, "image", "name", rarity_id) VALUES(border_id_seq.NEXTVAL, 'border_white.png', 'White Border', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'uncommon';
INSERT INTO LABDATABASE."border" (id, "image", "name", rarity_id) VALUES(border_id_seq.NEXTVAL, 'border_green.png', 'Green Border', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'rare';
INSERT INTO LABDATABASE."border" (id, "image", "name", rarity_id) VALUES(border_id_seq.NEXTVAL, 'border_blue.png', 'Blue Border', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'epic';
INSERT INTO LABDATABASE."border" (id, "image", "name", rarity_id) VALUES(border_id_seq.NEXTVAL, 'border_purple.png', 'Purple Border', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'legendary';
INSERT INTO LABDATABASE."border" (id, "image", "name", rarity_id) VALUES(border_id_seq.NEXTVAL, 'border_red.png', 'Red Border', ID_SEARCH);


SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'common';
INSERT INTO LABDATABASE."background" (id, "image", "name", rarity_id) VALUES(background_id_seq.NEXTVAL, 'background_normal.pnf', 'Normal Background', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'uncommon';
INSERT INTO LABDATABASE."background" (id, "image", "name", rarity_id) VALUES(background_id_seq.NEXTVAL, 'background_matte.pnf', 'Matte Background', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'rare';
INSERT INTO LABDATABASE."background" (id, "image", "name", rarity_id) VALUES(background_id_seq.NEXTVAL, 'background_transparent.pnf', 'Transparent Background', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'epic';
INSERT INTO LABDATABASE."background" (id, "image", "name", rarity_id) VALUES(background_id_seq.NEXTVAL, 'background_reflective.pnf', 'Reflective Background', ID_SEARCH);
SELECT id INTO ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'legendary';
INSERT INTO LABDATABASE."background" (id, "image", "name", rarity_id) VALUES(background_id_seq.NEXTVAL, 'background_metallic.pnf', 'Metallic Background', ID_SEARCH);


SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Reflective Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Purple Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'epic';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Copa do Mundo 2022';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 1, 'messi.png', 'Lionel Messi', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Metallic Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Red Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'legendary';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Copa do Mundo 2022';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 2, 'neymar.png', 'Neymar Junior', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Transparent Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Blue Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'rare';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Copa do Mundo 2022';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 3, 'cristiano_ronaldo.png', 'Cristiano Ronaldo', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Metallic Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Red Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'legendary';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Pokemon';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 1, 'pikachu.png', 'Pikachu', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Reflective Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Purple Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'epic';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Pokemon';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 2, 'charmander.png', 'Charmander', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Normal Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'White Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'common';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Pokemon';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 3, 'bulbasaur.png', 'Bulbasaur', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Metallic Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Red Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'legendary';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Harry Potter';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 1, 'harry.png', 'Harry Potter', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Reflective Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Purple Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'epic';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Harry Potter';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 2, 'hermione.png', 'Hermione Granger', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

SELECT id INTO BACKGROUND_ID_SEARCH FROM labdatabase."background" WHERE "name" = 'Matte Background';
SELECT id INTO BORDER_ID_SEARCH FROM labdatabase."border" WHERE "name" = 'Green Border';
SELECT id INTO RARITY_ID_SEARCH FROM labdatabase."rarity" WHERE "name" = 'uncommon';
SELECT id INTO ALBUM_ID_SEARCH FROM labdatabase."album" WHERE title = 'Harry Potter';
INSERT INTO LABDATABASE."card" (id, "number", "image", "name", background_id, border_id, rarity_id, album_id) VALUES(card_id_seq.NEXTVAL, 3, 'rony.png', 'Rony Weasley', BACKGROUND_ID_SEARCH, BORDER_ID_SEARCH, RARITY_ID_SEARCH, ALBUM_ID_SEARCH);

INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Mid');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Attacker');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Water');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Grass');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Fire');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Poison');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Flying');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Normal');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Electric');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Dragon');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Ice');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Stone');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Wizard');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Elf');
INSERT INTO LABDATABASE."tag" (id, "name") VALUES (tag_id_seq.NEXTVAL, 'Death Eaters');

COMMIT;
END;