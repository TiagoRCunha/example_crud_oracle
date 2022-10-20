SELECT b.id,
    b."name" AS "nome",
    b."image" AS "imagem",
    r."name" AS "raridade",
    TO_CHAR(b.created_at, 'dd/mm/yyyy') as "criado_em",
    TO_CHAR(b.updated_at, 'dd/mm/yyyy') as "atualizado_em"
FROM "border" b
    INNER JOIN "rarity" r ON b.rarity_id = r.id
ORDER BY b."name"