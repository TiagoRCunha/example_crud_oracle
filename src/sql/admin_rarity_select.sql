SELECT id,
	"name" AS "nome",
	"tier" AS "nível",
	TO_CHAR(created_at, 'dd/mm/yyyy') AS "criado_em",
	TO_CHAR(updated_at, 'dd/mm/yyyy') AS "atualizado_em"
FROM "rarity"
ORDER BY "tier", "name"