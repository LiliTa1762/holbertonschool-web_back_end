import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

hset(HolbertonSchools, 'Portland', 50, redis.print);
hset(HolbertonSchools, 'Seattle', 80, redis.print);
hset(HolbertonSchools, 'New York', 20, redis.print);
hset(HolbertonSchools, 'Bogota', 20, redis.print);
hset(HolbertonSchools, 'Cali', 40, redis.print);
hset(HolbertonSchools, 'Paris', 2, redis.print);

hgetall(HolbertonSchools, function(err, result) {
  console.log(result);
});
