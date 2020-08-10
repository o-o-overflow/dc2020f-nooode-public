var express = require('express');
var router = express.Router();
var fs = require("fs");

/* GET home page. */
router.get('/:id', function(req, res, next) {
  let config = res.locals.config;
  let data = fs.readFileSync(config.filepath).toString()
  data = JSON.parse(data)
  tiles = [
    "data-piece1",
    "data-piece2",
    "data-piece3",
    "data-piece4",
    "data-piece5",
    "data-piece6",
    "data-piece7",
    "data-piece8",
    "data-piece9",
  ].sort(function() {
    return .5 - Math.random();
  });
  if (data["treasure"] == req.params.id) 
    res.render('index', { title: 'Nooode', tiles: tiles, solved: "Congrats! You found the treasure!" });
  else
    res.render('index', { title: 'Nooode', tiles: tiles, solved: "Keep looking!" });
});

module.exports = router;
