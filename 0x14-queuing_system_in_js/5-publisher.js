import redis from 'redis';

const pub = redis.createClient();
pub.on('connect', (error) => {
  console.error('Redis client connected to the server');
});
pub.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(``);
    pub.publish('holberton school channel', `${message}`);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
