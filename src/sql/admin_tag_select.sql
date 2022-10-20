SELECT id,
	"name" AS "nome",
	TO_CHAR(created_at, 'dd/mm/yyyy') AS "criado_em",
	TO_CHAR(updated_at, 'dd/mm/yyyy') AS "atualizado_em"
FROM "tag"
ORDER BY "name"