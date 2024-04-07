import express from 'express';
import bodyParser from 'body-parser';
const app = express();
const cors = require('cors');
const port = 3000;

const corsOptions = {
  origin: '*', // Replace with your allowed origin
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
  optionsSuccessStatus: 204,
};

app.use(bodyParser.text());
app.use(cors(corsOptions));
app.options('/coupon', cors(corsOptions)); // Enable preflight for a specific route

app.post('/coupon', cors(corsOptions), (req,res) => {
  const data: string = req.body as string;
  const language: string = data.substring(0, 2);
  const guid: string = data.substring(2);
  res.setHeader('Content-Type', 'text/plain');
  console.log(guid[14]);
  if(guid[14]=="4"){
    if (language === 'fr') {
      res.status(200).send("Quel beau code sécuritaire. Vous gagnez 2 hamburgers gratuits!");
    }
    else {
      res.status(200).send("What a beautiful secure code. You win 2 free hamburgers!");
    }
  }
  else if(guid=="64195d7a-b900-1521-abf3-fdfe0b930aee") {
    res.status(200).send("polycyber{in53cur3_guid_v3r51on_on3_bdf23f1a}");
  }
  else {
    if (language === 'fr') {
      res.status(200).send("Ceci n'est pas un code valide. Il faut être plus sage!");
    }
    else {
      res.status(200).send("This is not a valid code. You need to be wiser!");
    }
  }
});

app.listen(port, () => {
  return console.log(`Express is listening at http://localhost:${port}`);
});
