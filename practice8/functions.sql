DROP FUNCTION IF EXISTS search_contacts1(TEXT) CASCADE;

CREATE FUNCTION search_contacts1(search_pattern TEXT)
RETURNS TABLE(ret_id INT, ret_name TEXT, ret_phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.id, 
        p.name, 
        p.phone
    FROM phonebook p
    WHERE p.name ILIKE ('%' || search_pattern || '%')
       OR p.phone ILIKE ('%' || search_pattern || '%');
END;
$$ LANGUAGE plpgsql;