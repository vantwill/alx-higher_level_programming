-- cities by states -addiss ababa
SELECT c.id, c.name, s.name FROM cities c, states s
WHERE c.state_id = s.id
GROUP BY c.id ASC;
