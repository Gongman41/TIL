CREATE TABLE songs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title  VARCHAR(50) NOT NULL,
  artist  VARCHAR(50) NOT NULL,
  album VARCHAR(50) NOT NULL,
  genre  VARCHAR(50) NOT NULL,
  duration INTEGER
  );

INSERT INTO
  songs (title,artist,album,genre,duration)
VALUES
  ('title1','artist1','album1','genre1','duration1'),
  ('title2','artist2','album2','genre2','duration2'),
  ('title3','artist3','album3','genre3','duration3'),
  ('title4','artist4','album4','genre4','duration4'),
  ('title5','artist5','album5','genre5','duration5');

UPDATE songs
SET title = 'title10'
WHERE id = 1;
