import { createClient } from 'redis';
const redis = require('redis');

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server:'));

client.on("message", function (channel, message) {
  console.log(message);
  if (message === "KILL_SERVER") {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});

client.subscribe("holberton school channel");
