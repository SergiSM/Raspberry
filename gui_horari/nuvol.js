var Connection = require('tedious').Connection;
var Request = require('tedious').Request;

var mysql = require('mysql');   //npm install mysql dins del directori on hi ha el script
//https://www.w3schools.com/nodejs/nodejs_mysql.asp

var config = 
{
    userName: 'admin-sql', 
    password: '', 
    server: '', 
    options: 
    {
        database: 'sp_proves_remotes', encrypt: true
    }
}

var connection = new Connection(config);

// Attempt to connect and execute queries if connection goes through
connection.on('connect', function(err) 
{
    if (err) 
    {
        console.log(err)
    }
else
    {            
        queryDatabase()
    }
});

function queryDatabase()
{ 
    console.log('Reading rows from the Table...');

    var con = mysql.createConnection({
        host: "",
        user: "",
        password: "",
        database: ""
      });
      
      con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");
        /*var sql = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
        con.query(sql, function (err, result) {
          if (err) throw err;
          console.log("1 record inserted");
        });*/
    });
    
    request = new Request(
        "SELECT dades FROM ap_ad",
            function(err, rowCount, rows) 
            {
                console.log(rowCount + ' row(s) returned');
                process.exit();
            }
        );

    request.on('row', function(columns) {
        var s ="";
    columns.forEach(function(column) {
            s = s + ", ('123', '"+column.value+"', '2018-10-10 13:46:07')"
            //console.log("%s\t%s", column.metadata.colName, column.value);        
            /*var sql = "INSERT INTO proves.ap_ad (serial_number, dades, dia_hora) VALUES ('123', '"+column.value+"', '2018-10-10 13:46:07')"
            console.log("%s", sql);        
            con.query(sql, function (err, result) {
            if (err) throw err;
            console.log("1 record inserted");
            });*/
        });

        s = s.substring(1);  //trec la primera coma
        var sql = "INSERT INTO proves.ap_ad (serial_number, dades, dia_hora) VALUES "+s;
        console.log("%s", sql);        
        /*con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("1 record inserted");
        })*/;


        });
    connection.execSql(request);
}
