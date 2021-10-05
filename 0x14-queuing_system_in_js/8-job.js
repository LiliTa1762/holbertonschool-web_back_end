function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  for (const one of jobs) {
    let job = queue.create('push_notification_code_3', one)
    .save( function (err) {
      if (!err) console.log(`Notification job created: ${job.id}`)
    })
    .on('complete', function() {
      console.log(`Notification job ${job.id} completed`)
    })
    .on('failed', function(err) {
      console.log(`Notification job ${job.id} failed: ${err}`)
    })
    .on('progress', function(progress) {
      console.log(`Notification job ${job.id} ${progress}% complete`)
    });
  };
}
export default createPushNotificationsJobs;
