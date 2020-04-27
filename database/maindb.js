const pg = require('pg');
const pool = new pg.Pool({
user: 'root',
host: '127.0.0.1',
database: 'softwater',
password: 'tts',
port: '5454'});

pool.query('SELECT NOW()', (err, res) => {
  console.log(err, res);
  pool.end();
});