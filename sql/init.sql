DROP TABLE IF EXISTS listings;

CREATE TABLE listings (
  listing_id SERIAL NOT NULL,
  listing_address VARCHAR(250) NOT NULL,
  listing_price INT NOT NULL,
  PRIMARY KEY (listing_id)
);

INSERT INTO listings (
    listing_address,
    listing_price
)
VALUES
    ('125 Parkway Dr.', 255000),
    ('1222 Jones Rd.', 135000),
    ('33 Main Street', 245000),
    ('1st Street', 330000),
    ('2nd Dr.', 140000),
    ('3rd Ave.', 555000),
    ('4th Blvd.', 450000),
    ('Madison Avenue', 100000),
    ('Park Ave.', 220000),
    ('Rocky Road', 375000);