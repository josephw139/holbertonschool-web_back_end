import { createClient } from 'redis';
const redis = require('redis');
const { promisify } = require("util");

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server:'));


const setNewSchool = async (schoolName, value) => {
  const setAsync = promisify(client.set).bind(client);
  const result = await setAsync(schoolName, value);
  redis.print(null, result);
}

const displaySchoolValue = async (schoolName) => {
  const getAsync = promisify(client.get).bind(client);
  const result = await getAsync(schoolName);
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
