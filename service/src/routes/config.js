"use strict";
var express = require('express');
const { Server } = require('http');
var router = express.Router();
var fs = require("fs");
var _ = require('lodash');

router.get('/', function(req, res, next) {
  let config = res.locals.config;
  let data = fs.readFileSync(config.filepath).toString()
  data = JSON.parse(data)
  res.json(data);
});

router.post('/validated/:lib?/:f?', function(req, res, next) {
  let config = res.locals.config;

  if (!req.params.lib) req.params.lib = "json-schema"
  if (!req.params.f) req.params.f = "validate"

  let jsonlib = require(req.params.lib)
  let valid = jsonlib[req.params.f](req.body)
  if (!valid) {
    res.send("validator failed");
    return
  }
  let p;
  if (config.path) { 
    p = config.path;
  } else if (config.filepath) {
    p = config.filepath;
  }

  let data = fs.readFileSync(p).toString()
  try {
    data = JSON.parse(data)
    if (_.isEqual(req.body, data))
      res.json(data)
    else
    res.send({ "validator": valid, "data":data, "msg": "data is corrupted"})
  } catch {
    res.send({ "validator": valid, "data":data})
  }
});

module.exports = router