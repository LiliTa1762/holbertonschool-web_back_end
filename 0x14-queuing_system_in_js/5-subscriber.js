import redis from 'redis';

const sub = redis.createClient();
sub.on('connect', (error) => {
  console.error('Redis client connected to the server');
});
sub.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

sub.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    sub.unsubscribe();
    sub.quit();
  }
  console.log(message);
});
sub.subscribe('holberton school channel');
