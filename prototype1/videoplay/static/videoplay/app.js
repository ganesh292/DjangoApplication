var pg = require('pg');
var conString = "postgres://navnigupta:Navn123@@@@localhost:5432/Elle_hacks";

var client = new pg.Client(conString);
client.connect();
const query = client.query("INSERT INTO Signup(Name, Email, Password) values('username','email','password')");
query.on('end', () => { client.end(); });