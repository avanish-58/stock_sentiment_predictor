
const express=require("express");
const app=express();



app.get("/",(req,res)=>{
    res.sendFile(__dirname+"/index.html");

      res.sendFile(__dirname+"/index.js");
    });
    
    app.listen("3000",()=>{
        console.log("chal rha");
    });
    