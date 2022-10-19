DROP VIEW admin_album_view;
CREATE VIEW admin_album_view AS (
   SELECT a.id,
      a.title AS "titulo",
      a.card_count AS "total_cartas",
      a.page_number AS "total_paginas",
      a."description" as "sobre",
      COUNT(u.id) as "contador_usuarios",
      TO_CHAR(a.created_at, 'dd/mm/yyyy') as "criado_em",
      TO_CHAR(a.updated_at, 'dd/mm/yyyy') as "atualizado_em"
   FROM labdatabase."album" a
   LEFT JOIN labdatabase."user" u
   ON a.id = u.album_id
   GROUP BY a.id, a.title, a.card_count, a.page_number, a."description", 
   a.created_at, a.updated_at
) ORDER BY a.title;