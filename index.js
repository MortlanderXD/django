const express = require("express");
const mysql = require("mysql");
const port = process.env.PORT || 5000
// http://localhost:5000/

<<<<<<< HEAD
const app = express();
=======
// const app = express();

// ++

// app.get('/',(req,res)=>{
//     const conn = mysql.createConnection({
//         host: 'localhost',
//         user: 'root',
//         password: '',
//         database: 'tryit',
//     })
//     conn.connect((err)=>{
//         if(err){
//             console.error('error :'+err.stack)
//             return
//         }
//         console.log('gg mon gars')
//     })
//     conn.query('SELECT * FROM tryagain',(err, rows,fields)=>{
//         if(err){
//             throw err
//         }
//         res.json(rows)
//     })
// })
>>>>>>> 3e8dc226f52b55a54a927c2d23d851525e7780e8

app.get('/',(req,res)=>{
    const conn = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'tryit',
    })
    conn.connect((err)=>{
        if(err){
            console.error('error :'+err.stack)
            return
        }
        console.log('gg mon gars')
    })
    conn.query('SELECT * FROM tryagain',(err, rows,fields)=>{
        if(err){
            throw err
        }
        res.json(rows)
    })
})

app.listen(port,()=>{
    console.log("online")
})


