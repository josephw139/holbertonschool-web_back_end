const kue = require('kue');
const queue = kue.createQueue();
const express = require('express');
import { createClient } from 'redis';


const client = createClient();
const app = express();

app.listen(1245);
app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (item) {
    res.send(item);
  } else {
    res.send({"status": "Product not found"});
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (!item) {
    res.send({"status": "Product not found"});
  }
  if (item.stock == 0) {
    res.send({"status":"Not enough stock available","itemId":itemId});
  }
  const newStock = item.stock - 1;
  reserveStockById(itemId, newStock);
  res.send({"status":"Reservation confirmed","itemId":1});
});

function reserveStockById(itemId, stock) {
  const item = getItemById(itemId);
  client.set(item.itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  const item = await util.promisify(client.get).bind(client)(itemId);
  return item.stock;
}

const listProducts = [
  {'itemId': 1, 'name': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4, 'currentQuantity': 4},
  {'itemId': 2, 'name': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10, 'currentQuantity': 10},
  {'itemId': 3, 'name': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2, 'currentQuantity': 2},
  {'itemId': 4, 'name': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5, 'currentQuantity': 5},
];

function getItemById(id) {
  for (product in listProducts) {
    if (product['id'] === id) {
      return product;
    }
  }
}