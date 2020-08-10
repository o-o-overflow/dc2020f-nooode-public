#!/usr/bin/env python3

import sys
import urllib.request
import urllib.parse

def check_config(url):
  path = "config"

  with urllib.request.urlopen(f'{url}/{path}') as response:
    rsp_text = response.read()
  # print(rsp_text)
  assert response.code == 200
  return

def check_config_validated(url):
  path = "config"
  data = urllib.parse.urlencode({ "test": "test" })
  data = data.encode('ascii')

  try:
    with urllib.request.urlopen(f'{url}/{path}/validated', data) as response:
      rsp_text = response.read()
  except:
    assert False
  # print(rsp_text)
  assert response.code == 200
  return


def check_config_validated_other1(url):
  path = "config"
  data = urllib.parse.urlencode({ "test": "test" })
  data = data.encode('ascii')

  with urllib.request.urlopen(f'{url}/{path}/validated/json-schema/validate', data) as response:
    rsp_text = response.read().decode('ascii').strip()
  print(rsp_text)
  assert response.code == 200
  assert rsp_text.startswith('{"validator":{"valid":true,"errors":[]},"data":{"treasure":"data-piece2"},"msg":"data is corrupted"}')
  return

def check_config_validated_other2(url):
  path = "config"
  data = urllib.parse.urlencode({ "treasure": "data-piece2" })
  data = data.encode('ascii')

  with urllib.request.urlopen(f'{url}/{path}/validated/json-schema/validate', data) as response:
    rsp_text = response.read().decode('ascii').strip()
  print(rsp_text)
  assert response.code == 200
  assert rsp_text.startswith("{\"treasure\":\"data-piece2\"}")
  return

def check_config_validated_bytes1(url):
  path = "config"
  data = urllib.parse.urlencode({ "treasure": "data-piece2" })
  data = data.encode('ascii')

  with urllib.request.urlopen(f'{url}/{path}/validated/bytes/format', data) as response:
    rsp_text = response.read().decode('ascii').strip()
  print(rsp_text)
  assert response.code == 200
  if not rsp_text.startswith("validator failed"):
      print("PUBLIC: dependency loading failed")
      sys.exit(-1)
  return


def check_config_validated_bytes2(url):
  path = "config"
  data = urllib.parse.urlencode({ "treasure": "data-piece2" })
  data = data.encode('ascii')

  try:
    with urllib.request.urlopen(f'{url}/{path}/validated/bytes/bytes', data) as response:
      rsp_text = response.read().decode('ascii').strip()
  except urllib.error.HTTPError as e:
    assert e.code == 500
    rsp_text = e.read().decode('ascii')
    assert "jsonlib[req.params.f] is not a function" in rsp_text

  return


def check_config_validated_jsonlint(url):
  path = "config"
  # import json
  # data = '{"creative?": "false"}'

  # req = urllib.request.Request(f'{url}/{path}/validated/jsonlint/parse')
  # req.add_header('Content-Type', 'application/json')

  # response = urllib.request.urlopen(req, data.encode('ascii'))
  # rsp_text = response.read().decode('ascii').strip()
  # assert response.code == 200
  # assert rsp_text.startswith("{\"treasure\":\"data-piece2\"}")
  # return


  data = urllib.parse.urlencode({ 'treasure': 'data-piece2' })
  data = data.encode('utf-8')

  try:
    with urllib.request.urlopen(f'{url}/{path}/validated/jsonlint/parse', data) as response:
      rsp_text = response.read().decode('ascii').strip()
  except urllib.error.HTTPError as e:
    print(e.reason)
    print(e.read())
    return
  print(rsp_text)
  assert response.code == 200
  assert rsp_text.startswith("{\"treasure\":\"data-piece2\"}")
  return


def main():

    host = sys.argv[1]
    port = int(sys.argv[2])
    url = f'http://{host}:{port}'

    f = urllib.request.urlopen(url)
    assert f.code == 200

    check_config(url)
    check_config_validated(url)
    check_config_validated_other1(url)
    check_config_validated_other2(url)
    # check_config_validated_jsonlint(url)

    check_config_validated_bytes1(url)
    check_config_validated_bytes2(url)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
