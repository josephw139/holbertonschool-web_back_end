const kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!(Array.isArray(jobs))) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach(job => {
    try {
      const newQueue = queue.create('push_notification_code_3', job).save((err) => {
        if (!err) {
          console.log(`Notification job created: ${newQueue.id}`);
        }
      })
      .on('complete', () => {
        console.log(`Notification job ${newQueue.id} completed`);
      })
      .on('failed', (err) => {
        console.log(console.log(`Notification job ${newQueue.id} failed: ${err}`));
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${newQueue.id} ${progress}% complete`)
      });
    } catch (err) {};
  })
}

module.exports = createPushNotificationsJobs
