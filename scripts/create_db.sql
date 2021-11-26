CREATE DATABASE blockchain_account_lookup;
\c blockchain_account_lookup;


-- Create extension for UUID Generation. Postgres does not support 
-- this by default. 
CREATE EXTENSION IF NOT EXISTS 'uuid-ossp';

DROP TABLE users;
CREATE TABLE users(
	ID SERIAL PRIMARY KEY     NOT NULL,
	USER_ID uuid DEFAULT uuid_generate_v4(), 
	EMAIL VARCHAR(50) UNIQUE, 
	PASSWORD_HASH VARCHAR(128) NOT NULL
);

DROP TABLE user_accounts;
CREATE TABLE user_accounts(
	ID SERIAL PRIMARY KEY     NOT NULL,
	USER_ID INTEGER NOT NULL, 
	ACCOUNT_ID VARCHAR(64), 
	ASSET_TYPE VARCHAR(5)
);

-- -- Sample User 
-- INSERT INTO users(email, first_name, last_name) VALUES (
-- 	'rodneywells01@gmail.com', 
-- 	'Rodney', 
-- 	'Wells'
-- );


-- -- Sample Inventory 
-- INSERT INTO inventory(user_id, item_name, qty_percentage_remaining)
-- VALUES (
-- 	'123',
-- 	'Toilet Paper',
-- 	1.0 
-- );


-- INSERT INTO inventory(user_id, item_name, qty_percentage_remaining)
-- VALUES (
-- 	'1238092183',
-- 	'Tissues',
-- 	0.5
-- );

-- INSERT INTO domain (name, category, photo_url, description) 
-- VALUES 
-- (
-- 	'facebook',
-- 	'Cancer',
-- 	'https://www.facebook.com/images/fb_icon_325x325.png',
-- 	'This shit sucks your soul dry.'
-- );





