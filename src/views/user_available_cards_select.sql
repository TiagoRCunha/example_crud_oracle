SELECT ca.id,
    ca."name" AS "nome",
    ca."number" AS "numero",
    ca."image" AS "imagem",
    a.title AS "album_titulo",
    TO_CHAR(ca.created_at, 'dd/mm/yyyy') as "criado_em",
    TO_CHAR(ca.updated_at, 'dd/mm/yyyy') as "atualizado_em"
    FROM "card" ca
    INNER JOIN "album" a ON ca.album_id = a.id
    WHERE ca.id NOT IN (
        SELECT c.id FROM "card" c
        LEFT OUTER JOIN "user_card" uc ON uc.card_id = c.id
        LEFT OUTER JOIN "user" u ON u.id = uc.user_id
        WHERE u.id = :1)