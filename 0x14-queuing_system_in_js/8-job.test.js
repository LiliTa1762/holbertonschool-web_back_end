let kue = require('kue')
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const jobData = [
  {
    phoneNumber: '789789',
    message: ' This is the code to verify your account',
  }
];

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

it('create and validate jobs creation', () => {
  createPushNotificationsJobs(jobData, queue);
  expect(queue.testMode.jobs.type).to.equal(Array);
});
