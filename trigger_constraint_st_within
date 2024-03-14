CREATE OR REPLACE FUNCTION check_within_polygon()
RETURNS TRIGGER AS $$
BEGIN
	IF (
		SELECT
			ST_Within(NEW.geom, ST_Collect(t2.geom))
		FROM t2 AS t2
		GROUP BY NEW.geom
		) IS TRUE
	THEN RETURN NEW;
	ELSE
		RAISE EXCEPTION 'La Géométrie doit être contenue dans celle de t2';
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER constraint_within_polygon
BEFORE INSERT OR UPDATE ON t1
FOR EACH ROW
EXECUTE FUNCTION check_within_polygon();
