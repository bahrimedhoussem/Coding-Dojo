const express = require('express')
const cors = require("cors")
const app = express()
require("dotenv").config()
const port = process.env.PORT 

app.use(express.json(), express.urlencoded({extended : true}) , cors())
require("./config/mongoose.config")

require("./routes/author.route")

app.listen(port , () => {
    console.log("listenning to port" + port );
})