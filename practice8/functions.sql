-- Search by pattern
CREATE OR REPLACE FUNCTION search_contacts1(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated1(lim INT, off INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;