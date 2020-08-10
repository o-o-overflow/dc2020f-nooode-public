var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
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
  res.render('index', { title: 'Nooode', tiles: tiles, solved: "" });
});

module.exports = router;
