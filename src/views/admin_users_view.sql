DROP VIEW admin_users_view;

CREATE VIEW admin_users_view AS (
   SELECT u.id,
      u.username AS "nome",
      u.access_type AS "tipo_acesso",
      a.title AS "album",
      COUNT(uc.card_id) AS "contador_cartas",
      u.created_at as "criado_em",
      u.updated_at as "atualizado_em"
   FROM labdatabase."user" u
   LEFT JOIN labdatabase."album" a
   ON a.id = u.album_id
   LEFT JOIN labdatabase."user_card" uc
   ON uc.user_id = u.id
   GROUP BY u.id, u.username, u.access_type, a.title, u.created_at, u.updated_at
) ORDER BY u.username;
