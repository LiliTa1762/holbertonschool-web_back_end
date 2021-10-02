const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const q = kue.createQueue();

for (const job of jobs) {
  let one = q.create('push_notification_code_2', job)
  .save( function (err) {
    if (!err) console.log(`Notification job created: ${one.id}`)
  })
  .on('complete', function() {
    console.log(`Notification job ${one.id} completed`)
  })
  .on('failed', function(err) {
    console.log(`Notification job ${one.id} failed: ${err}`)
  })
  .on('progress', function(progress) {
    console.log(`Notification job ${one.id} ${progress}% complete`)
  })
}
