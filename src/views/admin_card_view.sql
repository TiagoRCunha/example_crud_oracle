DROP VIEW admin_card_view;
CREATE VIEW admin_card_view AS (
    SELECT c.id,
        c."name" AS "nome",
        c."number" AS "numero",
        c."image" AS "imagem",
        bd.id AS "borda_id",
        bd."name" AS "borda_nome",
        bg.id AS "fundo_id",
        bg."name" AS "fundo_nome",
        r."name" AS "raridade",
        a.title AS "album_titulo",
        TO_CHAR(c.created_at, 'dd/mm/yyyy') as "criado_em",
        TO_CHAR(c.updated_at, 'dd/mm/yyyy') as "atualizado_em"
    FROM labdatabase."card" c
    LEFT JOIN labdatabase."border" bd
    ON c.border_id = bd.id
    LEFT JOIN labdatabase."background" bg
    ON c.background_id = bg.id
    LEFT JOIN labdatabase."rarity" r
    ON c.rarity_id = r.id
    INNER JOIN labdatabase."album" a
    ON c.album_id = a.id
) ORDER BY c."name";